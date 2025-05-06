import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None

def preprocess_data(data):
    """
    Perform data preprocessing steps.
    """
    # Example: Drop rows with missing values
    data_cleaned = data.dropna()
    return data_cleaned
