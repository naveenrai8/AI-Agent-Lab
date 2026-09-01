from dotenv import load_dotenv
from common.load_env import load_env_variables

import os

load_env_variables()


def inference_using_groq_provider(model_name: str):

    from langchain_groq import ChatGroq

    print(os.getenv("GROQ_API_KEY"))
    model = ChatGroq(model=model_name, api_key=os.getenv("GROQ_API_KEY"))
    print(model.model_dump_json)

    response = model.invoke("What is AI. Explain in 2 statements")
    print(response.pretty_print())


if __name__ == "__main__":
    inference_using_groq_provider("qwen/qwen3.6-27b")
