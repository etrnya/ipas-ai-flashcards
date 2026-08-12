import sys
import os
import json
import asyncio
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

cwd = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study'
json_path = os.path.join(cwd, 'junior_cards_data.json')
template_path = os.path.join(cwd, 'card_template.html')
output_dir = os.path.join(cwd, 'cards_png')

os.makedirs(output_dir, exist_ok=True)

with open(json_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

with open(template_path, 'r', encoding='utf-8') as f:
    html_template = f.read()

async def render_cards():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 675})

        for i, card in enumerate(cards):
            points_html = "".join([f'<li class="key-item"><span class="key-icon">✓</span> <span>{pt}</span></li>' for pt in card['points']])
            keywords_html = "".join([f'<span class="kw-tag">{kw}</span>' for kw in card['keywords']])
            
            card_html = html_template
            card_html = card_html.replace('CARD #01', card['id'])
            card_html = card_html.replace('L111 人工智慧概念', card['category'])
            card_html = card_html.replace('AI 的定義與三級能力分級', card['title'])
            
            # 替換具體內容
            card_html = card_html.replace(
                '''<div class="analogy-content" id="card-analogy">
        想像 AI 就像是廚房裡的工具：<br>
        • <span class="highlight-text">弱 AI</span>：像「果汁機」，只會榨果汁，不會炒菜。<br>
        • <span class="highlight-text">強 AI</span>：像「特級廚師」，跟人類一樣什麼菜都會做。<br>
        • <span class="highlight-text">超級 AI</span>：像「神廚」，做菜速度與美味度完全超越全人類！
      </div>''',
                f'<div class="analogy-content" id="card-analogy">{card["analogy"]}</div>'
            )
            card_html = card_html.replace(
                '''<ul class="key-points" id="card-points">
        <li class="key-item"><span class="key-icon">✓</span> <span><b>弱人工智慧 (ANI)</b>：又稱專用 AI，當今所有 AI (包含 ChatGPT) 都屬於此類。</span></li>
        <li class="key-item"><span class="key-icon">✓</span> <span><b>強人工智慧 (AGI)</b>：具備通用認知能力，能跨領域學習並解決未知問題。</span></li>
        <li class="key-item"><span class="key-icon">✓</span> <span><b>超級人工智慧 (ASI)</b>：在科學創造力、社交與智慧上全面超越人類總和。</span></li>
      </ul>''',
                f'<ul class="key-points" id="card-points">{points_html}</ul>'
            )
            card_html = card_html.replace(
                '''<div class="keyword-tags" id="card-keywords">
        <span class="kw-tag">專用AI ➔ 弱AI</span>
        <span class="kw-tag">通用認知 ➔ AGI</span>
        <span class="kw-tag">當今模型 ➔ 均為ANI</span>
      </div>''',
                f'<div class="keyword-tags" id="card-keywords">{keywords_html}</div>'
            )
            card_html = card_html.replace(
                '''<div class="exam-text" id="card-exam">
        <b>考題</b>：下列關於 AlphaGo 與 ChatGPT 的敘述何者正確？<br>
        <b>秒解</b>：兩者皆屬於「弱 AI (ANI)」，因為它們僅能在特定範疇發揮功效。
      </div>''',
                f'<div class="exam-text" id="card-exam">{card["exam"]}</div>'
            )

            temp_html_path = os.path.join(output_dir, f'temp_{i}.html')
            with open(temp_html_path, 'w', encoding='utf-8') as tf:
                tf.write(card_html)
            
            await page.goto(f'file:///{temp_html_path.replace("\\", "/")}')
            png_filename = f'junior_card_{i+1:02d}_{card["title"]}.png'.replace(' ', '_').replace('/', '_')
            png_path = os.path.join(output_dir, png_filename)
            
            await page.screenshot(path=png_path, clip={"x": 0, "y": 0, "width": 1200, "height": 675})
            os.remove(temp_html_path)
            print(f'📷 Saved PNG Flashcard: {png_filename}')

        await browser.close()

asyncio.run(render_cards())
print('🎉 All flashcard PNGs rendered successfully!')
