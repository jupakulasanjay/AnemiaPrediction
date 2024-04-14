import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request
from sklearn.metrics import accuracy_score
import joblib
# from ModelPredict import predict_Dlresult

app = Flask(__name__, static_url_path='/static')

def load_model(model_filename):
    return joblib.load(model_filename)

# # Load saved models
# rf_model = load_model('rf_model.pkl')
# gb_model = load_model('gb_model.pkl')
# dnn_model = tf.keras.models.load_model('dnn_model.h5')

@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')

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

def predict_Dlresult(user_input):

    print(user_input)
    filename = "./uploads/uploaded_file.csv"
    df = pd.read_csv(filename)
    feature_names = [
        'GENDER', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW', 'FOLATE', 'B12'
    ]
    
    user_data = pd.DataFrame(user_input, index=[0])
    
    X_train = df[feature_names]
    y_train = df['All_Class']
    
    # Modify GENDER feature
    user_data['GENDER'] = 1 if user_input['GENDER'] == 'Male' else 0
    
    X_test = user_data[feature_names]
    
    rf_model = load_model('./rf_model.joblib')
    gb_model = load_model('./gb_model.joblib')
    dnn_model = tf.keras.models.load_model('./dnn_model1.h5')
    
    X_train_base, X_test_base, y_train_base, y_test_base = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    predictions_rf = rf_model.predict(X_test)
    predictions_gb = gb_model.predict(X_test)
    # predictions_dnn = dnn_model.predict(X_test)
    predictions_dnn = dnn_model.predict(X_test)
    dnn_predictions = np.round(predictions_dnn).astype(int)
    
    accuracy_rf = accuracy_score(y_test_base, rf_model.predict(X_test_base))
    accuracy_gb = accuracy_score(y_test_base, gb_model.predict(X_test_base))

    print(accuracy_rf, accuracy_gb)

    return int(predictions_rf[0]), int(predictions_gb[0]), int(dnn_predictions[0][0])

if __name__ == "__main__":
    app.run(debug=True)
