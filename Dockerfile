FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .

# Step 1: Install lightweight packages first
RUN pip install --default-timeout=100 --retries=5 numpy pandas scikit-learn flask requests joblib dill flask-cors

# Step 2: Install TensorFlow and Keras separately with retries
RUN pip install --default-timeout=100 --retries=5 tensorflow keras

COPY app.py .
COPY preprocessor.pkl .
COPY flight_price_model.keras .
EXPOSE 5007
CMD ["python", "app.py"]
