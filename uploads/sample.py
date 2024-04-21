import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# Define a dictionary to map model classes to their names
model_names = {
    RandomForestClassifier: "Random Forest",
    GradientBoostingClassifier: "Gradient Boosting",
    SVC: "Support Vector Machine",
    KNeighborsClassifier: "K-Nearest Neighbors"
}

def get_user_input(features, input_data):
    """Prompts the user for required data and returns a Pandas DataFrame.

    Handles potential user input errors gracefully.

    Returns:
        pd.DataFrame: A DataFrame containing the user-provided data.
    """

    print("Choose from the following input datasets:")
    for i, data in enumerate(input_data):
        print(f"Choose {i}: {data['name']}")

    while True:
        try:
            index = int(input("Enter the index of the dataset you want to use: "))
            if 0 <= index < len(input_data):
                chosen_data = input_data[index]['data']
                break
            else:
                print("Invalid index. Please choose from the available options.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    data = {}
    for column, value in zip(features, chosen_data):
        data[column] = value

    return pd.DataFrame([data])

def train_and_evaluate(model_class, X_train, y_train, X_test):
    """Trains and evaluates a given model using cross-validation.

    Returns:
        float: Mean accuracy of the model.
    """

    model = model_class()
    # Train the model
    model.fit(X_train, y_train)
    # Evaluate using cross-validation
    scores = cross_val_score(model, X_train, y_train, cv=5)
    # Return the mean accuracy
    return scores.mean()

def print_predictions(predictions):
    # Find the index of the maximum probability value in each row
    max_index = predictions.iloc[:, :-1].values.argmax(axis=1)

    # Add 1 to convert zero-based index to class number
    all_class_values = max_index

    # Create a copy of the predictions DataFrame and replace 'All_Class' column with the calculated values
    predictions_with_all_class = predictions.copy()
    predictions_with_all_class['All_Class'] = all_class_values

    # Print the modified predictions DataFrame
    print(predictions_with_all_class)

def main():
    """Trains models, makes predictions, and prints results using the chosen dataset."""

    # Get file path from user
    file_path = input("Enter the file path of the dataset (csv): ")

    # Load dataset
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
        return

    # Define features and target variables
    features = [
        'GENDER', 'RBC', 'HGB', 'HCT',
        'MCV', 'MCH', 'MCHC', 'RDW', 'FOLATE', 'B12'
    ]
    target_variables = [
        'All_Class', 'HGB_Anemia_Class', 'Iron_anemia_Class',
        'Folate_anemia_class', 'B12_Anemia_class'
    ]

    # Predefined input data arrays
    input_data_arrays = [
        {
            "name": "Data Array 1 for class 4 test",
            "data": [1, 4.31, 12.7, 37.6, 87.2, 29.5, 33.8, 12.8, 5.06, 178.2]
        },
        {
            "name": "Data Array 2 for class 3 test",
            "data": [1, 4.6, 12.1, 37.6, 81.7, 26.3, 32.2, 15.4, 3.51, 217.6]
        },
        {
            "name": "Data Array 3 for class 2 test",
            "data": [1, 4.47, 12.4, 37.7, 84.3, 27.7, 32.9, 18, 11.13, 181.5]
        },
        {
            "name": "Data Array 4 for class 1 test",
            "data": [1, 4.41, 12.13, 35.11, 79.58, 27.48, 34.54, 12.92, 6.28, 631.2]
        },
        {
            "name": "Data Array 5 for non anemic",
            "data": [1, 5.83, 16.17, 49.05, 84.11, 27.72, 32.96, 11.72, 6.86, 485.7]
        }
    ]

    # Get user input and validate numerical values
    user_data = get_user_input(features, input_data_arrays)

    # Split data into features and target variables
    X = df[features]
    y = df[target_variables]

    # Define the additional algorithms
    additional_algorithms = [SVC, KNeighborsClassifier]

    # Train and predict using all models
    accuracies = {}
    for model_class in [RandomForestClassifier, GradientBoostingClassifier] + additional_algorithms:
        model_name = model_names.get(model_class, model_class.__name__)
        print(f"\nTraining and evaluating {model_name}...")
        accuracy = train_and_evaluate(model_class, X, y['All_Class'], user_data)
        accuracies[model_name] = accuracy
        print(f"{model_name} Mean Accuracy: {accuracy:.4f}")

    # Print accuracies
    print("\nAccuracies:")
    for model_name, accuracy in accuracies.items():
        print(f"{model_name}: {accuracy:.4f}")

    # Train and predict using both models
    rf_predictions = train_and_evaluate(RandomForestClassifier, X, y['All_Class'], user_data)
    gb_predictions = train_and_evaluate(GradientBoostingClassifier, X, y['All_Class'], user_data)

    # Print user-provided data
    print("\nUser-provided data:")
    print(user_data)

    # Print predictions for both models
    print("\nRandom Forest Predictions:")
    print_predictions(rf_predictions)
    print("\nGradient Boosting Predictions:")
    print_predictions(gb_predictions)

if __name__ == "__main__":
    main()
