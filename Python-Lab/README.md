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

## 🔭 Observability

Traces and LLM call logs are sent to [Pydantic Logfire](https://pydantic.dev/logfire) — a single `logfire.configure()` + `logfire.instrument_pydantic_ai()`/auto-instrumentation call captures every model invocation (prompts, tokens, latency, errors) with no changes to the model scripts themselves.

```bash
uv run logfire auth        # one-time: authenticate this machine
uv run logfire projects use <project-name>
```

```python
import logfire

logfire.configure()
logfire.instrument_openai()   # captures Azure OpenAI calls (langchain-openai wraps the openai SDK)
logfire.instrument_httpx()    # captures Groq calls (groq SDK has no dedicated instrumentor; httpx is its transport)
```

View traces at [logfire.pydantic.dev](https://logfire.pydantic.dev/).

## 🔧 Tools

Three ways to give a model access to tools, from most to least manual — see
[`fundamentals/`](fundamentals):

| Approach | File | Tool-call loop |
|---|---|---|
| `ChatGroq` (provider class) + `bind_tools()` | `fundamentals/tools_ChatModel_api.py` | Manual |
| `init_chat_model()` + `bind_tools()` | `fundamentals/tools_InitChatModel_api.py` | Manual |
| `create_agent(tools=[...])` | `fundamentals/tools_CreateAgent_api.py` | Automatic |

See [`TOOL_README.md`](TOOL_README.md)

## 📐 Structured Output

Two ways to constrain a `create_agent` response to a schema instead of free-form text — see
[`fundamentals/`](fundamentals):

| Approach | File | Schema style |
|---|---|---|
| `pydantic.BaseModel` + `Field(description=...)` | `fundamentals/structured_output_pydantic.py` | Class with typed fields, descriptions via `Field` |
| `typing_extensions.TypedDict` + `Annotated` | `fundamentals/structured_output_typedict.py` | Dict-shaped type, descriptions via `Annotated[type, ..., "desc"]` |

Both pass the schema as `response_format=UserInfo` to `create_agent(...)`; the agent's `.invoke()` result comes back matching that shape instead of a plain message string.

## ⚡ Quickstart

```bash
uv sync                        # install deps + this project (editable)
uv run Models/Groq_Model.py    # run any model script directly
```

Credentials are loaded via [`common/load_env.py`](common/load_env.py) from `[location of your choice. e.g. ~]/.env`.

## 🛠️ Requirements

- Python `>=3.13`
- `uv` for dependency management (`uv.lock` is checked in)


## References
1. [Langchain Structured output](https://docs.langchain.com/oss/python/langchain/structured-output)