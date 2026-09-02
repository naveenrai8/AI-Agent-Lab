from fundamentals.Model_Groq_api import init_groq_provider
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
    model = init_groq_provider(model_name=model_name)
    model_with_tools = model.bind_tools([get_weather])
    response = model_with_tools.invoke(conversation)
    conversation.append(response)
    logfire.info("Model Response", content=response)

    for tool in response.tool_calls:
        logfire.info("Tool_call", content=tool)
        if "get_weather" == tool["name"]:
            tool_response = get_weather.invoke(tool["args"])
            conversation.append(
                ToolMessage(content=tool_response, tool_call_id=tool["id"])
            )

    final_response = model.invoke(conversation)
    logfire.info("Final Response", content=final_response)


if __name__ == "__main__":
    with logfire.span("chat_model_tools"):
        call_tools("qwen/qwen3.6-27b", "Whats weather in Bengaluru")
