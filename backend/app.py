from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)
model = joblib.load("../ai/model.pkl")
scaler = joblib.load("../ai/scaler.pkl")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    input_df = pd.DataFrame([data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    return jsonify({"recommended_material": prediction[0]})
