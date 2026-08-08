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

## How to Run the Project

### Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate

# Module 1 — Data Pipeline

Install the required packages:

pip install -r data_pipeline/requirements.txt

Run the pipeline:

python data_pipeline/scraper.py
python data_pipeline/database.py
python data_pipeline/queries.py
This scrapes the book data, cleans it, creates the SQLite database, and runs the SQL queries.

# Module 2 — Analytics

Open:

analytics/analytics_pipeline.ipynb

Run the notebook cells from top to bottom.

The notebook performs data cleaning, exploratory analysis, machine learning model training, hyperparameter tuning, evaluation, and regression analysis.

# Module 3 — Support Assistant

Install the required packages:

pip install -r support_assistant/requirements.txt

Build the vector database:

python support_assistant/embed.py

Start the FastAPI server:

uvicorn support_assistant.main:app --reload

Open Swagger UI in your browser:

http://127.0.0.1:8000/docs

Use the POST /ask endpoint to ask questions.

## Notes

The project is organized as three independent but related modules covering data engineering, machine learning analytics, and retrieval-augmented customer support.