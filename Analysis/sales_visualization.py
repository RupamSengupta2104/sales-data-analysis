import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the script directory dynamically
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the processed datasets
product_sales = pd.read_csv(os.path.join(base_dir, "../data/product_sales.csv"))
top_products = pd.read_csv(os.path.join(base_dir, "../data/top_products.csv"))
region_sales = pd.read_csv(os.path.join(base_dir, "../data/region_sales.csv"))
monthly_sales = pd.read_csv(os.path.join(base_dir, "../data/monthly_sales.csv"))
'''
# Preview data
print("\n Data Loaded for Visualization!")
print(product_sales.head())
'''
'''
# Set the style
sns.set_style("whitegrid")

# Create the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Total_Sales", y="Item_Type", data=top_products, palette="viridis")

# Add labels and title
plt.xlabel("Total Units Sold")
plt.ylabel("Product Type")
plt.title("Best-Selling Products (By Units Sold)")

# Show the plot
plt.show()


# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(product_sales["Total_Revenue"], labels=product_sales["Item_Type"], autopct="%1.1f%%", colors=sns.color_palette("pastel"))

# Add title
plt.title("Revenue Distribution by Product Type")

# Show the plot
plt.show()


# Convert 'YearMonth' to datetime format
monthly_sales["YearMonth"] = pd.to_datetime(monthly_sales["YearMonth"])

# Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(x="YearMonth", y="Total_Units_Sold", data=monthly_sales, marker="o", color="b")

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Total Units Sold")
plt.title("Monthly Sales Trends Over Time")

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Show the plot
plt.show()
'''
'''
# Pivot the data for heatmap
region_pivot = region_sales.pivot("Region", "Total_Units_Sold", "Total_Revenue")

# Create the heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(region_pivot, annot=True, fmt=".0f", cmap="coolwarm", linewidths=0.5)

# Add title
plt.title("Regional Sales Performance")

# Show the plot
plt.show()
'''
'''
# Convert Region to index and sort by revenue
region_pivot = region_sales.set_index("Region")[["Total_Revenue"]]

# Create a heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(region_pivot, annot=True, fmt=".0f", cmap="coolwarm", linewidths=0.5)

# Add title
plt.title("Regional Sales Performance")

# Show the plot
plt.show()
'''

# Create the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Total_Sales", y="Item_Type", data=top_products, palette="viridis")

# Add labels and title
plt.xlabel("Total Units Sold")
plt.ylabel("Product Type")
plt.title("Best-Selling Products (By Units Sold)")

# Save the plot BEFORE calling plt.show()
plt.savefig(os.path.join(base_dir, "../images/best_selling_products.png"), bbox_inches="tight")

# Show the plot
plt.show()
