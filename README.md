# Sales Profit Prediction & Dashboard

## 📌 Project Overview
This project demonstrates a full **data analysis and machine learning pipeline**:
- Load and clean sales data  
- Analyze trends and insights  
- Visualize interactive charts  
- Predict profit for new orders using a trained model  
- Generate a PDF report  
- Interactive dashboard built with **Streamlit**

---

## 🗂 Folder Structure

Sales Profit Prediction & Dashboard/  
├── data/  
│   ├── raw/ — Original sample CSV files  
│   └── cleaned/ — Cleaned CSV files  
├── notebooks/ — Jupyter notebooks for EDA, feature testing, and model experiments  
├── src/  
│   ├── load.py — Load CSV/Excel/JSON files  
│   ├── clean.py — Clean data  
│   ├── analyse.py — Analyze data  
│   ├── viz.py — Create charts and save to reports/  
│   ├── report.py — Generate PDF report  
│   └── app.py — Streamlit interactive dashboard  
├── reports/ — Charts (PNG) and PDF report  
├── model.pkl — Trained ML model  
├── README.md  
└── requirements.txt

---

## 🔧 Installation

pip install -r requirements.txt


---

## ⚡ Key Features

- **Data Cleaning & Analysis** with Pandas  
- **Visualizations**:  
  - Sales by Category  
  - Sales by State  
  - Monthly Sales Trend  
  - Profit vs Sales Scatter  
- **Machine Learning Model** to predict Profit  
- **PDF Report Generation**  
- **Interactive Streamlit Dashboard**

---

## 🛠 Tech Stack

- Python 3.13  
- Pandas  
- Matplotlib  
- Scikit-learn  
- OpenPyXL  
- FPDF  
- Streamlit  

---

## ▶️ How to Run

1. Go to `src/` folder  
2. Create virtual environment:  
3. Activate venv (PowerShell):  
4. Install dependencies:  
5. Run dashboard:  

---

## 📊 Reports / Charts
All charts and the PDF report are in the `reports/` folder:
- sales_by_category.png  
- sales_by_state.png  
- monthly_sales_trend.png  
- profit_vs_sales.png  
- Sales_Report.pdf  

