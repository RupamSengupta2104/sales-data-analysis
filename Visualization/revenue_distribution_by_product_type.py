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

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(product_sales["Total_Revenue"], labels=product_sales["Item_Type"], autopct="%1.1f%%", colors=sns.color_palette("pastel"))

# Add title
plt.title("Revenue Distribution by Product Type")

# Save the plot BEFORE calling plt.show()
plt.savefig(os.path.join(base_dir, "../images/revenue_distribution_by_product_type.png"), bbox_inches="tight")

# Show the plot
plt.show()