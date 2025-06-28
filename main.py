from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from llm_client import query_ollama

app = FastAPI()


class CleanTextRequest(BaseModel):
    text: str

class ChatRequest(BaseModel):
    history: List[str]  # List of strings representing conversation history


@app.post("/clean_text")
def clean_text(request: CleanTextRequest):
    prompt = (
        "Clean the following text from noise such as headers, footers, and page numbers:\n\n"
        f"{request.text}"
    )
    cleaned = query_ollama(prompt)
    return {"cleaned_text": cleaned}


@app.post("/chat")
def chat(request: ChatRequest):
    conversation = "\n".join(request.history)
    prompt = (
        "You are a skeptical buyer. Engage in a conversation with the seller, but do NOT accept any offer unless you are truly convinced. "
        "Ask relevant questions and don’t agree too easily. Continue this conversation:\n\n"
        f"{conversation}"
    )
    response = query_ollama(prompt)
    return {"response": response}
