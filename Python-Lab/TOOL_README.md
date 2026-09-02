# 🔧 Tools

Three ways to give a model access to tools, from most to least manual — see
[`fundamentals/`](fundamentals):

| Approach | File | Tool-call loop |
|---|---|---|
| `ChatGroq` (provider class) + `bind_tools()` | `fundamentals/tools_ChatModel_api.py` | Manual |
| `init_chat_model()` + `bind_tools()` | `fundamentals/tools_InitChatModel_api.py` | Manual |
| `create_agent(tools=[...])` | `fundamentals/tools_CreateAgent_api.py` | Automatic |

**`bind_tools()`** (first two rows) attaches tool schemas to the model but doesn't
execute anything — you invoke, inspect `response.tool_calls`, run the matching tool
yourself, append a `ToolMessage`, and invoke again to get the final answer:

```python
model_with_tools = model.bind_tools([get_weather])
response = model_with_tools.invoke(conversation)

for tool in response.tool_calls:
    if tool["name"] == "get_weather":
        result = get_weather.invoke(tool["args"])
        conversation.append(ToolMessage(content=result, tool_call_id=tool["id"]))

final_response = model_with_tools.invoke(conversation)
```

**`create_agent(tools=[...])`** builds that same loop as a LangGraph graph — passing
`tools` as a constructor argument is enough; the graph calls the model, executes any
requested tools, and feeds results back until there's a final answer, in one `invoke()`:

```python
agent = create_agent(model=model_name, tools=[get_weather], system_prompt=...)
response = agent.invoke({"messages": [HumanMessage(content=query)]})
final_message = response["messages"][-1]
```

Same tool, same model, far less code — `create_agent` is the better default for anything
beyond a single hand-rolled tool-call round trip. Note its `invoke()` input/output shape
differs from a plain chat model's (`{"messages": [...]}` in, `response["messages"]` out,
not a bare message) — see [`pocs/Python-poc/03-langgraph-agent-input-schema`](../../../pocs/Python-poc/03-langgraph-agent-input-schema/README.md).
