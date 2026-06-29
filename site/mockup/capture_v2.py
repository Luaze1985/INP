import os
import asyncio
from playwright.async_api import async_playwright

# Verifiserings-screenshots for v2-løftet.
# reduced_motion="reduce" => scroll-reveal er av, så innholdet er fullt synlig i bildet.

async def capture():
    d = os.path.dirname(os.path.abspath(__file__))
    file_url = f"file:///{os.path.join(d, 'index.html').replace(os.sep, '/')}"
    out = os.path.join(d, "screens", "v2")
    os.makedirs(out, exist_ok=True)

    desktop_sections = ["sec-intro", "sec-challenge", "sec-what-we-know",
                        "sec-what-we-dont-know", "sec-why-us"]
    mobile_sections = ["sec-why-us", "sec-what-we-know"]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # Desktop
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900},
                                        device_scale_factor=1.25, reduced_motion="reduce")
        page = await ctx.new_page()
        await page.goto(file_url)
        await page.wait_for_timeout(1200)
        for s in desktop_sections:
            el = page.locator(f"#{s}")
            await el.scroll_into_view_if_needed()
            await page.wait_for_timeout(350)
            await el.screenshot(path=os.path.join(out, f"desktop-{s}.png"))
            print("saved", f"desktop-{s}.png")
        await ctx.close()

        # Mobile
        mctx = await browser.new_context(viewport={"width": 375, "height": 812},
                                         device_scale_factor=2, is_mobile=True,
                                         reduced_motion="reduce")
        mpage = await mctx.new_page()
        await mpage.goto(file_url)
        await mpage.wait_for_timeout(1200)
        for s in mobile_sections:
            el = mpage.locator(f"#{s}")
            await el.scroll_into_view_if_needed()
            await mpage.wait_for_timeout(300)
            await el.screenshot(path=os.path.join(out, f"mobile-{s}.png"))
            print("saved", f"mobile-{s}.png")
        await mctx.close()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
