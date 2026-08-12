skills/
├── docker/
├── ollama/
├── vultr/
├── github/
├── security/
├── rce/
└── computer_use/

Skill（大腦）
│
├── 決定流程
├── 什麼時候執行
├── 哪些步驟
├── 安全規則
└── 呼叫工具
        │
        ▼
Python Script（手腳）
│
├── install_docker.py
├── deploy_ollama.py
├── pull_model.py
├── health_check.py
└── cleanup.py

我對你的專案還有一個建議

依照你目前在做的：

Vultr
Docker
Ollama
OpenClaw
Hermes Agent
Qwen 3.6 27B

我會建議不要只做一個 deploy.py。

而是建立一個可重複使用的 Skill Library，例如：

