from common.logger_wrapper import configure_logfire
from langchain.agents import create_agent
from typing_extensions import TypedDict, Annotated
from langchain_core.messages import HumanMessage

logfire = configure_logfire()
logfire.instrument_httpx()


class UserInfo(TypedDict):
    """User information for a person"""

    name: Annotated[
        str, ..., "Name of the person which is full name including the sername"
    ]
    first_name: Annotated[
        str,
        ...,
        "First name of the person. When person's name has more than two words then all the words but the last word are part of first name",
    ]
    last_name: Annotated[
        str,
        ...,
        "Last name of the person. When person's name has more than two words than last word is the last name",
    ]
    email: Annotated[str, ..., "Email id of the person"]


def structured_output_typedict(query: str):
    agent = create_agent(
        model="groq:qwen/qwen3.8-27b",
        system_prompt="You are helpful assistance. Extract the User information from the user query",
        response_format=UserInfo,
    )

    user_info = agent.invoke({"messages": [HumanMessage(content=query)]})
    logfire.info("User Info", content=user_info)


if __name__ == "__main__":
    with logfire.span("Structured output using Pydantic"):
        structured_output_typedict(
            "Ram is sending email from his email id which is ram@abc.com"
        )

    with logfire.span("Structured output using Pydantic"):
        structured_output_typedict(
            "Ram Kumar is sending email from his email id which is ram_kumar@abc.com"
        )

    with logfire.span("Structured output using Pydantic"):
        structured_output_typedict(
            "Ram Kumar Sharma is sending email from his email id which is ram_kumar_sharma@abc.com"
        )
