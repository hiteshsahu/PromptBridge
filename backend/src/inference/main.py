from openai import RateLimitError

from backend.src.inference.openai_connector import OpenAIConnector, MODELS

prompt = """
Classify the following review 
as having either a positive or negative sentiment:

The banana pudding was really tasty!
"""

open_ai_connector = OpenAIConnector(MODELS["GPT_4O_MINI"])

try:
    result = open_ai_connector.llm_response(prompt)
    print(result)
except RateLimitError as error:
    print(f"⚠️ ERROR:: OpenAI API rate limit exceeded: {error}")


