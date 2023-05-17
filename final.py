import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data into a pandas DataFrame
data = {
    'Highest Temperature': [25, 26, 24, 27, 25, 26, 24, 27, 25, 26, 24, 27, 25, 26, 24, 27],
    'Lowest Temperature': [10, 12, 11, 13, 10, 12, 11, 13, 10, 12, 11, 13, 10, 12, 11, 13],
    'Rainfall': [400, 380, 410, 390, 400, 380, 410, 390, 400, 380, 410, 390, 400, 380, 410, 390],
    'Humidity': [60, 62, 58, 63, 60, 62, 58, 63, 60, 62, 58, 63, 60, 62, 58, 63],
    'Crop Yield': [2500, 2550, 2450, 2600, 2500, 2550, 2450, 2600, 2500, 2550, 2450, 2600, 2500, 2550, 2450, 2600],
    'Irrigation Frequency': [15, 16, 14, 17, 15, 16, 14, 17, 15, 16, 14, 17, 15, 16, 14, 17]
}

df = pd.DataFrame(data)

# Separate the features and target variables
X = df[['Highest Temperature', 'Lowest Temperature', 'Rainfall', 'Humidity']]
y_yield = df['Crop Yield']
y_irrigation = df['Irrigation Frequency']

# Split the data into training and testing sets
X_train, X_test, y_yield_train, y_yield_test, y_irrigation_train, y_irrigation_test = train_test_split(X, y_yield, y_irrigation, test_size=0.2, random_state=42)

# Train the random forest model for Crop Yield prediction
yield_model = RandomForestRegressor(n_estimators=100, random_state=42)
yield_model.fit(X_train, y_yield_train)

# Train the random forest model for Irrigation Frequency prediction
irrigation_model = RandomForestRegressor(n_estimators=100, random_state=42)
irrigation_model.fit(X_train, y_irrigation_train)

# New data for prediction
new_data = {
    'Highest Temperature': [26],
    'Lowest Temperature': [12],
    'Rainfall': [380],
    'Humidity': [62]
}

# Convert the new data to a DataFrame
new_df = pd.DataFrame(new_data)

# Make predictions for Crop Yield and Irrigation Frequency
yield_prediction = yield_model.predict(new_df)
irrigation_prediction = irrigation_model.predict(new_df)

print("Crop Yield Prediction:", yield_prediction[0])
print("Irrigation Frequency Prediction:", irrigation_prediction[0])

