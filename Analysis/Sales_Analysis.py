
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

# Check for duplicate rows
print("Duplicate Rows Before Removal:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()
print("Duplicate Rows After Removal:", df.duplicated().sum())

# Check for missing values
print("\nMissing Values Before Handling:\n", df.isnull().sum())

# Fix for categorical column
df['Item_Type'] = df['Item_Type'].fillna("Unknown")

# Fix for numeric column
df['Order_ID'] = df['Order_ID'].fillna(-1)

print("\nMissing Values After Handling:\n", df.isnull().sum())

print("\nData Types Before Conversion:\n", df.dtypes)


# Convert Order_ID to Integer (fix float issue)

df['Order_ID'] = df['Order_ID'].astype('Int64')  # Uses Pandas nullable integer type

print("\nData Types After Fix:\n", df.dtypes)
'''
# Convert Date column to datetime format

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("\nAfter Conversion:\n", df.dtypes)
'''
# Save the cleaned dataset

new_path = os.path.join(base_dir, "../data/cleaned_sales_data.csv")  # Construct path

df.to_csv(new_path, index=False)

# Load the dataset
df = pd.read_csv(new_path)

'''
# Convert Order_ID to Integer (force conversion)

df['Order_ID'] = df['Order_ID'].astype(int)  # Force conversion to integer

print("\nData Types After Fix:\n", df.dtypes)
'''
