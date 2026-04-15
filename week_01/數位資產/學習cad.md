🏗️ 核心架構：三層式自動化流程
一個運作良好的 CAD Agent 至少需要包含這三層：

1. 意圖解析層 (The Brain)
技術選型：LLM (如 GPT-4o 或 Claude 3.5)。

職責：將模糊的對話（如：「我要 3 房，主臥要大一點」）轉換為結構化參數。

輸出示例：

JSON
{
  "total_area": 85, 
  "rooms": [
    {"name": "Master", "size": [400, 350], "pos": [0, 0]},
    {"name": "Living", "size": [400, 600], "pos": [400, 0]}
  ]
}
2. 工具調用層 (The Hands)
技術選型：Python + ezdxf 庫。

職責：將上面的 JSON 參數轉化為真正的 向量座標。

為什麼選 ezdxf？ 因為它不需要啟動 AutoCAD 軟體，純後端運算，速度極快且穩定。

3. 渲染與回饋層 (The Eyes)
技術選型：matplotlib (預覽圖) 或 直接生成 .dxf。

職責：讓用戶（或 Agent 自己）看到結果。如果 Agent 發現房間重疊，它會重新計算座標。

🛠️ MVP 實作詳解：一步步構建
第一步：建立「幾何 Skill 庫」
AI 不擅長處理極其複雜的 CAD 指令，所以我們要為它封裝好簡單的 Python 函數。

Python
import ezdxf

class CADTool:
    def __init__(self):
        self.doc = ezdxf.new('R2010')
        self.msp = self.doc.modelspace()

    def draw_room(self, x, y, width, height, label):
        # 繪製矩形牆體
        points = [(x, y), (x+width, y), (x+width, y+height), (x, y+height), (x, y)]
        self.msp.add_lwpolyline(points, close=True)
        # 標註中心點
        self.msp.add_text(label, height=15).set_placement((x + width/4, y + height/2))

    def save(self, filename="floorplan.dxf"):
        self.doc.saveas(filename)
第二步：Prompt Engineering (賦予 AI 空間感)
在與 Agent 對話時，你需要給它一個 System Prompt，定義台北三房的常見規範：

「你是一個專業的台北室內設計助理。

牆厚請預設為 15cm。

門寬預設為 90cm。

當用戶說 3 房時，請確保包含 1 個主臥（含衛浴）與 2 個次臥。

請以 (0,0) 為基準點計算所有房間的相對座標，確保房間之間不重疊。」

第三步：自動化閉環
Agent 接收指令後，會寫出如下邏輯並自動執行：

計算：主臥放在 (0,0)，客廳放在 (400, 0)...

調用：執行 draw_room(0, 0, 400, 350, "主臥")。

產出：生成 output.dxf。

🏙️ 針對「台北 3 房」的空間邏輯最佳化
在 MVP 階段，Agent 應該內建一套座標偏移量算法：

公私分明動線：Agent 應優先將「客餐廳」置於中央，三間房間採放射狀或側邊分佈，這最符合台北狹長型或方正型公寓的特徵。

虛擬邊界檢查：在代碼執行前，增加一個簡單的 Python 判斷式，檢查 Rectangle_A 是否與 Rectangle_B 重疊，如果有，回傳錯誤給 LLM 重新修正座標。