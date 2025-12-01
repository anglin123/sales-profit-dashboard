import pandas as pd

def analyze_data(df):
    """Perform meaningful business analysis."""
    
    analysis = {}

    # 1. Total sales, profit, quantity
    analysis['total_sales'] = df['Sales'].sum()
    analysis['total_profit'] = df['Profit'].sum()
    analysis['total_quantity'] = df['Quantity'].sum()

    # 2. Sales by category
    analysis['sales_by_category'] = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

    # 3. Sales by state
    analysis['sales_by_state'] = df.groupby('State')['Sales'].sum().sort_values(ascending=False)

    # 4. Top 5 customers
    analysis['top_customers'] = df.groupby('CustomerName')['Sales'].sum().sort_values(ascending=False).head(5)

    # 5. Monthly sales trend
    df['Month'] = df['OrderDate'].dt.to_period('M')
    analysis['monthly_sales'] = df.groupby('Month')['Sales'].sum().sort_values()

    return analysis


if __name__ == "__main__":
    df = pd.read_csv("../data/cleaned/sales_data_cleaned.csv", parse_dates=['OrderDate'])

    results = analyze_data(df)

    print("\n=== ANALYSIS REPORT ===\n")
    for key, value in results.items():
        print(f"\n--- {key.upper()} ---")
        print(value)