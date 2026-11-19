
import numpy as np
import pandas as pd
import joblib
import pytest

from tensorflow.keras.models import load_model
from sklearn.metrics import r2_score, mean_absolute_percentage_error


# Load saved model and preprocessor
model = load_model("flight_price_model.keras")
preprocessor = joblib.load("preprocessor.pkl")


# Load independent test dataset
df = pd.read_csv("test_data.csv")


# Define numerical and categorical features
numerical_cols = [
    'distance', 'time', 'year', 'month', 'day', 'day_of_week'
]

categorical_cols = [
    'from', 'to', 'flightType', 'agency'
]


# Separate input features and actual target
X_test = df[numerical_cols + categorical_cols]
y_test = df['price']


# Transform test data using saved preprocessor
X_test_processed = preprocessor.transform(X_test)


# Test 1: Check whether model exists
def test_model_exists():
    assert model is not None


# Test 2: Check prediction dimensions
def test_prediction_shape():
    predictions = model.predict(X_test_processed).flatten()
    assert predictions.shape == y_test.shape


# Test 3: Check for valid numerical predictions
def test_predictions_valid():
    predictions = model.predict(X_test_processed).flatten()
    assert np.all(np.isfinite(predictions))


# Test 4: Check whether predictions are positive
def test_predictions_positive():
    predictions = model.predict(X_test_processed).flatten()
    assert np.all(predictions > 0)


# Test 5: Check model performance
def test_model_performance():
    predictions = model.predict(X_test_processed).flatten()

    r2 = r2_score(y_test, predictions)

    mape = mean_absolute_percentage_error(
        y_test, predictions
    ) * 100

    print(f"R2 Score: {r2:.4f}")
    print(f"MAPE: {mape:.2f}%")

    assert r2 > 0.90
    assert mape < 10
