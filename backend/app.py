from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Define base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler from ai folder
model_path = os.path.join(base_dir, '..', 'ai', 'model.pkl')
scaler_path = os.path.join(base_dir, '..', 'ai', 'scaler.pkl')

# Check if files exist
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")
if not os.path.exists(scaler_path):
    raise FileNotFoundError(f"Scaler file not found at {scaler_path}")

# Load model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    input_df = pd.DataFrame([data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    return jsonify({"recommended_material": prediction[0]})

