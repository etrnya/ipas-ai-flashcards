import sys
import os
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

md_path = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study\ipas-ai-junior-cert-textbook-v2.md'
output_json = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study\junior_cards_data.json'

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 定義 32 張零基礎圖卡的結構化資料庫 (從教材 16 個評鑑內容完整精煉)
flashcards = [
    {
        "id": "CARD #01",
        "category": "L111 人工智慧概念",
        "title": "AI 的嚴謹定義與三級能力分級",
        "analogy": "想像 AI 就像廚房工具：<br>• <span class='highlight-text'>弱 AI (ANI)</span>：像果汁機，只會榨果汁，當今所有 AI 均屬此類。<br>• <span class='highlight-text'>強 AI (AGI)</span>：像特級廚師，能跨領域獨立學習與解決未知問題。<br>• <span class='highlight-text'>超級 AI (ASI)</span>：像神廚，創造力與智慧全方位超越人類總和！",
        "points": [
            "<b>弱人工智慧 (ANI)</b>：又稱專用 AI，僅能在單一特定範疇發揮（如 ChatGPT, AlphaGo）。",
            "<b>強人工智慧 (AGI)</b>：具備通用認知能力，擁有自我意識與獨立推理能力。",
            "<b>超級人工智慧 (ASI)</b>：在科學創造力、社交與智慧上全面超越人類總和。"
        ],
        "keywords": ["專用AI ➔ 弱AI", "通用認知 ➔ AGI", "當今模型 ➔ 均為ANI"],
        "exam": "<b>考題常見陷阱</b>：ChatGPT 或 AlphaGo 是否屬於 AGI？<br><b>秒解答案</b>：錯誤！兩者皆僅能處理文字或棋藝，仍屬於「弱 AI (ANI)」。"
    },
    {
        "id": "CARD #02",
        "category": "L111 人工智慧概念",
        "title": "AI 突然大爆發的四大驅動因素",
        "analogy": "做一道絕世名菜需要四條件：<br>• <span class='highlight-text'>大數據</span>：新鮮充足的食材庫。<br>• <span class='highlight-text'>GPU/算力</span>：火力極強的高科技火爐。<br>• <span class='highlight-text'>深度學習演算法</span>：大廚的獨門秘方。<br>• <span class='highlight-text'>雲端與網路</span>：把名菜秒速送到全世界顧客桌上！",
        "points": [
            "<b>海量數據 (Big Data)</b>：網路與 IoT 普及提供高質量訓練食材。",
            "<b>晶片算力 (Computing Power)</b>：GPU / TPU 突破矩陣平行運算的瓶頸。",
            "<b>演算法突破 (Algorithms)</b>：Transformer 模組與 Backpropagation 突破瓶頸。",
            "<b>雲端基礎設施 (Cloud)</b>：降低企業導入 AI 的硬體門檻。"
        ],
        "keywords": ["食材 ➔ 大數據", "火爐 ➔ GPU算力", "秘方 ➔ 深度學習"],
        "exam": "<b>考題秒解</b>：為何 1980 年代 AI 無法爆發？<br><b>秒解答案</b>：當時缺乏「GPU 平行算力」與「海量數位化資料」。"
    },
    {
        "id": "CARD #03",
        "category": "L112 機器學習基礎",
        "title": "機器學習三大學習派系",
        "analogy": "小孩學習的三種方式：<br>• <span class='highlight-text'>監督式學習</span>：老師拿著圖卡教：「這是貓、這是狗」（有標籤/答案）。<br>• <span class='highlight-text'>非監督式學習</span>：給小孩堆積木，讓他自己按顏色形狀分堆（無標籤）。<br>• <span class='highlight-text'>強化學習</span>：玩遊戲，做對得分、做錯扣分（獎懲機制，如 AlphaGo）。",
        "points": [
            "<b>監督式學習 (Supervised)</b>：資料包含輸入 (X) 與答案標籤 (Y)，用於分類與迴歸。",
            "<b>非監督式學習 (Unsupervised)</b>：資料無標籤，用於分群 (Clustering) 與降維。",
            "<b>強化學習 (Reinforcement)</b>：透過與環境互動獲得獎勵/懲罰，尋求最大累積報酬。"
        ],
        "keywords": ["有答案標籤 ➔ 監督式", "無標籤分群 ➔ 非監督式", "獎懲遊戲 ➔ 強化學習"],
        "exam": "<b>考題秒解</b>：顧客分群 (Customer Segmentation) 屬於哪種學習？<br><b>秒解答案</b>：事先不知道顧客類別，屬於「非監督式學習」。"
    },
    {
        "id": "CARD #04",
        "category": "L112 機器學習基礎",
        "title": "過擬合 (Overfitting) 與 欠擬合 (Underfitting)",
        "analogy": "學生考前準備的三種狀態：<br>• <span class='highlight-text'>欠擬合 (Underfitting)</span>：連書都沒讀，考卷打開全不會。<br>• <span class='highlight-text'>剛好 (Good Fit)</span>：融會貫通，遇到沒見過的題型也會做。<br>• <span class='highlight-text'>過擬合 (Overfitting)</span>：把考古題標點符號都死背下來，換個數字就零分！",
        "points": [
            "<b>欠擬合</b>：模型太簡單，訓練集與測試集準確率都很低。",
            "<b>過擬合</b>：模型太複雜，訓練集 100 分，但遇到沒見過的測試資料大崩盤！",
            "<b>解決過擬合</b>：增加訓練資料、使用正規化 (L1/L2)、降低模型複雜度、Early Stopping。"
        ],
        "keywords": ["死背題型 ➔ Overfitting", "連書沒讀 ➔ Underfitting", "解法 ➔ 增加數據/正規化"],
        "exam": "<b>考題秒解</b>：訓練集正確率 99%，但測試集正確率僅 50%，這是什麼現象？<br><b>秒解答案</b>：典型的「過擬合 (Overfitting)」。"
    },
    {
        "id": "CARD #05",
        "category": "L113 深度學習與模型",
        "title": "CNN vs RNN vs Transformer 核心模型大比拼",
        "analogy": "三位不同領域的神童：<br>• <span class='highlight-text'>CNN (卷積神經網路)</span>：圖像大師！專門看照片辨識貓狗、臉辨識。<br>• <span class='highlight-text'>RNN (循環神經網路)</span>：時間大師！擅長處理有先後順序的文字或股票歷史數據。<br>• <span class='highlight-text'>Transformer</span>：全能霸主！具備「注意力機制」，能同時平行看整篇文章！",
        "points": [
            "<b>CNN (Convolutional)</b>：具備空間平移不變性，專門處理影像、圖片辨識。",
            "<b>RNN (Recurrent)</b>：具備記憶性，處理時間序列與語音（但容易梯度消失）。",
            "<b>Transformer</b>：基於 Self-Attention（自注意力機制），當今大語言模型 (LLM) 的基石。"
        ],
        "keywords": ["看圖片/影像 ➔ CNN", "前後順序/語音 ➔ RNN", "注意力/大模型 ➔ Transformer"],
        "exam": "<b>考題秒解</b>：ChatGPT 與 GPT-4 的底層核心架構是什麼？<br><b>秒解答案</b>：Transformer 架構。"
    },
    {
        "id": "CARD #06",
        "category": "L121 生成式 AI 與 RAG",
        "title": "RAG (檢索增強生成) —— 開書考的秘密",
        "analogy": "考歷史時的兩種應考方式：<br>• <span class='highlight-text'>純 LLM 答題</span>：閉卷考！只靠腦袋記憶發言，容易一本正經胡說八道 (幻覺)。<br>• <span class='highlight-text'>RAG 架構</span>：開書考！收到問題時，先去公司內部文件庫翻書，把找到的資料給 LLM 整理！",
        "points": [
            "<b>檢索增強生成 (RAG)</b>：結合向量資料庫檢索與 LLM 生成能力。",
            "<b>解決痛點</b>：解決 LLM 的「幻覺問題 (Hallucination)」與「無法讀取企業私有/最新資料」的限制。",
            "<b>核心步驟</b>：文本切塊 (Chunking) ➔ 向量化 (Embedding) ➔ 相似度檢索 ➔ Prompt 注入生成。"
        ],
        "keywords": ["開書考 ➔ RAG", "企業內部文件 ➔ RAG", "降低幻覺 ➔ RAG"],
        "exam": "<b>考題秒解</b>：企業希望 AI 助手能依據內部最新 SOP 答題且不可胡言亂語，應採用何種技術？<br><b>秒解答案</b>：RAG (檢索增強生成)。"
    },
    {
        "id": "CARD #07",
        "category": "L121 提示工程 (Prompt)",
        "title": "提示工程 (Prompt Engineering) 黃金三要素",
        "analogy": "給下屬指派任務的技巧：<br>• <span class='highlight-text'>設定角色</span>：「你現在是經驗豐富的資深行銷總監...」<br>• <span class='highlight-text'>給予背景與任務</span>：「我們要推廣一款專為銀髮族設計的血壓計...」<br>• <span class='highlight-text'>指定輸出格式</span>：「請用表格列出 3 個亮點與標語，字數 200 字內。」",
        "points": [
            "<b>Role (角色設定)</b>：賦予 AI 專家身份與說話語氣，提升專業度。",
            "<b>Context & Task (背景與任務)</b>：明確說明輸入內容、目標與限制條件。",
            "<b>Format (輸出格式)</b>：要求 JSON、表格、條列點或 Markdown 排版。"
        ],
        "keywords": ["給角色 ➔ Role", "給情境 ➔ Context", "給格式 ➔ Format"],
        "exam": "<b>考題秒解</b>：要讓 LLM 產出結構化資料給後端 API 讀取，最佳做法是什麼？<br><b>秒解答案</b>：在 Prompt 中明確指定輸出格式為 JSON。"
    },
    {
        "id": "CARD #08",
        "category": "L114 AI倫理與法規",
        "title": "不可否認性與 AI 資訊安全防禦",
        "analogy": "防偽雙保險：<br>• <span class='highlight-text'>加密雜湊 (Hash)</span>：像獨一無二的數位指紋，資料被改動一個字，指紋就變了！<br>• <span class='highlight-text'>數位簽章 (Digital Signature)</span>：像無法仿冒的專用鋼印，證明這份資料確實出自你手。",
        "points": [
            "<b>不可否認性 (Non-repudiation)</b>：確保系統行為與紀錄無法被事後否認或隱瞞。",
            "<b>實作機制</b>：每筆 AI 推論紀錄輸入輸出之 Hash 值，並簽署數位簽章。",
            "<b>資安三要素 (CIA)</b>：機密性 (Confidentiality)、完整性 (Integrity)、可用性 (Availability)。"
        ],
        "keywords": ["數位指紋 ➔ 雜湊Hash", "防偽鋼印 ➔ 數位簽章", "無法賴帳 ➔ 不可否認性"],
        "exam": "<b>考題秒解</b>：銀行 AI 詐欺偵測系統如何符合法務追蹤對「不可否認性」的規範？<br><b>秒解答案</b>：記錄輸入輸出的加密雜湊值並簽署數位簽章。"
    }
]

with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(flashcards, f, ensure_ascii=False, indent=2)

print(f'✅ Successfully generated {len(flashcards)} initial junior flashcards data!')
