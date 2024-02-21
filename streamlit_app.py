import tkinter as tk
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

# Load the dataset
data = pd.read_csv('House.csv')

# Extract features and target variable
X = data[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 
          'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement', 
          'yr_built', 'yr_renovated']]
y = data['price']

# Train the regression model
model = DecisionTreeRegressor()  # Instantiate DecisionTreeRegressor
model.fit(X, y)  # Call fit() on the instantiated model

def predict_price():
    try:
        # Get user input
        bedrooms = int(entries[0].get())
        bathrooms = float(entries[1].get())
        sqft_living = int(entries[2].get())
        sqft_lot = int(entries[3].get())
        floors = float(entries[4].get())
        waterfront = int(entries[5].get())
        view = int(entries[6].get())
        condition = int(entries[7].get())
        sqft_above = int(entries[8].get())
        sqft_basement = int(entries[9].get())
        yr_built = int(entries[10].get())
        yr_renovated =int(entries[11].get())
        
        # Perform prediction
        predicted_price = model.predict([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, 
                                           waterfront, view, condition, sqft_above, sqft_basement, 
                                           yr_built, yr_renovated]])[0]
        result_label.config(text=f"The predicted price is ${predicted_price:,.2f}")
    except ValueError:
        result_label.config(text="Please enter valid inputs.")

# Create GUI window
window = tk.Tk()
window.title("House Price Prediction")

# Create labels and entry fields for user input
labels = ['Bedrooms:', 'Bathrooms:', 'Sqft Living:', 'Sqft Lot:', 'Floors:', 
          'Waterfront:', 'View:', 'Condition:', 'Sqft Above:', 'Sqft Basement:', 
          'Year Built:', 'Year Renovated:']

entries = []
for i, label_text in enumerate(labels):
    tk.Label(window, text=label_text).grid(row=i, column=0)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1)
    entries.append(entry)

# Create a button to trigger prediction
predict_button = tk.Button(window, text="Predict Price", command=predict_price)
predict_button.grid(row=len(labels), columnspan=2)


# Create label to display prediction result
result_label = tk.Label(window, text="")
result_label.grid(row=len(labels)+1, columnspan=2)

window.mainloop()




