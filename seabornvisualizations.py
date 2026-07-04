# Seaborn Visualizations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("supermarket_sales_cleaned.csv")

# Professional plot style

sns.set_theme(style="whitegrid", context="talk")

# 1. Correlation Heatmap

numeric_columns = [
    "unit_price",
    "quantity",
    "tax_5%",
    "total",
    "cogs",
    "gross_income",
    "rating"
]
corr = df[numeric_columns].corr()
plt.figure(figsize=(10,8))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=.5,
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("01_correlation_heatmap.png", dpi=300)
plt.show()

# 2. Pairplot

pairplot_columns = [
    "unit_price",
    "quantity",
    "total",
    "rating"
]
pair = sns.pairplot(
    df[pairplot_columns],
    corner=True,
    diag_kind="hist"
)
pair.fig.suptitle(
    "Pairwise Relationship Between Numerical Features",
    y=0.98
)
pair.savefig("02_pairplot.png", dpi=100)
plt.show()

# 3. Boxen Plot

plt.figure(figsize=(12,6))
sns.boxenplot(
    data=df,
    x="product_line",
    y="total"
)
plt.title("Sales Distribution Across Product Lines")
plt.xlabel("Product Line")
plt.ylabel("Transaction Amount")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("03_boxen_plot.png", dpi=300)
plt.show()

# 4. FacetGrid

facet = sns.FacetGrid(
    df,
    col="gender",
    hue="customer_type",
    height=5,
    aspect=1
)
facet.map(
    sns.histplot,
    "total",
    bins=20
)
facet.add_legend()
facet.fig.suptitle(
    "Purchase Distribution by Gender and Customer Type",
    y=1.00
)
facet.savefig("04_facetgrid.png", dpi=300)
plt.show()

# 5. Violin Plot

plt.figure(figsize=(10,6))
sns.violinplot(
    data=df,
    x="payment",
    y="total"
)
plt.title("Transaction Amount by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.savefig("05_violin_plot.png", dpi=300)
plt.show()

# 6. Count Plot

plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="branch"
)
plt.title("Number of Transactions by Branch")
plt.xlabel("Branch")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("06_countplot_branch.png", dpi=300)
plt.show()

# 7. Regression Plot

plt.figure(figsize=(8,6))
sns.regplot(
    data=df,
    x="rating",
    y="total",
    scatter_kws={"alpha":0.5}
)
plt.title("Relationship Between Rating and Purchase Amount")
plt.xlabel("Customer Rating")
plt.ylabel("Total Purchase")
plt.tight_layout()
plt.savefig("07_regression_plot.png", dpi=300)
plt.show()

# 8. Box Plot

plt.figure(figsize=(10,6))
sns.boxplot(
    data=df,
    x="city",
    y="total"
)
plt.title("Sales Distribution by City")
plt.xlabel("City")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.savefig("08_boxplot_city.png", dpi=300)
plt.show()
