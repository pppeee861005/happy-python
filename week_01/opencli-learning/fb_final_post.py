import asyncio
from playwright.async_api import async_playwright

async def final_post():
    async with async_playwright() as p:
        # 啟動現有的 Chrome
        browser = await p.chromium.launch(
            executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
            headless=False
        )
        # 建立一個持久的 Context (存放在 temp_profile 中)
        context = await browser.new_context()
        page = await context.new_page()
        
        # 讀取 HN 內容
        with open("d:/gameplace/code第三學期初階/week_01/opencli-learning/fb_post.txt", "r", encoding="utf-8") as f:
            content = f.read()
            
        print("🌍 正在導航至 Facebook... 請確保已登入！")
        await page.goto("https://www.facebook.com/")
        
        print("💡 正在監控發文框... 請在視窗中完成登入並停留在首頁。")
        
        # 循環偵測，直到發文成功或視窗關閉
        for i in range(300): # 最多等待 600 秒 (300 * 2s)
            try:
                # 偵測首頁發文框
                trigger = page.get_by_text("在想什麼？").first
                if await trigger.is_visible():
                    print("✅ 偵測到發文框！開始自動填寫...")
                    await trigger.click()
                    await page.wait_for_timeout(3000)
                    
                    # 填入內容
                    textbox = page.locator('div[role="textbox"]').first
                    await textbox.fill(content)
                    await page.wait_for_timeout(2000)
                    
                    # 點擊發佈
                    print("🚀 正在點擊『發佈』按鈕...")
                    publish_btn = page.locator('div[aria-label="發佈"]').first
                    await publish_btn.click()
                    
                    print("🎉 發佈指令已送出！等待 15 秒確認上傳...")
                    await page.wait_for_timeout(15000)
                    break
            except Exception as e:
                pass
            
            await asyncio.sleep(2)
            if page.is_closed():
                print("❌ 瀏覽器視窗已被關閉。")
                break
        
        await browser.close()
        print("🏁 任務結束。")

if __name__ == "__main__":
    asyncio.run(final_post())
