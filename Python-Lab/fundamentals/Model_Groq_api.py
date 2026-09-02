from dotenv import load_dotenv
from common.load_env import load_env_variables
from langchain_core.language_models import BaseChatModel

from common.logger_wrapper import configure_logfire

import os

logfire = configure_logfire()
logfire.instrument_httpx()


def init_groq_provider(model_name: str) -> BaseChatModel:

    from langchain_groq import ChatGroq

    model = ChatGroq(model=model_name, api_key=os.getenv("GROQ_API_KEY"))
    return model


def inference_groq_model(model: BaseChatModel) -> str:

    response = model.invoke("What is AI. Explain in 2 statements")
    logfire.info(
        "Groq inference response",
        content=response.content,
        # usage=response.usage_metadata,
    )
    return response


if __name__ == "__main__":
    model = init_groq_provider("qwen/qwen3.8-27b")
    response = inference_groq_model(model=model)
    print(response)
