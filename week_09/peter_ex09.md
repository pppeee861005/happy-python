作業一：刪除列表中的所有負數

  x = [1, 3, 5, 0, -1, 3, -2]
  
  
  # 方法一：使用 list comprehension（推薦）  
  result = [num for num in x if num >= 0]
  print(result)  # [1, 3, 5, 0, 3]
  
  
  # 方法二：使用 for 循環
  result = []
  for num in x:
      if num >= 0:
          result.append(num)
  print(result)  # [1, 3, 5, 0, 3]
  
  
  # 方法三：filter() 函數
  result = list(filter(lambda num: num >= 0, x))
  print(result)  # [1, 3, 5, 0, 3]
  
  
  解釋：

  - 方法一：列表推導式是 Python 的優雅寫法，簡潔高效
  - 方法二：傳統循環方式，初學者容易理解
  - 方法三：函數式編程，適合處理簡單篩選
  ---
  
  
  作業二：計算嵌套列表中負數的總個數
  y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
 
  # 方法一：雙層 for 循環（最直觀）
  count = 0
  for row in y:
      for num in row:
          if num < 0:
              count += 1
  print(f"負數個數：{count}")  # 負數個數：4
  
  
  # 方法二：sum() + list comprehension
  count = sum(1 for row in y for num in row if num < 0)
  print(f"負數個數：{count}")  # 負數個數：4
  
  
  # 方法三：先展平再計算
  flattened = [num for row in y for num in row]
  count = sum(1 for num in flattened if num < 0)
  print(f"負數個數：{count}")  # 負數個數：4

  
  
  解釋：
  - 方法一：雙層循環，逐一檢查每個元素
  - 方法二：生成器表達式結合 sum()，高效且簡潔
  - 方法三：先展平列表再計算，邏輯清晰

  ---
  核心概念速記 📌

  ┌────────────────────┬───────────────┬───────────────────────────────────┐
  │        概念        │     用途      │               例子                │
  ├────────────────────┼───────────────┼───────────────────────────────────┤
  │ if 條件            │ 判斷真假      │ if num < 0:                       │
  ├────────────────────┼───────────────┼───────────────────────────────────┤
  │ for 迴圈           │ 遍歷序列      │ for num in x:                     │
  ├────────────────────┼───────────────┼───────────────────────────────────┤
  │ List Comprehension │ 簡潔篩選/轉換 │ [x for x in list if condition]    │
  ├────────────────────┼───────────────┼───────────────────────────────────┤
  │ sum() + generator  │ 快速計數      │ sum(1 for x in list if condition) │
  └────────────────────┴───────────────┴───────────────────────────────────┘



--------------------------------------------------

這是一個 列表推導式 (List Comprehension)，來逐部分解讀：

  result = [num for num in x if num >= 0]

  結構分解：

  | 部分           | 說明                                                        |
  |----------------|-------------------------------------------------------------|
  | result = [...] | 建立一個新的列表並指派給變數 result                         |
  | for num in x   | 迭代遍歷 x 這個可迭代物件（如列表），每次取一個元素存到 num |
  | if num >= 0    | 條件篩選：只保留滿足這個條件的元素                          |
  | num            | 最終加入新列表的值                                          |

  中文解讀：
  從 x 中逐個取出每個 num，如果 num 大於等於 0，就把它加入新列表；最後把結果儲存在 result

  實例：
  x = [5, -3, 8, -1, 0, 2]
  result = [num for num in x if num >= 0]
  print(result)  # 輸出：[5, 8, 0, 2]

  等價的傳統寫法：
  result = []
  for num in x:
      if num >= 0:
          result.append(num)

  列表推導式就是上面這種常見模式的簡潔寫法。
