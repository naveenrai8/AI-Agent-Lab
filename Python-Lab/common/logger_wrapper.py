import logfire
from .load_env import load_env_variables


def configure_logfire():
    load_env_variables()
    logfire.configure()
    return logfire
