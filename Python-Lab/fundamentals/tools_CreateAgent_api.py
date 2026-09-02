from langchain.agents import create_agent
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


def call_tools(model_name: str, query: HumanMessage):
    model = create_agent(
        model=model_name,
        tools=[get_weather],
        system_prompt=SystemMessage(
            content="You are an experience and helpful assistant."
        ),
    )
    response = model.invoke({"messages": [query]})
    final_message = response["messages"][-1]
    logfire.info("Final Response Content", content=final_message.content)


if __name__ == "__main__":
    with logfire.span("tools_Init_Chat_Model"):
        call_tools(
            "groq:qwen/qwen3.6-27b", HumanMessage(content="Whats weather in Bengaluru")
        )
