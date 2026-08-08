from fastapi import FastAPI

from support_assistant.graph import graph
from support_assistant.models import AskRequest, AskResponse

app = FastAPI(
    title="Zepto Support Assistant",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Zepto Support Assistant is running."
    }


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):

    result = graph.invoke(
        {
            "query": request.query,
            "intent": "",
            "answer": "",
            "sources": [],
            "confidence": 0.0
        }
    )

    return AskResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"]
    )