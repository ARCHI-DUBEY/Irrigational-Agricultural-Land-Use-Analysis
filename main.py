from data_preprocessing import load_data, preprocess_data
from eda import plot_histogram

def main():
    file_path = 'data/data.csv'  # Update with your actual file path
    data = load_data(file_path)
    if data is not None:
        data_cleaned = preprocess_data(data)
        plot_histogram(data_cleaned, 'column_name')  # Replace 'column_name' with your actual column

if __name__ == "__main__":
    main()
