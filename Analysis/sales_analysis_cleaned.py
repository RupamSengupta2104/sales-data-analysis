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

# Group by 'Item_Type' to calculate total sales & revenue
product_sales = df.groupby('Item_Type').agg(
    Total_Units_Sold=('Units_Sold', 'sum'),
    Total_Revenue=('Unit_SellingPrice', 'sum')
).reset_index()

# Sort by highest revenue
product_sales = product_sales.sort_values(by='Total_Revenue', ascending=False)

# Print results
print("\n Total Sales & Revenue Per Product:")
print(product_sales)

# Find top-selling products (based on total units sold)
top_products = df.groupby('Item_Type').agg(
    Total_Sales=('Units_Sold', 'sum')
).reset_index().sort_values(by='Total_Sales', ascending=False)

# Print top products
print("\n Best-Selling Products (By Units Sold):")
print(top_products.head(5))  # Show top 5

# Group sales data by Region
region_sales = df.groupby('Region').agg(
    Total_Units_Sold=('Units_Sold', 'sum'),
    Total_Revenue=('Unit_SellingPrice', 'sum')
).reset_index().sort_values(by='Total_Revenue', ascending=False)

# Print regional sales
print("\n Regional Sales Performance:")
print(region_sales)

# Extract Month & Year
df['YearMonth'] = df['Order_Date'].dt.to_period('M')

# Group by Month & Year to see trends
monthly_sales = df.groupby('YearMonth').agg(
    Total_Units_Sold=('Units_Sold', 'sum'),
    Total_Revenue=('Unit_SellingPrice', 'sum')
).reset_index()

# Print monthly sales trend
print("\n Monthly Sales Trends:")
print(monthly_sales)

# Ensure the 'data' folder exists before saving files
data_dir = os.path.join(base_dir, "../data")
os.makedirs(data_dir, exist_ok=True)  # ✅ Create folder if it doesn't exist

# Define file paths dynamically
product_sales_path = os.path.join(data_dir, "product_sales.csv")
top_products_path = os.path.join(data_dir, "top_products.csv")
region_sales_path = os.path.join(data_dir, "region_sales.csv")
monthly_sales_path = os.path.join(data_dir, "monthly_sales.csv")

# Save the analysis results
product_sales.to_csv(product_sales_path, index=False)
top_products.to_csv(top_products_path, index=False)
region_sales.to_csv(region_sales_path, index=False)
monthly_sales.to_csv(monthly_sales_path, index=False)

print("\n✅ Analysis Completed! Results saved successfully in 'data/' folder.")