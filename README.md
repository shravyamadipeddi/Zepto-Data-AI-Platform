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

## Repository Structure

```text
Zepto-Data-AI-Platform/
│
├── analytics/
│   ├── analytics_pipeline.ipynb
│   ├── best_model.joblib
│   └── README.md
│
├── data_pipeline/
│   ├── scraper.py
│   ├── database.py
│   ├── queries.py
│   └── README.md
│
├── support_assistant/
│   ├── embed.py
│   ├── graph.py
│   ├── main.py
│   ├── models.py
│   ├── prompts.py
│   └── README.md
│
├── README.md
└── .gitignore

## Module Design Decisions

### Data Pipeline
The pipeline separates scraping, cleaning, database creation, and analytical queries. Scraped data is stored as CSV, cleaned with Pandas, and loaded into a normalized SQLite database containing separate books and categories tables.

### Analytics
The analytics pipeline uses preprocessing for numerical and categorical features and compares multiple machine-learning models. Random Forest is tuned using GridSearchCV and evaluated using test metrics and Out-of-Bag (OOB) scoring.

### Support Assistant
The support assistant uses semantic retrieval over Zepto policy documents. LangGraph manages intent classification and conditional routing, while Chroma stores document embeddings for similarity search. FastAPI exposes the assistant through a REST API.