import streamlit as st
import pickle
import numpy as np
import pandas as pd


model = pickle.load(open('Linear_model.pkl', 'rb'))


st.title("Tip Amount Prediction")


total_bill = st.number_input('Total Bill', min_value=0, max_value=1000, value=43)
time = st.selectbox('Time', ['Lunch', 'Dinner'])
size = st.number_input('Size', min_value=1, max_value=100, value=2)  


time_encoded = 0 if time == "Lunch" else 1


input_data = pd.DataFrame([[total_bill, time_encoded, size]], 
                          columns=['total_bill', 'time', 'size'])


if st.button('Predict Tips'):
    prediction = model.predict(input_data)
    st.success(f"Predicted Tip: ${prediction[0]:.2f}")
