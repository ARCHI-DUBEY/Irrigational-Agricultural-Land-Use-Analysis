import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column):
    """
    Plot a histogram for a specified column.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
