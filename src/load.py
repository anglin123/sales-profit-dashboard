import pandas as pd

def load_csv(path):
    """Load CSV file into a pandas DataFrame."""
    return pd.read_csv(path)

def load_excel(path, sheet_name=0):
    """Load Excel file."""
    return pd.read_excel(path, sheet_name=sheet_name)

def load_json(path):
    """Load JSON file."""
    return pd.read_json(path)

if __name__ == "__main__":
    # Change filename here based on your data
    df = load_csv("../data/raw/sales_data.csv")
    print("Loaded data:")
    print(df.head())
