# 🧪 AI-Agent-Lab

A personal, hands-on lab for GenAI experiments — LLM chat models, agents, and the
infrastructure around them (env/config handling, observability). Organized as one
folder per language, so the same GenAI ideas can be explored across ecosystems.

## 📁 Structure

```
AI-Agent-Lab/
├── Python-Lab/   # LangChain-based chat models & agents, uv-managed — see below
└── Go-Lab/       # (planned) Go GenAI experiments
```

## 🐍 Python-Lab

The active lab today. LLM chat models (Groq, Azure OpenAI) wired up through
[LangChain](https://python.langchain.com/), managed with [`uv`](https://docs.astral.sh/uv/),
with request/response tracing shipped to [Pydantic Logfire](https://pydantic.dev/logfire).

→ Full details, structure, and quickstart: [`Python-Lab/README.md`](Python-Lab/README.md)

## 🐹 Go-Lab

Not started yet — reserved for the same class of GenAI experiments (chat models, agents)
written in Go, once that work begins.

## 🛠️ Requirements

- `uv` for the Python lab (`Python-Lab/uv.lock` is checked in)
- Go toolchain — once `Go-Lab/` exists
