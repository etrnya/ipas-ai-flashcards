import sys
import os
import asyncio
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

cwd = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study'
template_path = os.path.join(cwd, 'light_bento_template.html')
png_path = os.path.join(cwd, 'cards_png', 'light_bento_ai_summary_card.png')

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 900})
        await page.goto(f'file:///{template_path.replace("\\", "/")}')
        await page.screenshot(path=png_path, clip={"x": 0, "y": 0, "width": 1400, "height": 900})
        await browser.close()
        print(f'📷 Successfully rendered light bento card: {png_path}')

asyncio.run(render())
