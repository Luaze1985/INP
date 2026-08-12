import os
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# Full visuell gjennomgang: alle seksjoner + full-page, desktop + mobil.
# reduced_motion="reduce" => scroll-reveal er av, innholdet er fullt synlig.

SECTIONS = [
    "sec-intro",
    "sec-challenge",
    "sec-what-we-know",
    "sec-what-we-dont-know",
    "sec-what-verified-will-find-out",
    "sec-how-we-work",
    "sec-status",
    "footer-kapitaldagen",
]


async def capture():
    d = os.path.dirname(os.path.abspath(__file__))
    html_path = Path(d, "..", "web", "index.html").resolve()
    file_url = html_path.as_uri()
    out = os.path.join(d, "screens", "review")
    os.makedirs(out, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for label, vp, dsf, mobile in [
            ("desktop", {"width": 1440, "height": 900}, 1.25, False),
            ("mobile", {"width": 375, "height": 812}, 2, True),
        ]:
            ctx = await browser.new_context(
                viewport=vp, device_scale_factor=dsf,
                is_mobile=mobile, reduced_motion="reduce",
            )
            page = await ctx.new_page()
            await page.goto(file_url)
            await page.wait_for_timeout(1200)

            targets_ok = await page.evaluate("""
                [...document.querySelectorAll('a[href^="#"]')].every((link) => {
                    const href = link.getAttribute('href');
                    return href && document.querySelector(href);
                })
            """)
            assert targets_ok, f"{label}: internal link without target"
            assert await page.evaluate(
                "document.documentElement.scrollWidth <= window.innerWidth"
            ), f"{label}: horizontal overflow"
            assert await page.evaluate(
                "matchMedia('(prefers-reduced-motion: reduce)').matches"
            ), f"{label}: reduced-motion context not active"
            assert await page.evaluate(
                "getComputedStyle(document.documentElement).scrollBehavior === 'auto'"
            ), f"{label}: smooth scroll remains active with reduced motion"
            assert await page.locator(".scroll-prompt").evaluate(
                "el => getComputedStyle(el).animationName === 'none'"
            ), f"{label}: scroll animation remains active with reduced motion"

            image_treatments = await page.evaluate("""
                [...document.querySelectorAll('.story-section')].map((section) => ({
                    id: section.id,
                    image: getComputedStyle(section).backgroundImage,
                    blend: getComputedStyle(section).backgroundBlendMode,
                }))
            """)
            section_images = [item["image"] for item in image_treatments]
            main_section_count = len(SECTIONS) - 1
            assert len(section_images) == main_section_count, (
                f"{label}: expected {main_section_count} main images, got {len(section_images)}"
            )
            assert len(set(section_images)) == len(section_images), (
                f"{label}: duplicate main-section image"
            )
            assert all(item["blend"] == "normal" for item in image_treatments), (
                f"{label}: inconsistent main-image blend treatment"
            )

            await page.keyboard.press("Tab")
            assert await page.locator(".skip-link").evaluate(
                "el => el === document.activeElement"
            ), f"{label}: skip link is not first focus target"

            if mobile:
                toggle = page.locator("#menu-toggle-btn")
                await toggle.click()
                assert await toggle.get_attribute("aria-expanded") == "true"
                assert await page.locator("body").evaluate(
                    "el => el.classList.contains('menu-open')"
                )
                await page.keyboard.press("Escape")
                assert await toggle.get_attribute("aria-expanded") == "false"
                assert not await page.locator("body").evaluate(
                    "el => el.classList.contains('menu-open')"
                )

            footer_image = page.locator(".footer-photo__img")
            if await footer_image.count():
                await footer_image.scroll_into_view_if_needed()
                await footer_image.evaluate(
                    "el => el.complete ? Promise.resolve() : new Promise((resolve, reject) => { el.addEventListener('load', resolve, {once:true}); el.addEventListener('error', reject, {once:true}); })"
                )
                assert await footer_image.evaluate(
                    "el => el.complete && el.naturalWidth > 0 && el.naturalHeight > 0"
                ), f"{label}: footer image did not decode"

            checks = "anchors focus motion overflow unique-images color-treatment"
            if mobile:
                checks += " menu"
            print("verified", label, checks)

            # Full-page
            await page.screenshot(
                path=os.path.join(out, f"{label}-FULL.png"), full_page=True)
            print("saved", f"{label}-FULL.png")

            # Per seksjon
            for s in SECTIONS:
                el = page.locator(f"#{s}")
                assert await el.count() == 1, f"{label}: missing or duplicate section {s}"
                await el.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                await el.screenshot(path=os.path.join(out, f"{label}-{s}.png"))
                print("saved", f"{label}-{s}.png")

            await ctx.close()

        await browser.close()


if __name__ == "__main__":
    asyncio.run(capture())
