import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

# Get script directory dynamically
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load analyzed sales data
product_sales = pd.read_csv(os.path.join(base_dir, "../data/product_sales.csv"))
region_sales = pd.read_csv(os.path.join(base_dir, "../data/region_sales.csv"))

print("\n Data Loaded Successfully!")

# Create a new Excel workbook
wb = Workbook()

# Create sheets for different reports
ws_product = wb.active  # Default first sheet
ws_product.title = "Product Sales"
ws_region = wb.create_sheet(title="Regional Sales")

# Add headers to Product Sales sheet
ws_product.append(["Product", "Total Units Sold", "Total Revenue"])
for index, row in product_sales.iterrows():
    ws_product.append(row.tolist())

# Add headers to Regional Sales sheet
ws_region.append(["Region", "Total Units Sold", "Total Revenue"])
for index, row in region_sales.iterrows():
    ws_region.append(row.tolist())

# Apply styles to headers (Bold + Centered)
for sheet in [ws_product, ws_region]:
    for cell in sheet[1]:  # First row (headers)
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

# Define output file path
report_path = os.path.join(base_dir, "../reports/Sales_Report.xlsx")

# Ensure reports folder exists
os.makedirs(os.path.dirname(report_path), exist_ok=True)

# Save the report
wb.save(report_path)

print(f"\n Report Generated Successfully: {report_path}")
