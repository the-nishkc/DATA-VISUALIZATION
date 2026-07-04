# Data Visualization using Matplotlib


import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv("supermarket_sales_cleaned.csv")
plt.style.use("ggplot")

# 1. Monthly Sales Trend (Line Chart)

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly_sales = (
    df.groupby("month")["total"]
      .sum()
      .reindex(month_order)
      .dropna()
)

plt.figure(figsize=(11,5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o',
    linewidth=3
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=25)
plt.grid(alpha=.3)

plt.tight_layout()
plt.savefig("01_monthly_sales.png",dpi=300)
plt.show()

# 2. Revenue by Product Line

product_sales = (
    df.groupby("product_line")["total"]
      .sum()
      .sort_values()
)

plt.figure(figsize=(10,6))

plt.barh(
    product_sales.index,
    product_sales.values
)

plt.title("Revenue by Product Line")
plt.xlabel("Revenue")
plt.ylabel("Product Line")

plt.tight_layout()
plt.savefig("02_product_line.png",dpi=300)
plt.show()

# 3. Customer Type Distribution

customer = df["customer_type"].value_counts()
plt.figure(figsize=(7,7))
plt.pie(
    customer.values,
    labels=customer.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Type Distribution")
plt.savefig("03_customer_type.png",dpi=300)
plt.show()

# 4. Payment Method

payment = df["payment"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    payment.values,
    labels=payment.index,
    autopct="%1.1f%%",
    wedgeprops={"width":0.6},
    startangle=90
)
plt.title("Payment Method Share")
plt.savefig("04_payment.png",dpi=300)
plt.show()

# 5. Sales Distribution

plt.figure(figsize=(9,5))
plt.hist(
    df["total"],
    bins=25
)

plt.title("Distribution of Total Sales")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("05_sales_distribution.png",dpi=300)
plt.show()

# 6. Rating vs Total Purchase

plt.figure(figsize=(8,6))
plt.scatter(
    df["rating"],
    df["total"],
    alpha=.7
)
plt.title("Customer Rating vs Purchase Amount")
plt.xlabel("Rating")
plt.ylabel("Total Purchase")
plt.tight_layout()
plt.savefig("06_rating_vs_total.png",dpi=300)
plt.show()
