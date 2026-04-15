🛠️ AI Agent Skill: CADArchitect
1. 技能概述 (Overview)
名稱: CADArchitect

用途: 將自然語言描述的建築格局轉化為精確的 .dxf (CAD) 向量檔案。

核心引擎: Python ezdxf 庫。

適用場景: 台北 3 房 2 廳 2 衛等室內設計初步建模。

2. 核心指令集 (Action Schema)
Agent 必須透過調用以下函數來執行任務：

draw_space(name, x, y, width, height)
描述: 在指定座標繪製一個封閉的矩形房間，並自動加上中心標註。

參數:

name (str): 空間名稱（如：主臥、客廳）。

x, y (int): 空間左下角的起始座標（單位：cm）。

width, height (int): 空間的寬度與深度。

add_opening(type, wall_start, wall_end, offset)
描述: 在牆體上標註門或窗的位置。

參數:

type (str): "DOOR" 或 "WINDOW"。

offset (int): 距離牆體起點的距離。

export_dxf(filename)
描述: 封裝並導出最终檔案。

3. 台北標準格局邏輯 (Standard Configuration)
Agent 在執行時應遵循以下內建規範（台北都會區適用）：

牆體厚度: 外牆 20cm，隔間牆 15cm。

天花板高度: 預設 280cm - 320cm。

基本尺寸規範:

主臥室: 至少 400cm x 350cm。

衛浴: 至少 150cm x 240cm (含乾濕分離)。

走道寬度: 至少 90cm 以利通行。

4. 實作代碼 (Python Implementation)
Python
import ezdxf

class CADSkill:
    """
    這段代碼定義了 Agent 如何操作 CAD 檔案。
    """
    def __init__(self, project_name="Taipei_Project"):
        self.doc = ezdxf.new('R2010')
        self.msp = self.doc.modelspace()
        self.units = "CM"

    def execute_draw(self, name, x, y, w, h):
        # 繪製牆線 (Polyline)
        points = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
        self.msp.add_lwpolyline(points, close=True, dxfattribs={'layer': 'WALLS'})
        
        # 放置標籤
        self.msp.add_text(name, height=15).set_placement((x + 10, y + h/2))
        return f"已在 ({x},{y}) 繪製 {name}，尺寸 {w}x{h}"

    def finalize(self, filename):
        self.doc.saveas(f"{filename}.dxf")
        return f"檔案 {filename}.dxf 已成功生成。"

# Agent 呼叫範例:
# skill = CADSkill()
# skill.execute_draw("Living Room", 0, 0, 400, 600)
# skill.execute_draw("Master Bedroom", 400, 300, 400, 300)
# skill.finalize("Taipei_3B2B_Layout")
5. Agent 思考工作流 (Reasoning Loop)
解析 (Parse): 接收用戶輸入「3 房 2 廳」。

計算 (Compute): 根據總坪數計算各房間座標，防止重疊。

繪圖 (Act): 循環執行 execute_draw 函數。

校對 (Verify): 檢查是否所有房間都已繪製且包含門口。

交付 (Deliver): 提供 .dxf 檔案下載連結。

6. 錯誤處理 (Error Handling)
重疊警告: 如果兩個房間的座標區間發生交集，Agent 必須觸發 Self-Correction 重新計算偏移量。

超出邊界: 若總面積超過用戶設定的坪數限制，Agent 需主動詢問是否縮小特定房間。