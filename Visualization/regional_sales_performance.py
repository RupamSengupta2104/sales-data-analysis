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
# Pivot the data for heatmap
region_pivot = region_sales.pivot("Region", "Total_Units_Sold", "Total_Revenue")

# Create the heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(region_pivot, annot=True, fmt=".0f", cmap="coolwarm", linewidths=0.5)

# Add title
plt.title("Regional Sales Performance")
'''
# Convert Region to index and sort by revenue
region_pivot = region_sales.set_index("Region")[["Total_Revenue"]]

# Create a heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(region_pivot, annot=True, fmt=".0f", cmap="coolwarm", linewidths=0.5)

# Add title
plt.title("Regional Sales Performance")

# Save the plot BEFORE calling plt.show()
plt.savefig(os.path.join(base_dir, "../images/regional_sales_performance.png"), bbox_inches="tight")

# Show the plot
plt.show()