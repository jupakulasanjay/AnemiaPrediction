import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request
import joblib
from test5 import predict_Dlresult

app = Flask(__name__, static_url_path='/static')

def load_model(model_filename):
    return joblib.load(model_filename)

# Load saved models
rf_model = load_model('rf_model.pkl')
gb_model = load_model('gb_model.pkl')
dnn_model = tf.keras.models.load_model('dnn_model.h5')

@app.route('/')
def index():
    features = [
        'GENDER', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW', 'FOLATE', 'B12'
    ]
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])

def predict():
    filename = "./uploads/uploaded_file.csv"
    df = pd.read_csv(filename)
    feature_names = [
        'GENDER', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW', 'FOLATE', 'B12'
    ]

    user_input = {feature: request.form.get(feature) for feature in feature_names}
    # user_data = pd.DataFrame(user_input, index=[0])

    for i in user_input:
        if i != 'GENDER':
            user_input[i] = float(user_input[i])

    print(user_input)

    predictions_rf, predictions_gb, dnn_predictions = predict_Dlresult(user_input)
    print(predictions_rf, predictions_gb, dnn_predictions)
    
    combined_predictions = (predictions_rf + predictions_gb + dnn_predictions) / 3.0
    predicted_anemia = np.round(combined_predictions)
    predicted_class = (predictions_rf)
    return render_template('result.html', predicted_anemia=predicted_anemia, predicted_class=predicted_class)

if __name__ == "__main__":
    app.run(debug=True)
