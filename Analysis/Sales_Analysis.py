import os
import pandas as pd

# Get the absolute path dynamically (works on any system)
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
file_path = os.path.join(base_dir, "../data/sales_data.csv")  # Construct path

# Load the dataset
df = pd.read_csv(file_path)

# Show the first few rows
print(df.head())
# Get general information about the dataset
print(df.info())
# Check for missing values
print(df.isnull().sum())
# Get summary statistics
print(df.describe())
