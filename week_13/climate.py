#########################################################################
# Python x ChatGPT
# urllib, requests - URL/HTTP 處理程式庫
# [作業]
# 倫敦希斯洛機場氣象資料
# 問題：
#   撰寫程式透過 HTTP 下載並解析檔案
# 輸入：網址(URL)如下
#       ("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/"
#        "stationdata/heathrowdata.txt")
# 輸出：每個年度的平均降雨量、以及每年的最高和最低溫度。
# **提示：
#   1)大致檔案內容檢附如下，以幫助思考資料擷取方式
#   2)網路取得的文字內容，可以使用 str.split() 方法
#     取得所需欄位資料，並進行統計
# Heathrow (London Airport)
# Location 507800E 176700N, Lat 51.479 Lon -0.449, 25m amsl
# Estimated data is marked with a * after the value.
# Missing data (more than 2 days missing in month) is marked...
# Sunshine data taken from an automatic Kipp & Zonen sensor...
#    yyyy  mm   tmax    tmin      af    rain     sun
#               degC    degC    days      mm   hours
#    1948   1    8.9     3.3    ---     85.0    ---
#    1948   2    7.9     2.2    ---     26.0    ---
#    1948   3   14.2     3.8    ---     14.0    ---
#    1948   4   15.4     5.1    ---     35.0    ---
#    1948   5   18.1     6.9    ---     57.0    ---
#    1950   1   10.5     2.1    ---     48.0    ---
#    1950   2   17.5     3.8    ---     50.5    ---
###########################################################################
import requests
from collections import defaultdict
url = ("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/"
       "stationdata/heathrowdata.txt")
# 1. 發送 HTTP 請求取得資料
response = requests.get(url)
# 確保正確解碼文字
response.encoding = 'utf-8'
# 將文字按行切割
lines = response.text.split('\n')
# 用來儲存年度資料的字典
# 結構：{ 年份: {'tmax': [列表], 'tmin': [列表], 'rain': [列表]} }
weather_data = defaultdict(lambda: {'tmax': [], 'tmin': [], 'rain': []})
# 2. 解析每一行資料
for line in lines:
    # 使用 split() 切割，會自動忽略連續的空格
    parts = line.split()
    # 根據欄位特徵過濾掉標頭檔
    # 資料列的第一個元素必須是年份（數字），且欄位數量至少要有 6 個 (yyyy, mm, tmax, tmin, af, rain)
    if len(parts) >= 6 and parts[0].isdigit():
        try:
            year = int(parts[0])
            # 清理資料：移除可能存在的 '*' 號
            tmax_str = parts[2].replace('*', '')
            tmin_str = parts[3].replace('*', '')
            rain_str = parts[5].replace('*', '')
            # 檢查是否有缺失值 '---'，若無則轉換為浮點數
            if tmax_str != '---':
                weather_data[year]['tmax'].append(float(tmax_str))
            if tmin_str != '---':
                weather_data[year]['tmin'].append(float(tmin_str))
            if rain_str != '---':
                weather_data[year]['rain'].append(float(rain_str))
        except ValueError:
            # 預防萬一有其他無法轉換的髒資料，直接跳過該行
            continue
# --- 輸出結果面板 ---
print(f"{'年份':<6}{'平均降雨量 (mm)':<12}{'最高溫度 (°C)':<12}{'最低溫度 (°C)':<12}")
print("-" * 50)
# 3. 計算並統計每個年度的數據
for year in sorted(weather_data.keys()):
    data = weather_data[year]
    # 計算平均降雨量（如果該年有降雨量資料）
    if data['rain']:
        avg_rain = sum(data['rain']) / len(data['rain'])
        avg_rain_str = f"{avg_rain:.2f}"
    else:
        avg_rain_str = "無資料"
    # 找出最高溫與最低溫
    max_temp = max(data['tmax']) if data['tmax'] else "無資料"
    min_temp = min(data['tmin']) if data['tmin'] else "無資料"
    # 格式化輸出
    print(f"{year:<8}{avg_rain_str:<16}{max_temp:<14}{min_temp:<12}")

