import requests
from bs4 import BeautifulSoup
import pandas as pd
from deep_translator import GoogleTranslator

# 1. 目標網站網址
url = "https://quotes.toscrape.com/"

# 2. 向網站發送請求
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_html = soup.find_all('div', class_='quote')
    
    data_list = []
    
    # 初始化翻譯工具
    translator = GoogleTranslator(source='en', target='zh-TW')
    
    print("正在抓取、翻譯並分類數據，請稍候...")
    
    for q in quotes_html:
        text_en = q.find('span', class_='text').text       # 英文名言
        author = q.find('small', class_='author').text     # 作者
        
        # 進行翻譯
        try:
            text_zh = translator.translate(text_en)
        except Exception:
            text_zh = "翻譯失敗"
        
        data_list.append({
            '英文名言': text_en,
            '中文翻譯': text_zh,
            '作者': author
        })
    
    # 3. 轉換成總表格
    df = pd.DataFrame(data_list)
    
    # 4. 【分開儲存】
    # 建立純英文表格（只拿 英文名言 和 作者）
    df_en = df[['英文名言', '作者']]
    df_en.to_csv('quotes_english.csv', index=False, encoding='utf-8-sig')
    
    # 建立純中文表格（只拿 中文翻譯 和 作者）
    df_zh = df[['中文翻譯', '作者']]
    df_zh.to_csv('quotes_chinese.csv', index=False, encoding='utf-8-sig')
    
    print("\n--- 儲存成功！ ---")
    print("1. 英文版已儲存至: quotes_english.csv")
    print("2. 中文版已儲存至: quotes_chinese.csv")

else:
    print("無法連線到網站")