import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

load_dotenv()


MODELS = {
    "CHATGPT_3_5": "gpt-3.5-turbo",
    "GPT_4O_MINI": "gpt-4o-mini",
}

class OpenAIConnector:
    def __init__(self, model_type: str):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")

        if not model_type:
            raise ValueError("model_type is required")

        self._model_type = model_type
        self._client = OpenAI(api_key=api_key)

    def llm_response(self, prompt_input: str) -> str:
        prompt_messages = self.build_message(prompt_input)

        response = self._client.chat.completions.create(
            model=self._model_type,
            messages=prompt_messages,
            temperature=0,
        )

        return response.choices[0].message.content or ""

    @staticmethod
    def build_message(prompt_input: str) -> list[ChatCompletionUserMessageParam]:
        messages: list[ChatCompletionUserMessageParam] = [
            {
                "role": "user",
                "content": prompt_input,
            }
        ]
        return messages
