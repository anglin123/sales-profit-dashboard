import pandas as pd

def clean_data(df):
    """Clean the dataset: fix missing values, remove duplicates, convert types."""

    # 1. Remove duplicate rows
    df = df.drop_duplicates()

    # 2. Handle missing values
    df['Sales'] = df['Sales'].fillna(0)
    df['Quantity'] = df['Quantity'].fillna(0)
    df['Profit'] = df['Profit'].fillna(0)
    df['Category'] = df['Category'].fillna("Unknown")

    # 3. Convert dates
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

    # 4. Remove rows with invalid dates
    df = df.dropna(subset=['OrderDate'])

    return df


if __name__ == "__main__":
    # Load raw data
    df = pd.read_csv("../data/raw/sales_data.csv")

    # Clean
    cleaned_df = clean_data(df)

    # Save cleaned data
    cleaned_df.to_csv("../data/cleaned/sales_data_cleaned.csv", index=False)

    print("Cleaning complete! Saved to data/cleaned/")
    print(cleaned_df.head())
