import os

apikey = os.getenv("OPENAI_API_KEY")
if not apikey:
    raise RuntimeError("Set OPENAI_API_KEY in your environment before running the OpenAI example.")
