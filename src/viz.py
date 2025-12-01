import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder if it doesn't exist
os.makedirs("../reports", exist_ok=True)

def visualize():
    # Load cleaned data
    df = pd.read_csv("../data/cleaned/sales_data_cleaned.csv", parse_dates=['OrderDate'])

    # 1️⃣ Sales by Category
    category_sales = df.groupby('Category')['Sales'].sum()
    category_sales.plot(kind='bar', title='Sales by Category')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('../reports/sales_by_category.png')
    plt.close()

    # 2️⃣ Sales by State
    state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
    state_sales.plot(kind='bar', title='Sales by State', color='orange')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('../reports/sales_by_state.png')
    plt.close()

    # 3️⃣ Monthly Sales Trend
    df['Month'] = df['OrderDate'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum()
    monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('../reports/monthly_sales_trend.png')
    plt.close()

    # 4️⃣ Profit vs Sales Scatter
    df.plot(kind='scatter', x='Sales', y='Profit', title='Profit vs Sales', color='green')
    plt.tight_layout()
    plt.savefig('../reports/profit_vs_sales.png')
    plt.close()

    print("All charts saved in ../reports/ folder.")

if __name__ == "__main__":
    visualize()
