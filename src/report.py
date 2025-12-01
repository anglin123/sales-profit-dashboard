import pandas as pd
from fpdf import FPDF
import os

# Load cleaned data
df = pd.read_csv("../data/cleaned/sales_data_cleaned.csv", parse_dates=['OrderDate'])

# Calculate key metrics
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()

top_customers = df.groupby('CustomerName')['Sales'].sum().sort_values(ascending=False).head(5)
sales_by_category = df.groupby('Category')['Sales'].sum()
sales_by_state = df.groupby('State')['Sales'].sum()
df['Month'] = df['OrderDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Create reports folder if not exists
os.makedirs("../reports", exist_ok=True)

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Sales Analysis Report", ln=True, align="C")

# Add key metrics
pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Sales: ${total_sales:.2f}", ln=True)
pdf.cell(0, 10, f"Total Profit: ${total_profit:.2f}", ln=True)
pdf.cell(0, 10, f"Total Quantity Sold: {total_quantity}", ln=True)

# Add charts
chart_files = [
    "sales_by_category.png",
    "sales_by_state.png",
    "monthly_sales_trend.png",
    "profit_vs_sales.png"
]

for chart in chart_files:
    pdf.add_page()
    pdf.image(f"../reports/{chart}", w=180)

# Save PDF
pdf.output("../reports/Sales_Report.pdf")
print("PDF report generated at ../reports/Sales_Report.pdf")
