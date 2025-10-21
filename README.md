# Earthquake Alert Prediction

A Machine Learning-based system to predict earthquake alerts using Random Forest. Includes preprocessing, trained models,Flask API, and a Streamlit frontend.

## Files

- `RandomForestClassifier_model.pkl` – Initial model  
- `best_rf_model.pkl` – Optimized model  
- `earthquake-alert-prediction.ipynb` – Notebook with training and evaluation  
- `earthquake_alert_balanced_dataset.csv` – Dataset  
- `flask_app.py` – API backend  
- `streamlit_app.py` – Interactive frontend  
- `label_encoder.pkl` – Encodes categorical features  
- `scaler.pkl` – Normalizes numerical features  
- `LICENSE` – License file  

## Installation

```bash
git clone https://github.com/your-username/xlr8-git.git
cd xlr8-git
python -m venv venv
# Activate virtual environment
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
## Usage

Flask API
```bash
python flask_app.py
```

Runs at 
```bash

http://127.0.0.1:5000/predict.
```
Streamlit App

```bash

streamlit run streamlit_app.py
```

Open the provided URL in a browser to interact with the prediction interface.

Example Input
{
  "magnitude": 5.5,
  "depth": 10,
  "latitude": 34.05,
  "longitude": -118.25
}
