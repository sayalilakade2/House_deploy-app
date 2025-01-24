import pickle
import numpy as np
import streamlit as st
import requests
import joblib
import os

# Ensure correct protobuf version is installed
os.system("pip install protobuf==3.20.*")
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Download the model file if it doesn't already exist
model_filename = "finalized_model.sav"
model_url = "https://github.com/sayalilakade2/House_deploy-app/raw/main/finalized_model.sav"

if not os.path.exists(model_filename):
    r = requests.get(model_url)
    if r.status_code == 200:
        with open(model_filename, 'wb') as f:
            f.write(r.content)
    else:
        st.error("Failed to download the model file. Please check the URL or internet connection.")

# Load the model
try:
    model = joblib.load(model_filename)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Function to predict using the Decision Tree Regressor
def DecisionTreeRegressor(input_data):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    return prediction

# Streamlit app for house price prediction
def main():
    st.title("House Price Prediction App")
    st.write("Enter the details of the house to predict its price:")

    # Create input fields for user data
    entries = []
    features = [
        'Bedrooms', 'Bathrooms', 'Sqft Living', 'Sqft Lot', 'Floors', 
        'Waterfront', 'View', 'Condition', 'Sqft Above', 'Sqft Basement', 
        'Year Built', 'Year Renovated'
    ]
    
    for feature in features:
        if feature in ['Bedrooms', 'Bathrooms', 'Floors', 'Waterfront', 'View', 'Condition', 'Year Built', 'Year Renovated']:
            entries.append(st.number_input(feature, step=1, value=0))
        else:
            entries.append(st.number_input(feature, step=0.1, value=0.0))
    
    # Predict button
    if st.button('Predict Price'):
        try:
            predicted_price = DecisionTreeRegressor(entries)[0]
            st.success(f"The predicted price is ${predicted_price:,.2f}")
        except ValueError as e:
            st.error(f"Error during prediction: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()

