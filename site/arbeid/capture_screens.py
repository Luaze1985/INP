import os
import asyncio
from playwright.async_api import async_playwright

async def capture():
    # Paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, "index.html")
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    screens_dir = os.path.join(current_dir, "screens")
    os.makedirs(screens_dir, exist_ok=True)
    
    mobile_path = os.path.join(screens_dir, "mobile.png")
    desktop_path = os.path.join(screens_dir, "desktop.png")
    
    print(f"Loading mockup from: {file_url}")
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        
        # 1. Capture Mobile Viewport
        print("Capturing mobile screenshot...")
        mobile_context = await browser.new_context(
            viewport={"width": 375, "height": 812},
            device_scale_factor=2,
            is_mobile=True
        )
        mobile_page = await mobile_context.new_page()
        await mobile_page.goto(file_url)
        # Wait a bit for font loading/layout
        await mobile_page.wait_for_timeout(1000)
        await mobile_page.screenshot(path=mobile_path)
        print(f"Saved mobile screenshot to {mobile_path}")
        await mobile_context.close()
        
        # 2. Capture Desktop Viewport
        print("Capturing desktop screenshot...")
        desktop_context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.5
        )
        desktop_page = await desktop_context.new_page()
        await desktop_page.goto(file_url)
        await desktop_page.wait_for_timeout(1000)
        await desktop_page.screenshot(path=desktop_path)
        print(f"Saved desktop screenshot to {desktop_path}")
        await desktop_context.close()
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
