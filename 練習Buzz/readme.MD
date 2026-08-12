# Buzz AI 操作學習專案

## 核心目標

每天學習一小時，逐步成為「操作型」Buzz AI 達人。

本階段不 clone Buzz 原始碼、不研究底層架構，也不建立開發環境。學習重點是掌握 Buzz 的精髓：讓人類與具有獨立身分、權限及操作紀錄的 AI Agent，在同一個工作空間裡有效、安全且可追溯地協作。

## 學習原則

- 少講抽象架構，多做真正的操作、觀察與判斷。
- 每天固定投入 1 小時：10 分鐘複習、40 分鐘操作、10 分鐘記錄。
- 每堂課都要有可觀察的結果與明確的完成條件。
- 優先練習 Community、Channel、Thread、Agent、任務交付、權限、紀錄與故障判斷。
- 使用測試資料，不公開私鑰、API Key、Token、`.env` 或個人敏感資料。

## 目前進度

- 已認識 Buzz 的用途，以及 Community、Channel、Thread 的關係。
- 已安裝 Buzz Windows 桌面版。
- 已建立 Community：`ai-council-lab`。
- 已建立由自己管理的 Fizz Agent。
- 已將 Fizz 切換至本機 Codex runtime，並成功運行。
- 已初步認識 Agent 狀態、Reaction、Harness Log、身分與 Relay。

詳細紀錄請見[第二天學習紀錄.md](./第二天學習紀錄.md)。

## 主要教材

- [操作型 Buzz AI 達人學習計劃](./我要成為操作buzz%20ai的達人的學習計劃.md)
- [備用的進階學習計劃](./備用的進階學習計劃.md)：日後想研究 clone、架構與開發環境時才使用。
- [Buzz 官方專案](https://github.com/block/buzz)

## 現階段不做的事情

- 不 clone Buzz 原始碼。
- 不閱讀或分析 Buzz 原始碼架構。
- 不安裝 Rust、Node.js、pnpm、Hermit、`just` 等開發工具鏈。
- 不建立 `requirements.txt`；Buzz 並不是以 Python 為主的專案。
- 不自行架設正式 Relay 或資料庫。

## 達人的定義

操作型 Buzz AI 達人不只是會聊天，而是能設計工作空間、建立合適的 Agent、下達可驗收的任務、控制資訊與權限、判讀執行狀態、從紀錄找出問題，並讓多個 Agent 在人的決策與監督下可靠協作。
