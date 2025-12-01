import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt

# Load trained model
with open("../model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Sales Profit Prediction & Dashboard")

# Upload new data
uploaded_file = st.file_uploader("Upload CSV with Sales & Quantity", type="csv")

if uploaded_file:
    new_data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.write(new_data)

    if 'Sales' in new_data.columns and 'Quantity' in new_data.columns:
        X_new = new_data[['Sales', 'Quantity']]
        new_data['Predicted_Profit'] = model.predict(X_new)
        st.subheader("Predicted Profit")
        st.write(new_data[['Sales','Quantity','Predicted_Profit']])
    else:
        st.error("CSV must have columns: Sales, Quantity")

# Show pre-made charts
st.subheader("Visualizations")
chart_files = [
    "../reports/sales_by_category.png",
    "../reports/sales_by_state.png",
    "../reports/monthly_sales_trend.png",
    "../reports/profit_vs_sales.png"
]

for chart in chart_files:
    st.image(chart, use_container_width=True)
