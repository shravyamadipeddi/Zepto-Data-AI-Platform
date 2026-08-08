import os

from langgraph.graph import StateGraph, END

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from support_assistant.models import GraphState

# ----------------------------------------------------
# Environment Variable
# ----------------------------------------------------

MOCK_LLM = os.getenv("MOCK_LLM", "1")

# ----------------------------------------------------
# Load Embedding Model
# ----------------------------------------------------

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="support_assistant/chroma_db",
    embedding_function=embedding
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# ----------------------------------------------------
# Node 1
# classify_intent
# ----------------------------------------------------

POLICY_KEYWORDS = [
    "delivery",
    "return",
    "refund",
    "membership",
    "tracking",
    "cancel",
    "gift card",
    "support hours"
]


def classify_intent(state: GraphState):

    query = state["query"].lower()

    if any(keyword in query for keyword in POLICY_KEYWORDS):
        state["intent"] = "policy_question"
    else:
        state["intent"] = "general_question"

    return state


# ----------------------------------------------------
# Node 2
# retrieve_and_answer
# ----------------------------------------------------

def retrieve_and_answer(state: GraphState):

    docs = retriever.invoke(state["query"])

    state["sources"] = [
        doc.metadata.get("source", "")
        for doc in docs
    ]

    retrieved_context = "\n\n".join(
        doc.page_content for doc in docs
    )

    if MOCK_LLM == "1":

        state["answer"] = (
            f"Based on the retrieved context: \n\n{retrieved_context}"
        )

        state["confidence"] = 1.0

    else:

        state["answer"] = "Real LLM path not implemented."

        state["confidence"] = 0.0

    return state


# ----------------------------------------------------
# Node 3
# direct_answer
# ----------------------------------------------------

def direct_answer(state: GraphState):

    if MOCK_LLM == "1":

        state["answer"] = (
            "I can only answer questions about Zepto policies right now."
        )

        state["sources"] = []

        state["confidence"] = 1.0

    else:

        state["answer"] = "Real LLM path not implemented."

        state["sources"] = []

        state["confidence"] = 0.0

    return state


# ----------------------------------------------------
# Routing Function
# ----------------------------------------------------

def route(state: GraphState):

    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"


# ----------------------------------------------------
# Build Graph
# ----------------------------------------------------

builder = StateGraph(GraphState)

builder.add_node("classify_intent", classify_intent)

builder.add_node(
    "retrieve_and_answer",
    retrieve_and_answer
)

builder.add_node(
    "direct_answer",
    direct_answer
)

builder.set_entry_point("classify_intent")

builder.add_conditional_edges(
    "classify_intent",
    route,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)

builder.add_edge(
    "retrieve_and_answer",
    END
)

builder.add_edge(
    "direct_answer",
    END
)

graph = builder.compile()