import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import joblib

def stacking_ensemble(base_model1, base_model2, base_model3, meta_model, X_train, y_train, X_test):
    # Train base models
    base_model1.fit(X_train, y_train)
    base_model2.fit(X_train, y_train)
    base_model3.fit(X_train, y_train)
    
    # Generate predictions from base models
    base_model1_predictions = base_model1.predict(X_train)
    base_model2_predictions = base_model2.predict(X_train)
    base_model3_predictions = base_model3.predict(X_train)
    
    # Train the meta model using base model predictions
    meta_features = np.column_stack((base_model1_predictions, base_model2_predictions, base_model3_predictions))
    meta_model.fit(meta_features, y_train)
    
    # Generate predictions on test set
    base_model1_test_predictions = base_model1.predict(X_test)
    base_model2_test_predictions = base_model2.predict(X_test)
    base_model3_test_predictions = base_model3.predict(X_test)
    
    # Create meta features for test set
    test_meta_features = np.column_stack((base_model1_test_predictions, base_model2_test_predictions, base_model3_test_predictions))
    
    # Generate final predictions using the meta model
    final_predictions = meta_model.predict(test_meta_features)
    
    return final_predictions

def save_model(model, model_filename):
    joblib.dump(model, model_filename)

def load_model(model_filename):
    return joblib.load(model_filename)

def predict(user_input):
    filename = "C:/Users/sanju/OneDrive/Desktop/pro11/uploads/uploaded_file.csv"
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
    
    rf_model = RandomForestClassifier()
    gb_model = GradientBoostingClassifier()
    dnn_model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    dnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Placeholder model for demonstration
    placeholder_model = RandomForestClassifier()  
    
    X_train_base, X_test_base, y_train_base, y_test_base = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    rf_model.fit(X_train_base, y_train_base)
    gb_model.fit(X_train_base, y_train_base)
    dnn_model.fit(X_train_base, y_train_base, epochs=50, batch_size=32, validation_split=0.2)
    
    save_model(rf_model, 'C:/Users/sanju/OneDrive/Desktop/pro11/rf_model.joblib')
    save_model(gb_model, 'C:/Users/sanju/OneDrive/Desktop/pro11/gb_model.joblib')
    dnn_model.save('C:/Users/sanju/OneDrive/Desktop/pro11/dnn_model.h5')
    
    rf_model = load_model('rf_model.joblib')
    gb_model = load_model('gb_model.joblib')
    dnn_model = tf.keras.models.load_model('dnn_model.h5')
    
    predictions_rf = rf_model.predict(X_test)
    predictions_gb = gb_model.predict(X_test)
    predictions_dnn = dnn_model.predict(X_test)
    
    print("Random Forest Predictions:", predictions_rf)
    print("Gradient Boosting Predictions:", predictions_gb)
    print("DNN Predictions:", predictions_dnn)

# C:\Users\sanju\OneDrive\Desktop\pro11

# Example usage:
user_input = {
    'GENDER': 'Male',
    'RBC': 4.73,
    'HGB': 11.6,
    'HCT': 36.5,
    'MCV': 77.2,
    'MCH': 24.5,
    'MCHC': 31.8,
    'RDW': 14.9,
    'FOLATE': 4.69,
    'B12': 198.1
}

predict(user_input)
