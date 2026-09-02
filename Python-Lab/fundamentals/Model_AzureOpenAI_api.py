from dotenv import load_dotenv
from common.load_env import load_env_variables
from common.logger_wrapper import configure_logfire

from langchain_core.language_models import BaseChatModel


import os

logfire = configure_logfire()


def init_azure_openai_model() -> BaseChatModel:
    global logfire
    logfire.instrument_openai()

    from langchain_openai import AzureChatOpenAI

    print(os.getenv("GROQ_API_KEY"))
    model = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    )
    return model


def inference_azure_openai(model: BaseChatModel, query: str):

    response = model.invoke(query)
    return response


if __name__ == "__main__":
    with logfire.span("AzureOpenAI"):
        model = init_azure_openai_model()
        response = inference_azure_openai(model=model, query="Where is India?")
        print(response.pretty_print())
