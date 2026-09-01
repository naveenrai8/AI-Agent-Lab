def load_env_variables():
    from pathlib import Path

    from dotenv import load_dotenv

    path = Path.home() / ".self" / ".env"
    is_loaded = load_dotenv(dotenv_path=path)
    print(f"Env variables loaded: {is_loaded}")


if __name__ == "__main__":
    load_env_variables()
