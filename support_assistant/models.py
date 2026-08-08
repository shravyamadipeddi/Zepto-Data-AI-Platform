from typing import List
from pydantic import BaseModel
from typing_extensions import TypedDict


class GraphState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: List[str]
    confidence: float


class AskRequest(BaseModel):
    query: str


class AskResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float