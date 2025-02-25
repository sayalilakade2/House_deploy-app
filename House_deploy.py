import pickle
import numpy as np
import streamlit as st
import requests
import joblib



# Load the model
#loaded_model = pickle.load(open(r"https://github.com/sayalilakade2/House_deploy-app/raw/main/finalized_model.sav", 'rb'))
# Load the model
model_url = "https://github.com/sayalilakade2/House_deploy-app/raw/main/finalized_model.sav"
r = requests.get(model_url)

if r.status_code == 200:
    with open('finalized_model.sav', 'wb') as f:
        f.write(r.content)
else:
    print("Failed to download the model file")

model = joblib.load('finalized_model.sav')


def DecisionTreeRegressor(input_data):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1, -1) 
    prediction = model.predict(input_data_reshaped)
    return prediction

def predict_price(entries):
    try:
        # Get user input
        input_data = [int(entries[0]), float(entries[1]), int(entries[2]), int(entries[3]), 
                      float(entries[4]), int(entries[5]), int(entries[6]), int(entries[7]), 
                      int(entries[8]), int(entries[9]), int(entries[10]), int(entries[11])]
        
        # Perform prediction
        predicted_price = DecisionTreeRegressor(input_data)[0]
        return f"The predicted price is ${predicted_price:,.2f}"
    except ValueError:
        return "Please enter valid inputs."

        
 


def main():
    st.title("House Price Prediction")
    entries = []
    for feature in ['Bedrooms:', 'Bathrooms:', 'Sqft Living:', 'Sqft Lot:', 'Floors:', 
                    'Waterfront:', 'View:', 'Condition:', 'Sqft Above:', 'Sqft Basement:', 
                    'Year Built:', 'Year Renovated:']:
        entries.append(st.number_input(feature))
    
    if st.button('Predict Price'):
        result = predict_price(entries)
        st.success(result)

if __name__ == '__main__':
    main()


