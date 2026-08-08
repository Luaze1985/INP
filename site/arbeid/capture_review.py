import os
import asyncio
from playwright.async_api import async_playwright

# Full visuell gjennomgang: alle seksjoner + full-page, desktop + mobil.
# reduced_motion="reduce" => scroll-reveal er av, innholdet er fullt synlig.

SECTIONS = [
    "sec-intro",
    "sec-challenge",
    "sec-what-we-know",
    "sec-what-we-dont-know",
    "sec-what-verified-will-find-out",
    "sec-why-us",
    "sec-status",
]


async def capture():
    d = os.path.dirname(os.path.abspath(__file__))
    file_url = f"file:///{os.path.join(d, 'index.html').replace(os.sep, '/')}"
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

            # Full-page
            await page.screenshot(
                path=os.path.join(out, f"{label}-FULL.png"), full_page=True)
            print("saved", f"{label}-FULL.png")

            # Per seksjon
            for s in SECTIONS:
                el = page.locator(f"#{s}")
                if await el.count() == 0:
                    print("MISSING", s)
                    continue
                await el.scroll_into_view_if_needed()
                await page.wait_for_timeout(300)
                await el.screenshot(path=os.path.join(out, f"{label}-{s}.png"))
                print("saved", f"{label}-{s}.png")

            await ctx.close()

        await browser.close()


if __name__ == "__main__":
    asyncio.run(capture())
