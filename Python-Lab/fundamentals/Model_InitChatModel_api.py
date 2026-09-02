from langchain.chat_models import init_chat_model
from common.logger_wrapper import configure_logfire

logfire = configure_logfire()


def get_chat_model(model: str, model_provider: str):
    model = init_chat_model(model=model, model_provider=model_provider)
    response = model.invoke("What is AI")
    print(response.content)


if __name__ == "__main__":
    get_chat_model(model="qwen/qwen3.6-27b", model_provider="groq")
