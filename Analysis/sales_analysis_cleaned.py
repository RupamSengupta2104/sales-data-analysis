import os
import pandas as pd

# Get the script directory dynamically
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/cleaned_sales_data.csv")  # Load cleaned dataset

# Read the cleaned CSV file
df = pd.read_csv(file_path)
'''
# Convert 'Order_Date' to datetime format (if not already converted)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

Order_Date contains dates in multiple formats, and pd.to_datetime() is unable to automatically parse them all 
correctly

'''
# Convert 'Order_Date' to datetime (handling different formats)
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True, errors='coerce')

# Convert 'Ship_Date' to datetime (handling different formats)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True, errors='coerce')

# Check if any dates failed to convert
print("\nMissing Dates After Conversion:")
print(df[['Order_Date', 'Ship_Date']].isnull().sum())

# Fix missing Order_Date values by assigning the minimum available date
df['Order_Date'] = df['Order_Date'].fillna(df['Order_Date'].min())

# Fix missing Ship_Date values by assigning the median available date
df['Ship_Date'] = df['Ship_Date'].fillna(df['Ship_Date'].median())

# Verify missing dates are handled
print("\nFinal Missing Dates Check:")
print(df[['Order_Date', 'Ship_Date']].isnull().sum())


