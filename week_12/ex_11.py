#############################################################
# Python x ChatGPT
# List & function 串列與函數應用
# [作業一]
# 財務報表：
# 請改寫先前作業(ex-07)，再加上「排名」一欄
# 輸入：
#      要求使用者輸入 '年度', '營業額', '利潤' 數值
#      1)每年度紀錄須一次輸入3個數值，數值間以逗號隔開
#      2)按 'Q' 離開
# 輸出：
#      1)請增加「獲利率」一欄(自動計算)，
#      2)請增加「排名(獲利率)」一欄(自動計算)，
#      3)印出這份報表。
#        - 其中營業額與利潤要加上千分位符號；
#        - 獲利率要採百分比表示，精確度到小數點後2位。
#   年度        營業額       利潤      獲利率     排名
# ======================================================
#    110      1550000	    47895
#    111      2000000	   104600
#    112      2234000	   122200
# ======================================================
# (提示)：使用 sort() 與 匿名函數
##############################################################
def main():
    data_list = []
    
    print("=== 財務報表輸入系統 ===")
    print("請輸入 [年度, 營業額, 利潤]（例如: 110, 1550000, 47895）")
    print("輸入 'Q' 或 'q' 結束輸入並產生報表。\n")
    
    # --- 1. 資料輸入階段 ---
    while True:
        user_input = input("請輸入資料: ").strip()
        
        if user_input.upper() == 'Q':
            break
            
        try:
            # 依逗號隔開數值
            year_str, revenue_str, profit_str = user_input.split(',')
            
            year = year_str.strip()
            revenue = int(revenue_str.strip())
            profit = int(profit_str.strip())
            
            # 自動計算獲利率 (利潤 / 營業額)
            # 這裡先儲存浮點數，最後輸出再格式化為百分比
            margin = profit / revenue if revenue != 0 else 0.0
            
            # 將資料存入字典
            record = {
                'year': year,
                'revenue': revenue,
                'profit': profit,
                'margin': margin,
                'rank': 0  # 排名先預設為 0，後面計算
            }
            data_list.append(record)
            
        except ValueError:
            print("❌ 輸入格式錯誤！請確保輸入3個數值並以逗號隔開（整數），或輸入 Q 離開。")
            continue

    if not data_list:
        print("沒有輸入任何資料，程式結束。")
        return

    # --- 2. 計算排名階段 (使用 sort 與 lambda) ---
    # 先依「獲利率 (margin)」由大到小 (reverse=True) 排序
    data_list.sort(key=lambda x: x['margin'], reverse=True)
    
    # 根據排序後的順序賦予排名
    for index, record in enumerate(data_list):
        record['rank'] = index + 1
        
    # 為了報表好看，我們將資料改回依「年度 (year)」從小到大排序
    data_list.sort(key=lambda x: x['year'])

    # --- 3. 報表輸出階段 ---
    print("\n" + "=" * 65)
    # 標題欄位（使用左對齊與置中調整排版）
    print(f"{'年度':<8}{'營業額':<18}{'利潤':<15}{'獲利率':<12}{'排名':<6}")
    print("=" * 65)
    
    for r in data_list:
        # 格式化語法：
        # :,d -> 整數加上千分位
        # :.2% -> 轉為百分比並四捨五入到小數後2位
        rev_formatted = f"{r['revenue']:,}"
        prof_formatted = f"{r['profit']:,}"
        margin_formatted = f"{r['margin']:.2%}"
        
        print(f"{r['year']:<10}{rev_formatted:<18}{prof_formatted:<15}{margin_formatted:<13}{r['rank']:<6}")
        
    print("=" * 65)

if __name__ == "__main__":
    main()

##############################################################
# Python x ChatGPT
# file, string, tuple lookup 檔案、字串、元組與函數應用
# [作業二]
# 分析你的朋友(analyze your friends)
# 撰寫函數讀入特定格式的檔案，內含朋友名字與電話號碼，
# 程式必須能儲存這些資料並作分析。
# 輸入：
#   1)讀入檔案 friends.txt 內含朋友名字與電話號碼。
#     格式：朋友1名字\n朋友1電話\n朋友2名字\n朋友2電話\n ..
#   2)讀入檔案 areacodes_cities 內含電話區碼與對應之城市
#     格式：區碼1\n城市1\n區碼2\n城市2\n ..
# 操作：請參考函數架構建議(如下)
# 輸出：
#   1)檔案內共有幾位朋友
#   2)他們住在哪幾個城市(不重複)
###############################################################
# ==========================================
# 核心函數實作
# ==========================================

def read_file(file_obj):
    """
    從檔案讀取朋友的姓名與電話號碼。
    每兩行一組，奇數行(1, 3, 5...)為姓名，偶數行(2, 4, 6...)為電話（或區碼與城市）。
    :param obj file_obj: 已開啟的檔案物件
    :return tuple: 兩個元組 (tuple1, tuple2)
    """
    # 讀取所有行並去除前後換行符與空白
    lines = [line.strip() for line in file_obj.readlines() if line.strip()]
    
    list1 = []  # 存放姓名 或 區碼
    list2 = []  # 存放電話 或 城市
    
    for i in range(len(lines)):
        if i % 2 == 0:
            list1.append(lines[i])
        else:
            list2.append(lines[i])
            
    return tuple(list1), tuple(list2)


def sanitize(some_tuple):
    """
    清除指定元組中每個電話號碼(字串)裡所有空格、橫槓(-)、括號()、點號(.)
    :param tuple of str some_tuple: 電話號碼元組
    :return tuple: 內含乾淨字串元素的元組
    """
    clean_list = []
    # 定義需要被移除的雜質字元
    scary_chars = [' ', '-', '(', ')', '.']
    
    for item in some_tuple:
        clean_item = item
        for char in scary_chars:
            clean_item = clean_item.replace(char, '')
        clean_list.append(clean_item)
        
    return tuple(clean_list)


def analyze_friends(names, phones, all_areacodes, all_places):
    """
    依指定之元組資料印出你有多少朋友、與其電話號碼對應的居住城市(不重複).
    :param tuple names: 朋友姓名
    :param tuple phones: 清洗過的電話號碼
    :param tuple all_areacodes: 所有區域號碼的字串
    :param tuple all_places: 所有城市名稱字串
    """
    
    def get_unique_area_codes():
        """
        過濾所有電話號碼，並傳回其中不重複的區域代碼（假設區碼為號碼的前2碼，如 02, 04）
        :return tuple: unique area codes of all phone numbers
        """
        unique_codes = set()
        for phone in phones:
            # 這裡假設台灣常見市話區碼為前 2 碼 (例如: 02, 03, 04, 07)
            # 如果是手機或特殊格式，可依實際需求調整切片長度
            area_code = phone[:2] 
            unique_codes.add(area_code)
        return tuple(unique_codes)

    def get_cities(some_areacodes):
        """
        檢索指定元組(區域號碼)所代表的城市名稱並傳回。
        :param tuple some_areacodes: 內含區域號碼
        :return tuple: 區域號碼所代表的城市名稱 (不重複)
        """
        matched_cities = set()
        # 利用 zip 將區碼與城市一一綁定對照
        code_to_city_dict = dict(zip(all_areacodes, all_places))
        
        for code in some_areacodes:
            if code in code_to_city_dict:
                matched_cities.add(code_to_city_dict[code])
                
        return tuple(matched_cities)

    # --- 開始進行分析與輸出 ---
    total_friends = len(names)
    friend_codes = get_unique_area_codes()
    cities = get_cities(friend_codes)
    
    print("\n" + "="*30 + " 分析結果 " + "="*30)
    print(f"1) 檔案內共有幾位朋友：{total_friends} 位")
    print(f"2) 記錄中朋友所居住的城市（不重複）：{', '.join(cities)}")
    print("="*70)


# ==========================================
# 主程式執行
# ==========================================

def main():
    """
    指令：讀取檔案、分析內容、關閉檔案
    """
    try:
        # 1. 讀取朋友資料檔案
        with open('friends.txt', 'r', encoding='utf-8') as f_friends:
            names, phones = read_file(f_friends)
            
        # 2. 讀取區碼城市對照檔案
        with open('areacodes_cities.txt', 'r', encoding='utf-8') as f_codes:
            all_areacodes, all_places = read_file(f_codes)
            
        # 3. 清洗朋友的電話號碼
        clean_phones = sanitize(phones)
        
        # 4. 分析朋友資料
        analyze_friends(names, clean_phones, all_areacodes, all_places)
        
    except FileNotFoundError as e:
        print(f"❌ 錯誤：找不到指定的檔案。請確認 friends.txt 與 areacodes_cities.txt 是否存在。")
        print(f"詳細錯誤訊息: {e}")

if __name__ == "__main__":
    main()
