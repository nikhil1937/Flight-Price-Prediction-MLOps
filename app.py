from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import dill  # <--- CRITICAL: Required for unpickling custom preprocessors
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Load the saved model and fitted preprocessor
preprocessor = joblib.load("preprocessor.pkl")
model = load_model("flight_price_model.keras")

required_cols = [
    "distance", "time", "year", "month", "day",
    "day_of_week", "from", "to", "flightType", "agency"
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flight Price Prediction API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "Send a valid JSON object"}), 400

        missing = [col for col in required_cols if col not in data]
        if missing:
            return jsonify({"error": "Missing required fields", "missing_fields": missing}), 400

        input_df = pd.DataFrame([{col: data[col] for col in required_cols}])
        processed = preprocessor.transform(input_df)
        prediction = float(model.predict(processed, verbose=0).flatten()[0])

        return jsonify({"predicted_price": round(prediction, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007, debug=False)
