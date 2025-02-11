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

# Set the style
sns.set_style("whitegrid")

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