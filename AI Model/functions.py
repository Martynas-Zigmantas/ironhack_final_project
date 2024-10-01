import pandas as pd
import streamlit as st
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from datetime import datetime
import os

def show_toolbar():
    # Load the data to get unique values for the dropdowns
    data = load_and_preprocess_data()

    # Convert all values to strings to handle type errors
    data['airline'] = data['airline'].astype(str)
    data['departure_city'] = data['departure_city'].astype(str)
    data['destination_city'] = data['destination_city'].astype(str)
    data['departure_time_scheduled'] = data['departure_time_scheduled'].astype(str)

    # Create a horizontal layout with st.columns
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    # Display dropdowns and date input in columns
    with col1:
        # Sort airline options alphabetically
        airline_options = sorted(data['airline'].unique())
        airline = st.selectbox('Airline', options=airline_options)

    with col2:
        # Sort departing_from options alphabetically
        departing_from_options = sorted(data['departure_city'].unique())
        departing_from = st.selectbox('Departing From', options=departing_from_options)

    with col3:
        # Sort destination options alphabetically
        destination_options = sorted(data['destination_city'].unique())
        destination = st.selectbox('Destination', options=destination_options)

    with col4:
        # Sort time options alphabetically
        time_options = sorted(data['departure_time_scheduled'].unique())
        time = st.selectbox('Time', options=time_options)

    with col5:
        # No sorting needed for dates
        date = st.date_input('Date', value=pd.to_datetime("2024-01-01"))

    # Create a submit button under the columns
    submit_col = st.columns(1)[0]  # For the submit button, span across one column
    with submit_col:
        if st.button('Submit'):
            # Create the validation DataFrame with selected inputs
            validation_data = pd.DataFrame({
                'airline': [airline],
                'departure_city': [departing_from],
                'destination_city': [destination],
                'departure_time_scheduled': [time],
                'date_depart': [str(date)]
            })

            # Run the prediction function with the validation data
            process_and_predict_with_regression(validation_data)


# Load and preprocess the data
def load_and_preprocess_data():
    # Load the dataset
    data = pd.read_csv('departures_for_model.csv')

    # Combine 'date_depart' and 'departure_time_scheduled' into a datetime column
    data['departure_datetime'] = data['date_depart'] + ' ' + data['departure_time_scheduled']
    data['departure_datetime'] = pd.to_datetime(data['departure_datetime'], format='%Y-%m-%d %H:%M:%S')

    data['status_class'] = data['departure_time_difference'].apply(lambda x: 0 if x < 10 else 1)
    
    # Convert 'date_depart' to datetime
    data['date_depart'] = pd.to_datetime(data['date_depart'], format='%Y-%m-%d')

    # Create 'time_of_day_bin' using the 'departure_datetime' column
    def time_of_day_category(departure_time):
        if 5 <= departure_time.hour < 9:
            return 1  # Morning (5 AM - 9 AM)
        elif 9 <= departure_time.hour < 13:
            return 2  # Noon (9 AM - 1 PM)
        elif 13 <= departure_time.hour < 18:
            return 3  # Afternoon (1 PM - 6 PM)
        else:
            return 4  # Evening/Night (6 PM - 5 AM)

    data['time_of_day_bin'] = data['departure_datetime'].apply(time_of_day_category)

    # Extract 'day' from 'date_depart'
    data['day'] = data['date_depart'].dt.day

    # Load additional features
    average_departure_time_difference = pd.read_csv('features_departures/average_departure_time_difference.csv')
    avg_day_airline = pd.read_csv('features_departures/avg_day_airline.csv')
    avg_day_destination = pd.read_csv('features_departures/avg_day_destination.csv')
    avg_time_airline = pd.read_csv('features_departures/avg_time_airline.csv')
    avg_day_airport = pd.read_csv('features_departures/avg_day_airport.csv')

    # Merge with the necessary datasets
    data = pd.merge(data, avg_day_destination, on=['destination_city', 'day'], how='left')
    data = pd.merge(data, avg_time_airline, on=['airline', 'time_of_day_bin'], how='left')
    data = pd.merge(data, avg_day_airline, on=['airline', 'day'], how='left')
    data = pd.merge(data, avg_day_airport, on=['departure_city', 'day'], how='left')
    data = pd.merge(data, average_departure_time_difference, on='airline', how='left')

    return data

# Define and train the models
def train_models():
    # Load and preprocess the data
    data = load_and_preprocess_data()

    # Define features and target for regression
    X_reg = data[['airline', 'departure_city', 'destination_city', 
                  'average_departure_time_difference', 'avg_time_airline', 
                  'avg_day_airline', 'avg_day_destination', 'avg_day_airport']]
    y_reg = data['departure_time_difference']

    # Split the data into training and test sets for regression
    X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

    # Define and train the regression model
    regressor_model = Pipeline(steps=[
        ('preprocessor', ColumnTransformer(
            transformers=[
                ('num', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='mean'))
                ]), ['average_departure_time_difference', 'avg_time_airline', 
                     'avg_day_airline', 'avg_day_destination', 'avg_day_airport']),
                ('cat', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore'))
                ]), ['airline', 'departure_city', 'destination_city'])
            ],
            remainder='passthrough'
        )),
        ('model', GradientBoostingRegressor(n_estimators=100, random_state=42))
    ])
    regressor_model.fit(X_reg_train, y_reg_train)

    # Define features and target for classification
    X_cls = data[['airline', 'departure_city', 'destination_city', 
                  'average_departure_time_difference', 'avg_time_airline', 
                  'avg_day_airline', 'avg_day_destination']]
    y_cls = data['status_class']

    # Split the data into training and test sets for classification
    X_cls_train, X_cls_test, y_cls_train, y_cls_test = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

    # Define and train the classification model
    classifier_model = Pipeline(steps=[
        ('preprocessor', ColumnTransformer(
            transformers=[
                ('cat', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore'))
                ]), ['airline', 'departure_city', 'destination_city']),
                ('num', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='mean')),
                    ('scaler', StandardScaler())
                ]), ['average_departure_time_difference', 'avg_time_airline', 
                     'avg_day_airline', 'avg_day_destination'])
            ]
        )),
        ('classifier', GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42))
    ])
    classifier_model.fit(X_cls_train, y_cls_train)

    return classifier_model, regressor_model


def process_and_predict_with_regression(validation_data, threshold=0.45):
    # Train the models
    classifier_model, regressor_model = train_models()

    # Convert columns to string types
    validation_data['date_depart'] = validation_data['date_depart'].astype(str)
    validation_data['departure_time_scheduled'] = validation_data['departure_time_scheduled'].astype(str)

    # Create 'departure_datetime' by concatenating 'date_depart' and 'departure_time_scheduled'
    validation_data['departure_datetime'] = validation_data['date_depart'] + ' ' + validation_data['departure_time_scheduled']
    validation_data['departure_datetime'] = pd.to_datetime(validation_data['departure_datetime'], format='%Y-%m-%d %H:%M:%S')

    # Create 'time_of_day_bin' and 'day' in validation data
    validation_data['time_of_day_bin'] = validation_data['departure_datetime'].apply(time_of_day_category)
    validation_data['day'] = validation_data['date_depart'].apply(pd.to_datetime).dt.day

    # Merge with necessary datasets
    average_departure_time_difference = pd.read_csv('features_departures/average_departure_time_difference.csv')
    avg_day_airline = pd.read_csv('features_departures/avg_day_airline.csv')
    avg_day_destination = pd.read_csv('features_departures/avg_day_destination.csv')
    avg_time_airline = pd.read_csv('features_departures/avg_time_airline.csv')
    avg_day_airport = pd.read_csv('features_departures/avg_day_airport.csv')

    validation_data = pd.merge(validation_data, avg_day_destination, on=['destination_city', 'day'], how='left')
    validation_data = pd.merge(validation_data, avg_time_airline, on=['airline', 'time_of_day_bin'], how='left')
    validation_data = pd.merge(validation_data, avg_day_airline, on=['airline', 'day'], how='left')
    validation_data = pd.merge(validation_data, avg_day_airport, on=['departure_city', 'day'], how='left')
    validation_data = pd.merge(validation_data, average_departure_time_difference, on='airline', how='left')

    # Prepare data for prediction
    classifier_data = validation_data[['airline', 'departure_city', 'destination_city', 
                                       'average_departure_time_difference', 'avg_time_airline', 
                                       'avg_day_airline', 'avg_day_destination']]
    regressor_data = validation_data[['airline', 'departure_city', 'destination_city', 
                                      'average_departure_time_difference', 'avg_time_airline', 
                                      'avg_day_airline', 'avg_day_destination', 'avg_day_airport']]

    # Classifier prediction
    y_proba_new = classifier_model.predict_proba(classifier_data)[:, 1]
    y_pred_classifier = (y_proba_new >= threshold).astype(int)

    # Predict delays based on classifier output
    for i, pred in enumerate(y_pred_classifier):
        departure_city = validation_data.iloc[i]['departure_city']
        destination_city = validation_data.iloc[i]['destination_city']
        airline = validation_data.iloc[i]['airline']
        
        if pred == 1:
            # If a delay is expected, predict the delay time
            regressor_input = regressor_data.iloc[[i]]  # Double brackets ensure it remains a DataFrame
            delay_pred = regressor_model.predict(regressor_input)
            delay_time = delay_pred[0]
            
            # Determine the delay message and associated label
            if delay_time < 10:
                prediction_label = "Short Delay"
                message = f"{airline}'s flight from {departure_city} to {destination_city}: Expect short delays."
                image_path = "images/short_delay_emoji.png"
            elif delay_time < 20:
                prediction_label = "Medium Delay"
                message = f"{airline}'s flight from {departure_city} to {destination_city}: Expect medium delays (10-20 minutes)."
                image_path = "images/medium_delay_emoji.png"
            else:
                prediction_label = "Long Delay"
                message = f"{airline}'s flight from {departure_city} to {destination_city}: Expect long delays."
                image_path = "images/long_delay_emoji.jpg"
            
            # Display the message and image
            st.markdown(f"**{message}**", unsafe_allow_html=True)
            st.image(image_path, width=100)
            
        else:
            prediction_label = "On-Time"
            message = f"{airline}'s flight from {departure_city} to {destination_city}: No delays expected."
            image_path = "images/no_delay_emoji.jpg"
            
            # Display the message and image
            st.markdown(f"**{message}**", unsafe_allow_html=True)
            st.image(image_path, width=100)
        
        # Save the prediction to CSV
        save_prediction_to_csv(validation_data.iloc[[i]], prediction_label)

# Define a function to categorize time of day
def time_of_day_category(departure_time):
    if 5 <= departure_time.hour < 9:
        return 1  # Morning (5 AM - 9 AM)
    elif 9 <= departure_time.hour < 13:
        return 2  # Noon (9 AM - 1 PM)
    elif 13 <= departure_time.hour < 18:
        return 3  # Afternoon (1 PM - 6 PM)
    else:
        return 4  # Evening/Night (6 PM - 5 AM)


# Function to save prediction results to CSV
def save_prediction_to_csv(validation_data, prediction_label):
    # Define the file path for saving predictions
    csv_file = 'previous_searches/saved_predictions.csv'
    
    # Add the prediction label to the validation data
    validation_data['Prediction'] = prediction_label
    
    # Check if the file exists
    file_exists = os.path.exists(csv_file)
    
    # Write to CSV
    validation_data.to_csv(csv_file, mode='a', header=not file_exists, index=False)



def load_saved_predictions():
    csv_file = 'previous_searches/saved_predictions.csv'
    
    try:
        # Load the CSV file into a DataFrame
        saved_data = pd.read_csv(csv_file)
        
        # Select relevant columns and rename them for display
        saved_data = saved_data[['airline', 'departure_city', 'destination_city', 'departure_time_scheduled', 'date_depart', 'Prediction']]
        
        # Rename the columns to the desired display names
        saved_data.columns = ['Airline', 'Departing From', 'Destination', 'Time', 'Date', 'Prediction']
        
        return saved_data
    except FileNotFoundError:
        # Return an empty DataFrame with the desired column headers if the file doesn't exist
        return pd.DataFrame(columns=['Airline', 'Departing From', 'Destination', 'Time', 'Date', 'Prediction'])
