from unittest.mock import MagicMock, patch

import pytest

from backend.src.inference.openai_connector import OpenAIConnector, MODELS


def test_should_raise_error_when_api_key_is_missing(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(ValueError, match="OPENAI_API_KEY environment variable not set"):
        OpenAIConnector(MODELS["GPT_4O_MINI"])


def test_should_raise_error_when_model_type_is_missing(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-api-key")

    with pytest.raises(ValueError, match="model_type is required"):
        OpenAIConnector(None)


@patch("src.openai_connector.OpenAI")
def test_should_return_llm_response(mock_openai_client, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-api-key")

    mock_client_instance = MagicMock()
    mock_openai_client.return_value = mock_client_instance

    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Positive"

    mock_client_instance.chat.completions.create.return_value = mock_response

    connector = OpenAIConnector(MODELS["GPT_4O_MINI"])

    result = connector.llm_response("The banana pudding was really tasty!")

    assert result == "Positive"

    mock_openai_client.assert_called_once_with(api_key="fake-api-key")

    mock_client_instance.chat.completions.create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "The banana pudding was really tasty!",
            }
        ],
        temperature=0,
    )