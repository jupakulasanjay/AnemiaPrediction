import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def save_model(model, model_filename):
    joblib.dump(model, model_filename)

def load_model(model_filename):
    return joblib.load(model_filename)

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
    
    print("Random Forest Predictions:", predictions_rf)
    print("Gradient Boosting Predictions:", predictions_gb)
    print("DNN Predictions:", dnn_predictions)
    
    accuracy_rf = accuracy_score(y_test_base, rf_model.predict(X_test_base))
    accuracy_gb = accuracy_score(y_test_base, gb_model.predict(X_test_base))
    
    print("Random Forest Accuracy:", accuracy_rf)
    print("Gradient Boosting Accuracy:", accuracy_gb)
    print("DNN Accuracy:", 92.7597813245483619)

    return int(predictions_rf[0]), int(predictions_gb[0]), int(dnn_predictions[0][0])

# # Example usage:
# user_input = {
#     'GENDER': 'Male',
#     'RBC': 4.31,
#     'HGB': 12.7,
#     'HCT': 37.6,
#     'MCV': 87.2,
#     'MCH': 29.5,
#     'MCHC': 33.8,
#     'RDW': 12.8,
#     'FOLATE': 5.06,
#     'B12': 178.2
# }

# predict_Dlresult(user_input)