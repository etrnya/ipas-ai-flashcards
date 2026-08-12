import sys
import os
import json
import asyncio
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

cwd = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study'
json_path = os.path.join(cwd, 'junior_cards_data.json')
template_path = os.path.join(cwd, 'light_bento_template.html')
output_dir = os.path.join(cwd, 'cards_png')

os.makedirs(output_dir, exist_ok=True)

with open(json_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

with open(template_path, 'r', encoding='utf-8') as f:
    html_template = f.read()

async def render_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 900})

        for i, card in enumerate(cards):
            # 替換具體內容
            card_html = html_template
            card_html = card_html.replace('AI 基礎與演算法技術應用', card['title'])
            card_html = card_html.replace('iPAS AI 初級考綱精華', card['badge_tag'])
            card_html = card_html.replace('從資料驅動到模型訓練，徹底打通 AI 機器學習與深度學習核心邏輯！', card['desc'])
            
            # 替換總結與口訣
            card_html = card_html.replace('當今 AI 均為 ANI 弱人工智慧；監督式學習需有標籤；過擬合可用正規化與增加資料解決。', card['summary'])
            card_html = card_html.replace('題目見「連續數字」選線性迴歸；見「二選一/刷卡詐欺」選邏輯斯迴歸；見「企業文件」選 RAG。', card['strategy'])
            card_html = card_html.replace('「當今 AI 皆弱類，分群無標答案給；死背題目過擬合，開書檢索 RAG 隨。」', card['mnemonic'])

            temp_html_path = os.path.join(output_dir, f'render_temp_{i}.html')
            with open(temp_html_path, 'w', encoding='utf-8') as tf:
                tf.write(card_html)
            
            await page.goto(f'file:///{temp_html_path.replace("\\", "/")}')
            safe_title = card['title'].replace(' ', '_').replace('/', '_').replace(':', '_').replace('?', '')
            png_filename = f'junior_card_{i+1:02d}_{safe_title}.png'
            png_path = os.path.join(output_dir, png_filename)
            
            await page.screenshot(path=png_path, clip={"x": 0, "y": 0, "width": 1400, "height": 900})
            os.remove(temp_html_path)
            print(f'📷 [{i+1}/{len(cards)}] Rendered PNG: {png_filename}')

        await browser.close()

asyncio.run(render_all())
print('🎉 All 22 flashcard PNGs successfully rendered!')
