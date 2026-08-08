# Module 2: Analytics Pipeline

## Overview

This module builds a complete Machine Learning analytics pipeline using the Titanic dataset. It covers data cleaning, exploratory data analysis (EDA), preprocessing, feature engineering, model training, evaluation, hyperparameter tuning, and model serialization.

---

## Objectives

- Load and explore the Titanic dataset
- Handle missing values and clean the data
- Perform Exploratory Data Analysis (EDA)
- Preprocess numerical and categorical features
- Train multiple Machine Learning models
- Handle class imbalance using SMOTE
- Perform hyperparameter tuning with GridSearchCV
- Evaluate model performance
- Save the best trained model

---

## Dataset

"Dataset:" Titanic Passenger Dataset

"Target Variable:"

- `survived`

---

## Project Structure

```text
analytics/
│
├── analytics_pipeline.ipynb
├── titanic.csv
├── titanic_cleaned.csv
├── best_model.joblib
└── README.md
```

---

## Data Cleaning

The following preprocessing steps were performed:

- Removed columns with excessive missing values
- Filled missing categorical values
- Dropped remaining missing rows
- Removed target leakage (`alive`)
- Standardized numerical features
- Encoded categorical variables using OneHotEncoder

---

## Exploratory Data Analysis

The notebook includes:

- Dataset overview
- Missing value analysis
- Summary statistics
- Histograms
- Boxplots
- Correlation Heatmap
- Pairplots
- Survival rate analysis
- Feature distribution analysis

---

## Feature Engineering

- Numerical feature scaling using StandardScaler
- Categorical encoding using OneHotEncoder
- ColumnTransformer pipeline
- Scikit-learn Pipeline implementation

---

## Machine Learning Models

The following classification models were trained:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

---

## Handling Class Imbalance

SMOTE was explored on the training data to demonstrate class balancing. The final model comparison and hyperparameter tuning were performed using the preprocessing pipeline without SMOTE.

---

## Hyperparameter Tuning

Random Forest was optimized using GridSearchCV.

### Tuned Parameters

- n_estimators
- max_depth
- max_features

The model was configured with:

- bootstrap=True
- oob_score=True

to report the Out-of-Bag (OOB) score.

---

## Best Model Results

"Best Parameters"

```text
max_depth = 5
max_features = sqrt
n_estimators = 200
```

"Performance"

| Metric | Value |
|---------|------:|
| Cross Validation Score | 0.8199 |
| OOB Score | 0.8200 |
| Test Accuracy | 0.8202 |
| Weighted F1 Score | 0.82 |

---

## Regression Analysis

A Linear Regression model was also trained to predict the `fare` variable.

Evaluation metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Model Serialization

The best trained model is saved using Joblib.

```python
joblib.dump(best_model, "best_model.joblib")
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Joblib

---

## Learning Outcomes

This module demonstrates:

- Data preprocessing
- Missing value handling
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Pipelines
- Model Evaluation
- Hyperparameter Optimization
- Model Serialization
- Classification and Regression techniques

---

## Author

"Shravya Madipeddi"
