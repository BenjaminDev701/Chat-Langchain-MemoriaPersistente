import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


get_llm = init_chat_model(
    model="openai:gpt-6-luna",
    temperature=0.7
)
