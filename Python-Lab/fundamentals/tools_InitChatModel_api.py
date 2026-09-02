from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from common.logger_wrapper import configure_logfire
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

logfire = configure_logfire()


@tool
def get_weather(city: str) -> str:
    """
    get_weather Fetch the weather of give city

    Args:
        get_weather (str): Name of the city

    Returns:
        undefined: Returns the Weather

    Raises:
        ValueError: None
    """
    return f"Its hot and humit in {city}"


def call_tools(model_name: str, query: str):
    conversation = [
        SystemMessage(content="You are an experience and helpful assistant."),
        HumanMessage(content=query),
    ]
    model = init_chat_model(model=model_name)
    model_with_tools = model.bind_tools([get_weather])
    response = model_with_tools.invoke(conversation)
    logfire.info("Model with tools", content=response)

    for tool in response.tool_calls:
        logfire.info(f"Tool call {tool['name']}", content=tool)
        if "get_weather" == tool["name"]:
            tool_response = get_weather.invoke(tool["args"])
            conversation.append(
                ToolMessage(content=tool_response, tool_call_id=tool["id"])
            )

    final_response = model_with_tools.invoke(conversation)
    logfire.info("Final Response", content=final_response)
    logfire.info("Final Response Content", content=final_response.content)


if __name__ == "__main__":
    with logfire.span("tools_Init_Chat_Model"):
        call_tools("groq:qwen/qwen3.6-27b", "Whats weather in Bengaluru")
