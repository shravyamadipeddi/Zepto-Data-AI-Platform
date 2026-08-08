# Module 3 – Zepto AI Customer Support Assistant

## Overview

This module implements an AI-powered customer support assistant for Zepto using Retrieval-Augmented Generation (RAG). It retrieves relevant policy documents from a vector database and returns accurate answers through a FastAPI REST API.

---

## Features

- FastAPI REST API
- LangGraph workflow orchestration
- Chroma vector database
- HuggingFace sentence embeddings
- Semantic document retrieval
- Intent classification
- Confidence score in responses
- Source document tracking

---

## Project Structure

```
support_assistant/
│
├── docs/
│   ├── doc_01.txt
│   ├── doc_02.txt
|   ├── doc_03.txt
|   ├── doc_04.txt
|   ├── doc_05.txt
|   ├── doc_06.txt
|   ├── doc_07.txt
│   └── doc_08.txt
│
├── chroma_db/
├── embed.py
├── graph.py
├── main.py
├── models.py
├── prompts.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r support_assistant/requirements.txt
```

---

## Build Vector Database

```bash
python support_assistant/embed.py
```

---

## Run API

```bash
uvicorn support_assistant.main:app --reload
```

API:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /ask

Request

```json
{
  "query": "What is Zepto's refund policy?"
}
```

Example Response

```json
{
  "answer": "Based on the retrieved context...",
  "sources": [
    "support_assistant/docs/doc_02.txt",
    "support_assistant/docs/doc_05.txt"
  ],
  "confidence": 1.0
}
```

---

## Technologies Used

- Python
- FastAPI
- LangGraph
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Pydantic

---

## Workflow

User Question

↓

Intent Classification

↓

Semantic Search

↓

Retrieve Relevant Documents

↓

Generate Response

↓

Return Answer + Sources + Confidence


## Author

Shravya Madipeddi