from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("best_rf_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data], columns=['magnitude', 'depth', 'cdi', 'mmi', 'sig'])
    
    # Scale features
    df_scaled = scaler.transform(df)
    
    # Predict
    pred_encoded = model.predict(df_scaled)
    pred_alert = le.inverse_transform(pred_encoded)
    
    return jsonify({"predicted_alert": pred_alert[0]})

if __name__ == "__main__":
    app.run(debug=True)
