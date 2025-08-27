from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    input_df = pd.DataFrame([data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    return jsonify({"recommended_material": prediction[0]})
