# Turbofan Engine RUL Prediction

## Overview
This project predicts the Remaining Useful Life (RUL) of turbofan engines using sensor data from the CMAPSS dataset. It implements machine learning models including Random Forest and XGBoost with feature engineering techniques to forecast engine degradation.

## Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn

Install dependencies:
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn


Data Preparation
Download the CMAPSS dataset from NASA's Turbofan Engine Degradation Simulation
Place these files in your working directory:
train_FD001.txt
test_FD001.txt
RUL_FD001.txt
Usage
Data Loading & Preprocessing :
Load and preprocess training/test data
Calculate RUL for each engine cycle
Normalize sensor data
Perform feature engineering (rolling statistics, lag features)
Model Training :
Baseline models: Random Forest and XGBoost
Hyperparameter tuning with GridSearchCV
Advanced feature engineering with sensor aggregations
Evaluation :
Metrics: RMSE, MAE, R², MAPE
Visualization of prediction vs actual RUL

Key Results
XGBoost (Base)
RMSE 36.85
MAE 25.61
R^2 0.21
ACCURACY 57.43%
XGBoost (Enriched)
RMSE 32.90
MAE 23.44
R^2 0.37
ACCURACY 62.63%


.
├── train_FD001.txt    # Training data
├── test_FD001.txt     # Test data
├── RUL_FD001.txt      # Validation RUL values
├── rul_prediction.ipynb # Main Jupyter notebook



This README provides a clear overview of the project, dependencies, data requirements, usage instructions, and key results. The user can customize paths and parameters as needed for their specific implementation.




This is my 1st year 2nd semester project. Created this with beginner level knowledge and understanding in data science and machine learning. Will try to improve the accuracy as I learn more.