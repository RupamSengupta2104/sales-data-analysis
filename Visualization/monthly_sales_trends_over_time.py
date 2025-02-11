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

# Save the plot BEFORE calling plt.show()
plt.savefig(os.path.join(base_dir, "../images/monthly_sales_trends_over_time.png"), bbox_inches="tight")

# Show the plot
plt.show()
