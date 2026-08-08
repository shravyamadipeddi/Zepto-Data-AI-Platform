# Zepto Data & AI Platform

An end-to-end data and AI platform project built with Python, covering data engineering, analytics, machine learning, and an AI-powered customer support assistant.

## Modules

### Module 1 – Data Pipeline
- Data ingestion and cleaning
- Data transformation
- Pandas-based data processing
- SQL queries and database operations
- Generated cleaned datasets

### Module 2 – Analytics & Machine Learning
- Exploratory Data Analysis
- Feature preprocessing
- Classification
- Logistic Regression
- Decision Tree
- Random Forest
- SMOTE for class balancing
- Hyperparameter tuning using GridSearchCV
- Model evaluation using Accuracy, Precision, Recall and F1-score
- Out-of-Bag (OOB) evaluation for Random Forest
- Regression using Linear Regression
- Model serialization using Joblib

### Module 3 – AI Support Assistant
- Document loading
- Text chunking
- Semantic search
- HuggingFace embeddings
- Chroma vector database
- LangGraph workflow
- Intent classification
- Retrieval-based responses
- FastAPI backend

## Project Structure

```text
Zepto-Data-AI-Platform/
│
├── analytics/
│   ├── analytics_pipeline.ipynb
│   ├── titanic.csv
│   ├── titanic_cleaned.csv
│   └── best_model.joblib
│
├── data_pipeline/
│   ├── books.csv
│   ├── books_cleaned.csv
│   ├── books.db
│   ├── database.py
│   ├── queries.py
│   └── ...
│
├── support_assistant/
│   ├── docs/
│   ├── chroma_db/
│   ├── embed.py
│   ├── graph.py
│   ├── main.py
│   ├── models.py
│   ├── prompts.py
│   ├── Dockerfile
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
└── README.md