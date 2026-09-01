from dotenv import load_dotenv
from common.load_env import load_env_variables

import os

load_env_variables()


def inference_using_azure_openai():

    from langchain_openai import AzureChatOpenAI

    print(os.getenv("GROQ_API_KEY"))
    model = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    )
    print(model.model_dump_json)

    response = model.invoke("What is AI. Explain in 2 statements")
    print(response.pretty_print())


if __name__ == "__main__":
    inference_using_azure_openai()
