from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.src.inference.openai_connector import OpenAIConnector, MODELS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str
    model: str = "GPT_4O_MINI"


class PromptResponse(BaseModel):
    response: str


@app.post("/api/chat", response_model=PromptResponse)
def chat(request: PromptRequest):
    connector = OpenAIConnector(MODELS[request.model])
    response = connector.llm_response(request.prompt)

    return PromptResponse(response=response)