# 🤖 AI-Agent-Lab

A personal, hands-on playground for building and testing LLM-powered chat models and agents with [LangChain](https://python.langchain.com/), managed with [`uv`](https://docs.astral.sh/uv/).

## 📁 Structure

```
AI-Agent-Lab/
├── Models/          # One script per LLM provider — the entry point for each model
│   ├── Groq_Model.py
│   └── AzureOpenAI_Model.py
├── common/          # Shared utilities (env loading, credential config)
├── main.py
└── pyproject.toml
```

## 🧠 Models

Each file in [`Models/`](Models) wires up a single provider through LangChain's chat model interface and runs a quick inference call when executed directly.

| Provider | File | Chat class |
|---|---|---|
| 🟢 Groq | `Models/Groq_Model.py` | `ChatGroq` |
| 🔷 Azure OpenAI | `Models/AzureOpenAI_Model.py` | `AzureChatOpenAI` |

Adding a new provider? Drop a new `<Provider>_Model.py` file in `Models/`, following the same shape: load env vars, construct the chat model, `model.invoke(...)`.

## ⚡ Quickstart

```bash
uv sync                        # install deps + this project (editable)
uv run Models/Groq_Model.py    # run any model script directly
```

Credentials are loaded via [`common/load_env.py`](common/load_env.py) from `[location of your choice. e.g. ~]/.env`.

## 🛠️ Requirements

- Python `>=3.13`
- `uv` for dependency management (`uv.lock` is checked in)
