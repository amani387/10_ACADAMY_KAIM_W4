# Rossmann Pharmaceuticals Sales Forecasting

## Overview

This project focuses on predicting daily sales for Rossmann Pharmaceuticals stores across several cities for the next six weeks. The goal is to build and serve an end-to-end machine learning product that delivers accurate sales predictions to analysts in the finance team.

## Objectives

1. **Exploration of Customer Purchasing Behavior**: 
   - Analyze factors influencing customer purchases.
   - Identify seasonal trends and the effects of promotions.

2. **Prediction of Store Sales**:
   - Build machine learning models to predict daily sales.
   - Use advanced preprocessing techniques and feature engineering.

3. **Deep Learning Approach**:
   - Develop an LSTM-based regression model for sales prediction.

4. **Model Serving**:
   - Create a REST API to deliver real-time sales predictions.

## Key Features

- **Exploratory Data Analysis**: 
  - Analyze correlations, trends, and the impact of holidays and promotions on sales.
  - Handle missing data and outliers.
  - Visualize findings with appropriate plots.

- **Machine Learning**:
  - Implement sklearn pipelines for modular and reproducible models.
  - Use tree-based algorithms like Random Forest for regression.
  - Tune hyperparameters and evaluate models with custom loss functions.

- **Deep Learning**:
  - Build and train LSTM models using TensorFlow or PyTorch.
  - Transform time-series data for supervised learning.
  - Estimate confidence intervals for predictions.

- **Model Deployment**:
  - Serialize trained models with timestamps for tracking.
  - Develop a REST API using Flask or FastAPI to serve predictions.

## Tools and Technologies

- Python: Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch, Matplotlib
- Flask/FastAPI: REST API development
- GitHub: Code versioning and CI/CD pipelines
- Logging: Traceability using Python's logger library
- Data Version Control (DVC): MLOps for model and data management

## Project Deliverables

1. **Exploratory Analysis Notebook**:
   - Insights into customer behavior with visualizations and summaries.

2. **Machine Learning Models**:
   - Sklearn pipelines for preprocessing and predictions.
   - Serialized models saved with timestamps.

3. **Deep Learning Models**:
   - LSTM-based time-series forecasting.

4. **API Endpoint**:
   - REST API to handle prediction requests and return sales forecasts.

5. **Interim Submission**:
   - Slide deck summarizing findings from Task 1.

6. **Final Submission**:
   - PDF report suitable for publication as a blog.
   - GitHub repository with all code and outputs.

## Learning Outcomes

- Advanced feature engineering and data preprocessing
- Machine learning model building and hyperparameter tuning
- Deep learning techniques for time-series forecasting
- CI/CD for ML models with MLOps tools
- Communication and reporting of technical findings


