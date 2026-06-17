import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Original Data")
print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Quantity with median
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# Fill missing Price with mean
df['Price'] = df['Price'].fillna(df['Price'].mean())

# Recalculate Sales
df['Sales'] = df['Quantity'] * df['Price']

# Convert date column
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data")
print(df.head())

# -----------------------------
# Reporting
# -----------------------------

# Total Sales
total_sales = df['Sales'].sum()

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()

print("\nTotal Sales:", total_sales)
print("\nSales by Region")
print(region_sales)

# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_report.png")
plt.show()

print("\nReport Generated Successfully!")
