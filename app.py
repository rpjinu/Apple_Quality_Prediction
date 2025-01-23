import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\project_vs\Apple_Quantity_detection\model.pkl")

# Streamlit app title
st.title("🍎 Apple Quality Prediction")

# Input fields for user
st.header("Enter Apple Features")

# Create input fields for each feature
size = st.number_input("Size", value=-0.5)
weight = st.number_input("Weight", value=-1.0)
sweetness = st.number_input("Sweetness", value=0.0)
crunchiness = st.number_input("Crunchiness", value=1.0)
juiciness = st.number_input("Juiciness", value=0.5)
ripeness = st.number_input("Ripeness", value=0.5)
acidity = st.number_input("Acidity", value=0.5)

# Button to make predictions
if st.button("Predict Quality"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        'Size': [size],
        'Weight': [weight],
        'Sweetness': [sweetness],
        'Crunchiness': [crunchiness],
        'Juiciness': [juiciness],
        'Ripeness': [ripeness],
        'Acidity': [acidity]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Extract the prediction value from the array
    prediction_value = prediction[0]

    # Map the prediction to a label
    if prediction_value == 1:
        quality_label = "Good"
    else:
        quality_label = "Bad"

    # Display the result
    st.success(f"Predicted Quality: **{quality_label}**")