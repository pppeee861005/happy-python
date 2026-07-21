**Groq 做的不是 GPU，也不是 Google 的 TPU，而是自家設計的 AI 加速晶片：LPU（Language Processing Unit）。** ([Groq][1])

可以這樣理解：

| 晶片      | 主要用途                    | 代表廠商       |
| ------- | ----------------------- | ---------- |
| GPU     | 圖形運算、AI 訓練與推論，通用性高      | NVIDIA、AMD |
| TPU     | Tensor 運算，主要用於 AI 訓練與推論 | Google     |
| **LPU** | 專門追求大型語言模型的高速、低延遲推論     | **Groq**   |

### Groq LPU 的特色

Groq LPU 主要用來執行已經訓練好的模型，也就是 **AI inference（推論）**，例如讓 Llama、Qwen 等模型快速產生文字。它的目標不是取代 GPU 做所有工作，而是把「一個 token 接一個 token 產生」這件事做到非常快而且延遲穩定。([Groq][2])

它與 GPU 最大的不同是：

* GPU 有大量平行核心，工作排程較複雜。
* Groq LPU 採用類似「固定流水線、裝配線」的資料流架構。
* 編譯器預先決定資料何時移動、何時運算，因此執行時間較容易預測。
* 使用大量晶片內部 **SRAM**，減少資料在處理器與外部記憶體之間搬運。([Groq][3])

一句話比喻：

> **GPU 像一間可以生產很多產品的萬能工廠；Groq LPU 像專門生產 AI token 的高速自動化流水線。**

所以最準確的說法是：

> **Groq 是 AI inference 晶片公司，核心晶片叫 LPU；概念上與 TPU 同屬專用 AI accelerator，但架構並不是 TPU。**

[1]: https://groq.com/lpu-architecture?utm_source=chatgpt.com "LPU | Groq is fast, low cost inference."
[2]: https://groq.com/?s=Nvidia+Groq+LPUs+real-world+performance&utm_source=chatgpt.com "Groq is fast, low cost inference."
[3]: https://groq.com/blog/the-groq-lpu-explained?utm_source=chatgpt.com "What is a Language Processing Unit? | Groq is fast, low cost inference."

