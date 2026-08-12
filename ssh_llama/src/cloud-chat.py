"""Groq 雲端 LLM 互動聊天與用量紀錄範例。"""

from __future__ import annotations

import csv
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"
INPUT_USD_PER_MILLION = 0.59
OUTPUT_USD_PER_MILLION = 0.79
RESULTS_FILE = Path("results/cloud-chat-metrics.csv")
SYSTEM_MESSAGE = "你是一位精簡、友善的繁體中文 AI 助手。"


def estimate_cost_usd(prompt_tokens: int, completion_tokens: int) -> float:
    """依程式內設定的 Groq 單價估算本次費用。"""
    return (
        prompt_tokens * INPUT_USD_PER_MILLION
        + completion_tokens * OUTPUT_USD_PER_MILLION
    ) / 1_000_000


def save_metrics(
    elapsed_seconds: float,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
    estimated_cost_usd: float,
) -> None:
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    is_new_file = not RESULTS_FILE.exists()
    with RESULTS_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(
                [
                    "timestamp_utc",
                    "model",
                    "elapsed_seconds",
                    "prompt_tokens",
                    "completion_tokens",
                    "total_tokens",
                    "estimated_cost_usd",
                ]
            )
        writer.writerow(
            [
                datetime.now(timezone.utc).isoformat(),
                MODEL,
                f"{elapsed_seconds:.3f}",
                prompt_tokens,
                completion_tokens,
                total_tokens,
                f"{estimated_cost_usd:.8f}",
            ]
        )


def request_chat(api_key: str, messages: list[dict[str, str]]) -> dict:
    body = json.dumps(
        {"model": MODEL, "messages": messages, "temperature": 0.7},
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            # 避免 Cloudflare 將 urllib 的預設請求特徵判定為不允許的客戶端。
            "User-Agent": "ssh-llama-cloud-chat/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def main() -> None:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise SystemExit("找不到 GROQ_API_KEY，請先設定環境變數。")

    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
    print(f"已連線模型：{MODEL}（輸入 exit 結束）")

    while True:
        user_text = input("\n你：").strip()
        if user_text.lower() in {"exit", "quit", "退出"}:
            break
        if not user_text:
            continue

        messages.append({"role": "user", "content": user_text})
        started_at = time.perf_counter()
        try:
            result = request_chat(api_key, messages)
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            messages.pop()
            print(f"API 錯誤 {error.code}：{detail}")
            continue
        except urllib.error.URLError as error:
            messages.pop()
            print(f"網路錯誤：{error.reason}")
            continue

        elapsed = time.perf_counter() - started_at
        assistant_text = result["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": assistant_text})

        usage = result.get("usage", {})
        prompt_tokens = int(usage.get("prompt_tokens", 0))
        completion_tokens = int(usage.get("completion_tokens", 0))
        total_tokens = int(usage.get("total_tokens", prompt_tokens + completion_tokens))
        cost = estimate_cost_usd(prompt_tokens, completion_tokens)
        save_metrics(elapsed, prompt_tokens, completion_tokens, total_tokens, cost)

        print(f"\nAI：{assistant_text}")
        print(
            f"\n[指標] {elapsed:.2f} 秒 | "
            f"token {prompt_tokens} 輸入 + {completion_tokens} 輸出 "
            f"= {total_tokens} | 估計 US${cost:.8f}"
        )


if __name__ == "__main__":
    main()
