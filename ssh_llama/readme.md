# 地端 AI Agent 學習專案

本專案用來學習如何在 Vultr 雲端主機上部署 Docker、Ollama 與大型語言模型，逐步建立可供 AI Agent 使用的實驗環境。

由於在本機下載模型的速度較慢，現階段先使用 Vultr 練習部署與操作；熟悉流程後，再將環境移回本機，研究完全地端化的 AI Agent。

## 專案目標

### 現階段

1. 在 Vultr 的 Ubuntu 22.04 主機上安裝 Docker。
2. 使用 Docker 安裝並操作 Ollama。
3. 下載 Gemma 等語言模型，測試基本聊天功能。
4. 熟悉容器、模型下載、服務啟動及日誌查看。

### 長期目標

- 在本機執行 Hermes Agent。
- 使用約 27B 規模的 Qwen 地端模型驅動 Agent（實際版本待確認）。
- 研究模型、工具與 Agent 之間的整合方式。
- 逐步測試更大型的模型及不同部署方案。

## 實驗環境

| 項目 | 規格 |
| --- | --- |
| 雲端平台 | Vultr |
| 作業系統 | Ubuntu 22.04 x64 |
| CPU | 2 vCPU |
| RAM | 8 GB |
| 儲存空間 | 10 GB（Hermes Storage） |
| Volume ID | `56c79f0a-7b1c-4b65-8dc1-12cf0e5f96ce` |
| Bandwidth | 目前顯示 0 GB |

## 預計學習順序

```text
Ubuntu 基礎操作
  → Docker 安裝與管理
  → Ollama 容器部署
  → 模型下載與聊天測試
  → Hermes Agent 整合
  → 本機地端化部署
```

## 專案狀態

目前正在進行 Docker 的安裝與基礎操作練習。

最後更新：2026-07-31


你的最佳選擇

若 Vultr 選項允許自訂，我建議：

1× L40S 48GB + 8 vCPU + 32或64GB RAM

若只能選固定套餐，選擇順序是：

先確定有 L40S 48GB，再挑最便宜且至少 4 vCPU／32GB RAM 的方案。

你每天只練習一小時，不需要追求昂貴的高 CPU 套餐。真正需要注意的是：建立 GPU 主機與下載 24GB 模型也會占用租用時間，因此最好把環境做成 Docker image，或保留一顆 Block Storage 存模型；不過 Block Storage 在主機刪除後仍會持續計費。