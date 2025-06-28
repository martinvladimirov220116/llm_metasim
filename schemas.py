from pydantic import BaseModel
from typing import List

class CleanTextRequest(BaseModel):
    text: str

class ChatRequest(BaseModel):
    history: List[str]