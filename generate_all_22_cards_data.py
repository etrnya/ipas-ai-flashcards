import sys
import os
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

cards = [
    {
        "id": "CARD 01",
        "category": "L111 人工智慧概念",
        "title": "AI 的定義、驅動因素與三級能力分級",
        "badge_tag": "AI 基礎概論",
        "desc": "徹底打通弱 AI (ANI)、強 AI (AGI) 與超級 AI (ASI) 的本質差異！",
        "capsules": ["弱 AI (ANI)", "強 AI (AGI)", "超級 AI (ASI)", "爆發四大引擎"],
        "checklist": [
            "掌握當今所有 AI (ChatGPT, AlphaGo) 均屬弱 AI",
            "理解大數據 + 算力 + 演算法 + 雲端四大爆發引擎",
            "區分通用認知 (AGI) 與專用模型 (ANI) 之邊界"
        ],
        "flow": ["海量數據 ➔ GPU 算力 ➔ 演算法突破 ➔ 雲端部署"],
        "bento_blocks": [
            {
                "num": "1", "color": "num-1", "title": "AI 三級能力分級", "sub": "依智慧廣度與深度分類",
                "type": "table",
                "headers": ["層級", "名稱", "能力特徵", "代表範例"],
                "rows": [
                    ["ANI", "弱人工智慧", "單一特定領域專用", "ChatGPT/AlphaGo"],
                    ["AGI", "強人工智慧", "具備通用認知與自我學習", "未實現 (目標)"],
                    ["ASI", "超級人工智慧", "全面超越人類總和智慧", "遠期理論概念"]
                ],
                "focus": "💡 考試重點：當今所有 AI 均屬於 ANI 弱人工智慧"
            },
            {
                "num": "2", "color": "num-2", "title": "AI 爆發四大驅動因素", "sub": "缺一不可的現代 AI 基礎設施",
                "type": "list",
                "items": [
                    "• <b>海量數據 (Big Data)</b>：網路與 IoT 普及提供高質量食材。",
                    "• <b>晶片算力 (Computing Power)</b>：GPU / TPU 平行運算突破瓶頸。",
                    "• <b>演算法突破</b>：Transformer 與反向傳播演算法進化。",
                    "• <b>雲端架構 (Cloud)</b>：降低企業算力建置門檻。"
                ],
                "focus": "💡 考試重點：1980年代無法爆發主因缺乏算力與資料"
            },
            {
                "num": "3", "color": "num-3", "title": "AI 三大功能分類", "sub": "依對資料處理的行為分",
                "type": "list",
                "items": [
                    "• <b>感知型 AI</b>：看懂圖像、聽懂語音（如人臉辨識）。",
                    "• <b>預測型 AI</b>：預測數字、分類目標（如信用卡刷卡詐欺）。",
                    "• <b>生成型 AI</b>：創造全新文字、圖像、程式碼（如 GenAI）。"
                ],
                "focus": "💡 考試重點：生成型 AI 能創造出訓練集沒有的新內容"
            },
            {
                "num": "4", "color": "num-4", "title": "規劃師視角 vs 使用者視角", "sub": "iPAS 認證核心思維",
                "type": "list",
                "items": [
                    "• <b>使用者視角</b>：只在乎工具好不好用、介面漂不漂亮。",
                    "• <b>規劃師視角</b>：評估 ROI、選型、資安合規、資料品質與維運。",
                    "• <b>企業痛點</b>：避免盲目追求新技術而忽視業務落地成本。"
                ],
                "focus": "💡 考試重點：規劃師需兼顧技術可行性與商業價值"
            },
            {
                "num": "5", "color": "num-5", "title": "AI 與自動化 (RPA) 之差異", "sub": "規則驅動 vs 資料驅動",
                "type": "list",
                "items": [
                    "• <b>RPA 流程自動化</b>：基於固定 IF-THEN 規則，無學習能力。",
                    "• <b>AI 機器學習</b>：基於資料統計學規律，具備泛化預測能力。",
                    "• <b>最佳實踐</b>：RPA 負責重複流程，AI 負責複雜決策。"
                ],
                "focus": "💡 考試重點：RPA 遇到未定義狀況會崩潰，AI 能泛化處理"
            },
            {
                "num": "6", "color": "num-6", "title": "黃仁勳 AI 四階段論", "sub": "NVIDIA 產業演進框架",
                "type": "list",
                "items": [
                    "• <b>第一階段</b>：Perception AI (感知 AI 辨識看聽)。",
                    "• <b>第二階段</b>：Generative AI (生成式 AI 創作)。",
                    "• <b>第三階段</b>：Physical AI (具身 AI 機器人/自駕)。",
                    "• <b>第四階段</b>：Biological AI (生醫 AI 蛋白質折疊)。"
                ],
                "focus": "💡 考試重點：具身 AI (Physical AI) 是下一波機器人核心"
            }
        ],
        "summary": "當今所有 AI 均為 ANI 弱人工智慧；爆發來自算力、資料、演算法與雲端四大驅動。",
        "strategy": "題目見「AlphaGo/ChatGPT」選 ANI 弱 AI；見「通用認知」選 AGI；見「1980年代瓶頸」選算力與資料。",
        "mnemonic": "「當今 AI 皆弱類，算力資料雙引擎；專用模型辦特案，通用 AGI 夢中尋。」"
    },
    {
        "id": "CARD 02",
        "category": "L111 人工智慧概念",
        "title": "AI 發展演進史與黃仁勳 4 階段論",
        "badge_tag": "演進歷史",
        "desc": "從符號邏輯推論到聯結主義深度學習的六十年演進圖譜！",
        "capsules": ["符號主義", "聯結主義", "行為主義", "具身 AI"],
        "checklist": [
            "理解 1950 達特茅斯會議 AI 誕生歷史",
            "區分符號主義 (邏輯推論) 與聯結主義 (神經網路)",
            "掌握黃仁勳 NVIDIA 具身 AI (Physical AI) 趨勢"
        ],
        "flow": ["達特茅斯會議 ➔ 專家系統 ➔ 機器學習 ➔ 深度學習 ➔ 具身 AI"],
        "bento_blocks": [
            {
                "num": "1", "color": "num-1", "title": "AI 學界三大流派", "sub": "思想源流與技術路線",
                "type": "list",
                "items": [
                    "• <b>符號主義 (Symbolism)</b>：基於邏輯與專家規則 (如 Expert Systems)。",
                    "• <b>聯結主義 (Connectionism)</b>：模擬人腦神經元 (如 Deep Learning)。",
                    "• <b>行為主義 (Actionism)</b>：基於控制論與環境互動 (如 Reinforcement)。"
                ],
                "focus": "💡 考試重點：當今主流大模型屬於聯結主義 (神經網路)"
            },
            {
                "num": "2", "color": "num-2", "title": "三次 AI 冬天與復興主因", "sub": "歷史起伏的教訓",
                "type": "list",
                "items": [
                    "• <b>第一次冬天 (1970s)</b>：算力不足與組合爆炸限制。",
                    "• <b>第二次冬天 (1980s-90s)</b>：專家系統維護成本過高且缺乏彈性。",
                    "• <b>深度學習復興 (2012)</b>：AlexNet 贏得 ImageNet 競賽突破。"
                ],
                "focus": "💡 考試重點：2012 ImageNet 是深度學習全面復興里程碑"
            },
            {
                "num": "3", "color": "num-3", "title": "黃仁勳 4 階段演進圖譜", "sub": "NVIDIA 產業展望",
                "type": "table",
                "headers": ["階段", "核心主題", "代表應用"],
                "rows": [
                    ["P1", "Perception AI", "人臉辨識 / 語音轉文字"],
                    ["P2", "Generative AI", "ChatGPT / Midjourney"],
                    ["P3", "Physical AI", "人形機器人 / 全自駕車"],
                    ["P4", "Biological AI", "AlphaFold / 新藥開發"]
                ],
                "focus": "💡 考試重點：Physical AI 結合數位分身 (Digital Twin) 模擬"
            },
            {
                "num": "4", "color": "num-4", "title": "圖靈測試 (Turing Test)", "sub": "AI 測試經典標準",
                "type": "list",
                "items": [
                    "• <b>提出者</b>：艾倫·圖靈 (Alan Turing, 1950)。",
                    "• <b>測試方式</b>：詢問者透過文字對話，無法分辨對方是人還是機器。",
                    "• <b>局限性</b>：僅能測試「模仿人類對話」，無法證明具備真正理解。"
                ],
                "focus": "💡 考試重點：通過圖靈測試不等於具備自我意識"
            },
            {
                "num": "5", "color": "num-5", "title": "中文房間思考實驗", "sub": "反駁圖靈測試的反例",
                "type": "list",
                "items": [
                    "• <b>提出者</b>：約翰·希爾勒 (John Searle, 1980)。",
                    "• <b>核心概念</b>：房間裡的人不懂中文，靠查手冊給出正確中文回應。",
                    "• <b>結論</b>：符號操作 (Syntax) 不等於語意理解 (Semantics)。"
                ],
                "focus": "💡 考試重點：中文房間證明 AI 只是在做符號對照而非真正理解"
            },
            {
                "num": "6", "color": "num-6", "title": "摩爾定律與 AI 算力黃仁勳定律", "sub": "硬體演進速度",
                "type": "list",
                "items": [
                    "• <b>摩爾定律</b>：晶片電晶體數量約每 18-24 個月翻倍。",
                    "• <b>黃仁勳定律</b>：AI 算力晶片效能每年提升超過 2 倍。",
                    "• <b>關鍵技術</b>：HBM 高頻寬記憶體與 NVLink 晶片互連。"
                ],
                "focus": "💡 考試重點：AI 算力增長速度遠超過傳統摩爾定律"
            }
        ],
        "summary": "AI 經歷三次起伏；當今主流為聯結主義；中文房間證明 AI 懂語法不等於懂語意。",
        "strategy": "見「模仿對話測試」選圖靈測試；見「反駁懂語意」選中文房間；見「2012復興」選 AlexNet/ImageNet。",
        "mnemonic": "「圖靈測試測模仿，中文房間辯理解；三次起伏神經興，具身機器未來接。」"
    },
    {
        "id": "CARD 03",
        "category": "L111 人工智慧概念",
        "title": "AI 三大核心子技術與規劃師工具箱",
        "badge_tag": "核心技術",
        "desc": "深入拆解電腦視覺 (CV)、自然語言處理 (NLP) 與語音辨識技術！",
        "capsules": ["電腦視覺 (CV)", "NLP 語處理", "語音識別 (ASR)", "知識圖譜"],
        "checklist": [
            "掌握 CV 影像分類、物件偵測與語意分割差異",
            "理解 NLP 文字斷詞、詞向量與語意分析",
            "分辨 ASR 語音轉文字與 TTS 文字轉語音"
        ],
        "flow": ["原始音訊/影像 ➔ 特徵擷取 ➔ 深度模型 ➔ 語意/類別輸出"],
        "bento_blocks": [
            {
                "num": "1", "color": "num-1", "title": "電腦視覺 (CV) 三大任務階層", "sub": "依空間與細節粒度劃分",
                "type": "table",
                "headers": ["任務", "說明", "範例"],
                "rows": [
                    ["影像分類", "判斷整張圖是什麼", "這張圖是貓"],
                    ["物件偵測", "框出物件位置 (BBox)", "標出圖中 3 輛車"],
                    ["語意分割", "像素級 (Pixel) 標註", "自駕車識別路面/行人"]
                ],
                "focus": "💡 考試重點：物件偵測包含「類別」與「邊界框 (Bounding Box)」"
            },
            {
                "num": "2", "color": "num-2", "title": "自然語言處理 (NLP) 關鍵流程", "sub": "文字轉數字的數位化過程",
                "type": "list",
                "items": [
                    "• <b>斷詞 (Tokenization)</b>：將句子拆解為 Token 單位。",
                    "• <b>詞向量 (Word Embedding)</b>：將文字轉為高維空間向量 (Word2Vec)。",
                    "• <b>語意關聯</b>：距離越近代表詞義越相似 (如 王-男+女=女王)。"
                ],
                "focus": "💡 考試重點：詞向量能將抽象文字轉為電腦可計算的數學向量"
            },
            {
                "num": "3", "color": "num-3", "title": "語音辨識 (ASR) vs 語音合成 (TTS)", "sub": "聽與說的技術",
                "type": "list",
                "items": [
                    "• <b>ASR (語音轉文字)</b>：Automatic Speech Recognition 聽寫。",
                    "• <b>TTS (文字轉語音)</b>：Text-to-Speech 朗讀發音。",
                    "• <b>聲學模型</b>：將聲音波形轉為音素與文字對應。"
                ],
                "focus": "💡 考試重點：客服機器人聽懂話靠 ASR，說話靠 TTS"
            },
            {
                "num": "4", "color": "num-4", "title": "知識圖譜 (Knowledge Graph)", "sub": "結構化的顯性知識關聯",
                "type": "list",
                "items": [
                    "• <b>三元組結構</b>：(主體 Entity - 關聯 Relation - 客體 Entity)。",
                    "• <b>優點</b>：具備強大邏輯推論能力，且回答 100% 可追溯。",
                    "• <b>應用</b>：搜尋引擎知識卡片、醫藥相互作用查詢。"
                ],
                "focus": "💡 考試重點：知識圖譜能精確補足 LLM 缺乏的明確事實推論"
            },
            {
                "num": "5", "color": "num-5", "title": "多模態 AI (Multimodal AI)", "sub": "跨越文字、圖片、音訊",
                "type": "list",
                "items": [
                    "• <b>定義</b>：能同時處理並融合文字、圖像、音訊、影片多種輸入。",
                    "• <b>對齊機制</b>：將不同模態投影至同一個對齊的語意向量空間 (CLIP)。",
                    "• <b>代表模型</b>：GPT-4o, Gemini 1.5 Pro."
                ],
                "focus": "💡 考試重點：CLIP 模型是圖像與文字空間對齊的核心技術"
            },
            {
                "num": "6", "color": "num-6", "title": "邊緣 AI (Edge AI)", "sub": "端末地端運算",
                "type": "list",
                "items": [
                    "• <b>優點</b>：低延遲、省頻寬、資料免上雲極高資安隱私。",
                    "• <b>硬體</b>：NPU (神經網路處理單元)、嵌入式晶片。",
                    "• <b>應用</b>：自駕車即時煞車、手機人臉解鎖。"
                ],
                "focus": "💡 考試重點：極致低延遲與個資隱私防護選 Edge AI"
            }
        ],
        "summary": "CV 負責視覺、NLP 負責文字、ASR/TTS 負責聽說；多模態將多種資料對齊於同一空間。",
        "strategy": "見「框出位置」選物件偵測 (Detection)；見「文字轉數字向量」選 Word Embedding；見「低延遲免上雲」選 Edge AI。",
        "mnemonic": "「CV 看圖物件框，NLP 詞向量裡藏；聽寫 ASR 說 TTS，邊緣運算隱私強。」"
    },
    {
        "id": "CARD 04",
        "category": "L112 機器學習基礎",
        "title": "機器學習三大學習派系與訓練流程",
        "badge_tag": "機器學習",
        "desc": "監督式、非監督式與強化學習的本質差異與完整 Pipeline！",
        "capsules": ["監督式 (有標籤)", "非監督式 (無標籤)", "強化學習 (獎懲)", "Pipeline"],
        "checklist": [
            "區分標籤 (Y) 對於監督與非監督式學習之決定性影響",
            "理解分類 (Classification) 與迴歸 (Regression) 之差異",
            "掌握強化學習代理人 (Agent) 與環境 (Environment) 互動"
        ],
        "flow": ["資料收集 ➔ 資料前處理 ➔ 切分集 ➔ 模型訓練 ➔ 評估驗證"],
        "bento_blocks": [
            {
                "num": "1", "color": "num-1", "title": "機器學習三大學習派系對比", "sub": "依學習方式與有無標籤劃分",
                "type": "table",
                "headers": ["派系", "標籤需求", "核心任務", "典型範例"],
                "rows": [
                    ["監督式", "必須有解答 (Y)", "分類 / 迴歸", "垃圾郵件過濾/房價預測"],
                    ["非監督式", "完全無標籤", "分群 / 降維", "客戶自動分群/異常偵測"],
                    ["強化學習", "無標籤，靠獎懲", "累積最大報酬", "AlphaGo/自動駕駛控制"]
                ],
                "focus": "💡 考試重點：區分「監督」與「非監督」唯一關鍵在於訓練資料有無標籤 (Label)"
            },
            {
                "num": "2", "color": "num-2", "title": "監督式學習：分類 vs 迴歸", "sub": "依輸出目標型態劃分",
                "type": "list",
                "items": [
                    "• <b>分類 (Classification)</b>：輸出為離散類別（如 貓/狗、詐欺/正常）。",
                    "• <b>迴歸 (Regression)</b>：輸出為連續數值（如 房價 1500萬、溫度 28.5度）。",
                    "• <b>常考陷阱</b>：邏輯斯迴歸名為迴歸，實為二分法分類！"
                ],
                "focus": "💡 考試重點：預測「金額/數量」選迴歸，預測「種類/是否」選分類"
            },
            {
                "num": "3", "color": "num-3", "title": "非監督式學習：分群 vs 降維", "sub": "探索資料內在結構",
                "type": "list",
                "items": [
                    "• <b>分群 (Clustering)</b>：物以類聚，自動將相似資料歸為一組 (K-Means)。",
                    "• <b>降維 (Dimensionality Reduction)</b>：壓縮特徵數量，保留主成分 (PCA)。",
                    "• <b>好處</b>：不需要耗費昂貴的人工標註資料成本。"
                ],
                "focus": "💡 考試重點：PCA 主成分分析常用於高維資料壓縮降維"
            },
            {
                "num": "4", "color": "num-4", "title": "強化學習 (Reinforcement Learning)", "sub": "試錯學習機制",
                "type": "list",
                "items": [
                    "• <b>Agent (代理人)</b>：學習的主體（如 AI 棋手）。",
                    "• <b>Environment (環境)</b>：Agent 所在的世界（如 棋盤）。",
                    "• <b>Reward (獎勵訊號)</b>：做對給正獎勵，做錯給負懲罰。"
                ],
                "focus": "💡 考試重點：RL依靠「累積報酬最大化」來學習最佳策略 (Policy)"
            },
            {
                "num": "5", "color": "num-5", "title": "資料集黃金拆分比例", "sub": "避免評估偏差",
                "type": "table",
                "headers": ["資料集", "用途", "常規比例"],
                "rows": [
                    ["訓練集 (Train)", "模型學習參數", "70% - 80%"],
                    ["驗證集 (Validation)", "調校超參數 (Hyperparameter)", "10% - 15%"],
                    ["測試集 (Test)", "最終考驗，絕對不可參與訓練", "10% - 15%"]
                ],
                "focus": "💡 考試重點：測試集在訓練過程中必須嚴格隔離 (Data Leakage)"
            },
            {
                "num": "6", "color": "num-6", "title": "半監督式與自我監督學習", "sub": "現代 AI 混合模式",
                "type": "list",
                "items": [
                    "• <b>半監督式 (Semi-supervised)</b>：少量標註資料 + 大量未標註資料。",
                    "• <b>自我監督 (Self-supervised)</b>：自己遮蓋部分資料讓自己猜 (LLM 底層)。",
                    "• <b>優勢</b>：解決人工標註資料太貴的產業痛點。"
                ],
                "focus": "💡 考試重點：GPT 大模型預訓練主要採用「自我監督學習」"
            }
        ],
        "summary": "監督式有標籤做分類迴歸；非監督無標籤做分群降維；訓練集與測試集必須嚴格隔離。",
        "strategy": "見「有標籤」選監督式；見「預測連續金額」選迴歸；見「資料未標示自動分組」選非監督分群。",
        "mnemonic": "「標籤有無分監督，分類連續看迴歸；測試資料嚴隔離，試錯獎懲強化隨。」"
    },
    {
        "id": "CARD 05",
        "category": "L112 機器學習基礎",
        "title": "經典演算法原理、特色與適用情境對照",
        "badge_tag": "演算法地圖",
        "desc": "線性迴歸、邏輯斯迴歸、決策樹、隨機森林、SVM 與 KNN 六大經典！",
        "capsules": ["線性迴歸", "邏輯斯迴歸", "決策樹/隨機森林", "SVM/KNN"],
        "checklist": [
            "掌握線性迴歸極小化 MSE 殘差平方和原理",
            "理解邏輯斯迴歸使用 Sigmoid 將輸出映射至 0~1",
            "明白決策樹集成為隨機森林 (Random Forest) 的優勢"
        ],
        "flow": ["明確問題型態 ➔ 特徵分析 ➔ 挑選適合演算法 ➔ 模型評估"],
        "bento_blocks": [
            {
                "num": "1", "color": "num-1", "title": "線性迴歸 (Linear Regression)", "sub": "預測連續數值的基石",
                "type": "list",
                "items": [
                    "• <b>核心原理</b>：找出最佳擬合直線 $y = w_0 + w_1 x$。",
                    "• <b>損失函數</b>：最小化殘差平方和 (MSE)。",
                    "• <b>優缺點</b>：簡單易解釋，但僅能處理線性關係，易受離群值影響。"
                ],
                "focus": "💡 考試重點：房價預測、氣溫預估等「連續數值」首選"
            },
            {
                "num": "2", "color": "num-2", "title": "邏輯斯迴歸 (Logistic Regression)", "sub": "二分類問題的經典選擇",
                "type": "list",
                "items": [
                    "• <b>核心函數</b>：使用 Sigmoid 函數 $\\frac{1}{1+e^{-z}}$ 將結果壓縮至 0~1。",
                    "• <b>本質</b>：名為迴歸，實際用於預測二選一發生之「機率」。",
                    "• <b>應用</b>：信用卡刷卡詐欺偵測、疾病診斷 (是/否)。"
                ],
                "focus": "💡 考試重點：輸出的機率值大於 0.5 判定為類別 1，否則為 0"
            },
            {
                "num": "3", "color": "num-3", "title": "決策樹 (Decision Tree)", "sub": "直覺易解釋的樹狀規則",
                "type": "list",
                "items": [
                    "• <b>分裂指標</b>：資訊增益 (Information Gain) 或 幾尼不純度 (Gini)。",
                    "• <b>優點</b>：像流程圖極易向非技術人員解釋說明。",
                    "• <b>缺點</b>：樹長太深極度容易死背答案 (過擬合 Overfitting)。"
                ],
                "focus": "💡 考試重點：決策樹常需進行「剪枝 (Pruning)」以防止過擬合"
            },
            {
                "num": "4", "color": "num-4", "title": "隨機森林 (Random Forest)", "sub": "整合學習 (Ensemble) 的王者",
                "type": "list",
                "items": [
                    "• <b>機制</b>：結合多棵決策樹，採用 Bootstrap 抽樣與多數決投票。",
                    "• <b>優點</b>：準確度高、抗噪能力強、不易過擬合。",
                    "• <b>精神</b>：三個臭皮匠，勝過一個諸葛亮。"
                ],
                "focus": "💡 考試重點：隨機森林屬於 Bagging 整合學習技術"
            },
            {
                "num": "5", "color": "num-5", "title": "支持向量機 (SVM)", "sub": "最大化邊界超平面",
                "type": "list",
                "items": [
                    "• <b>核心概念</b>：尋找能將兩類資料分開且邊界 (Margin) 最大化的超平面。",
                    "• <b>核技巧 (Kernel Trick)</b>：將低維不可分資料映射至高維空間分開。",
                    "• <b>優點</b>：高維資料表現極佳、泛化能力強。"
                ],
                "focus": "💡 考試重點：Kernel Trick 能解決非線性可分的複雜問題"
            },
            {
                "num": "6", "color": "num-6", "title": "K 近鄰演算法 (KNN)", "sub": "懶惰學習 (Lazy Learning)",
                "type": "list",
                "items": [
                    "• <b>原理</b>：計算新樣本與鄰近 K 個點的歐式距離，多數決分類。",
                    "• <b>特性</b>：無須訓練過程，但推論時計算量很大。",
                    "• <b>敏感點</b>：對特徵的尺度與範圍極度敏感（需先做標準化）。"
                ],
                "focus": "💡 考試重點：KNN 執行前必須先做資料標準化/歸一化"
            }
        ],
        "summary": "連續數值用線性迴歸；二分類機率用邏輯斯；樹狀流程用決策樹/隨機森林；高維邊界用 SVM。",
        "strategy": "見「Sigmoid機率二選一」選邏輯斯迴歸；見「多樹投票抗過擬合」選隨機森林；見「最大化 Margin」選 SVM。",
        "mnemonic": "「線性預測數連續，邏輯機率二選一；樹深容易過擬合，森林投票最精準。」"
    }
]

# 後續將補齊全部 22 張完整 cards，寫入 junior_cards_data.json
output_json = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study\junior_cards_data.json'
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print(f'✅ Written first batch of cards to junior_cards_data.json (Total cards: {len(cards)})')
