可以。最可靠的方法是：把 10 個 Agent 加入同一個 Channel，然後在同一則 Message 中逐一 @提及 全部 Agent。

  Buzz 的 Agent 各自擁有 Channel 成員資格；只有已加入該 Channel 的 Agent 才能讀寫內容。官方架構也說明，@mention 事件會被送到 Agent
  處理。Buzz README (https://github.com/block/buzz/blob/main/README.md)、Buzz Architecture
  (https://github.com/block/buzz/blob/main/ARCHITECTURE.md)

  ### 實際操作

  1. 進入你的 buzz_learning Channel。
  2. 打開 Channel 成員名單。
  3. 確認 10 個 Agent 全部都已加入。
  4. 發布一則新的 Message，逐一提及它們：

  @fizz @agent2 @agent3 @agent4 @agent5
  @agent6 @agent7 @agent8 @agent9 @agent10

  請每位 Agent 分別回答：

  「什麼時候應該使用 Channel，什麼時候應該使用 Thread？」

  回答規則：
  1. 每位 Agent 都要獨立回答。
  2. 不要替其他 Agent 回答。
  3. 請將答案回覆在這則訊息的 Thread。
  4. 回答開頭先寫自己的名字。
  5. 看過其他答案後，仍要提出自己的判斷。

  輸入 @ 後，請從 Buzz 顯示的名單中點選 Agent，確保它真的成為有效提及，而不是只輸入普通文字。

  ### 為什麼要放在同一個 Thread？

  這樣結構會是：

  Channel：buzz_learning
  └── Message：同一個問題
      └── Thread
          ├── Fizz 的回答
          ├── Agent 2 的回答
          ├── Agent 3 的回答
          └── 其餘 Agent 的回答

  所有答案集中在同一處，方便比較，也不會讓 Channel 出現十條散落的討論。

  ### 如果只有部分 Agent 回答

  依序檢查：

  - 沒回答的 Agent 是否已加入 Channel。
  - 是否真的透過 @ 選單提及，而非只打名字。
  - Agent 是否在線或正在執行其他任務。
  - 等 Agent 回覆完再追問，避免同一個 Agent 的工作佇列塞入太多訊息。
  - 在原本的 Thread 裡再次寫：

  @agent4 @agent7

  你們尚未回答原始問題，請各自補充回答。

  不要另外開新 Message，否則同一問題的紀錄會被拆散。

  ### 一個重要區別

  如果你只是把問題貼到 Channel，但沒有提及任何 Agent，它們不一定會回答。你之前對 Fizz 的實驗已經證明這一點：加入 Channel 代表它有資格參
  與，@fizz 才是明確請它處理這則訊息。

  你現在可以先用 3 個 Agent 測試一次；成功後再擴大到 10 個，會比較容易發現哪一個環節沒有設定好。