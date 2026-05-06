import os

import pytest
from openai import RateLimitError

from backend.src.inference.openai_connector import OpenAIConnector, MODELS


@pytest.mark.integration
def test_should_call_openai_and_return_sentiment():
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY is not set")

    connector = OpenAIConnector(MODELS["CHATGPT_3_5"])

    prompt = """
    Classify the following review as having either a positive or negative sentiment.

    Return only one word: Positive or Negative.

    Review:
    The banana pudding was really tasty!
    """

    try:
        result = connector.llm_response(prompt)
    except RateLimitError as error:
        print(f"Skipping integration test:: OpenAI API rate limit exceeded: {error}")
        pytest.skip(f"Skipping integration test because OpenAI quota/rate limit failed: {error}")

    assert "positive" in result.strip().lower()