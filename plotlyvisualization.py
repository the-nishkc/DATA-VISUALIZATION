# Plotly Interactive Visualizations

import pandas as pd
import plotly.express as px

# Load Dataset

df = pd.read_csv("supermarket_sales_cleaned.csv")

# Professional Plotly Theme
TEMPLATE = "plotly_white"


# 1. Interactive Monthly Sales Trend


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
      .reset_index()
)

fig = px.line(
    monthly_sales,
    x="month",
    y="total",
    title="Interactive Monthly Revenue Trend",
    markers=True,
    template=TEMPLATE
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue",
    hovermode="x unified"
)

fig.write_html("01_monthly_sales.html")

fig.show()


# 2. Product Line Revenue


product_sales = (
    df.groupby("product_line")["total"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

fig = px.bar(
    product_sales,
    x="product_line",
    y="total",
    color="total",
    title="Revenue by Product Line",
    template=TEMPLATE
)

fig.update_layout(
    xaxis_title="Product Line",
    yaxis_title="Revenue"
)

fig.write_html("02_product_line.html")

fig.show()


# 3. Treemap


fig = px.treemap(
    df,
    path=["city","branch","product_line"],
    values="total",
    color="gross_income",
    title="Revenue Hierarchy",
    template=TEMPLATE
)

fig.write_html("03_treemap.html")

fig.show()


# 4. Sunburst Chart


fig = px.sunburst(
    df,
    path=["city","branch","customer_type"],
    values="total",
    color="rating",
    title="Customer Distribution by City and Branch",
    template=TEMPLATE
)

fig.write_html("04_sunburst.html")

fig.show()


# 5. Interactive Scatter Plot


fig = px.scatter(
    df,
    x="rating",
    y="total",
    color="payment",
    size="quantity",
    hover_data=[
        "city",
        "branch",
        "product_line",
        "customer_type"
    ],
    title="Customer Rating vs Purchase Amount",
    template=TEMPLATE
)

fig.update_layout(
    xaxis_title="Customer Rating",
    yaxis_title="Total Purchase"
)

fig.write_html("05_scatter.html")

fig.show()


# 6. Interactive Box Plot


fig = px.box(
    df,
    x="payment",
    y="total",
    color="payment",
    points="all",
    title="Transaction Distribution by Payment Method",
    template=TEMPLATE
)

fig.update_layout(
    xaxis_title="Payment Method",
    yaxis_title="Transaction Amount"
)

fig.write_html("06_boxplot.html")

fig.show()
