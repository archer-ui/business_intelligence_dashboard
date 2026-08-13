import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD PROCESSED DATASET
# ============================================================

DATA_FOLDER = Path("Data")

processed_files = list(DATA_FOLDER.glob("processed*"))

if not processed_files:
    st.error(
        "Processed dataset not found. Make sure your processed dataset "
        "is inside the Data folder and its name starts with 'processed'."
    )
    st.stop()

data_file = processed_files[0]

if data_file.suffix.lower() in [".xlsx", ".xls"]:
    df = pd.read_excel(data_file)
elif data_file.suffix.lower() == ".csv":
    df = pd.read_csv(data_file)
else:
    st.error("The processed dataset must be an Excel or CSV file.")
    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

# Convert Order Date to datetime
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

# Create Profit Margin if it does not already exist
if "Profit Margin Percentage" not in df.columns:
    df["Profit Margin Percentage"] = (
        df["Profit"] / df["Sales"] * 100
    ).replace([float("inf"), -float("inf")], 0).fillna(0)


# ============================================================
# TITLE
# ============================================================

st.title("Business Intelligence Dashboard")
st.markdown(
    "### Interactive Visual Analytics System"
)

st.markdown(
    "This dashboard integrates the data preparation, "
    "feature engineering and visual analysis developed "
    "through the previous milestones."
)

st.divider()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Dashboard Filters")

# Region filter
regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)

# Category filter
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = (
    filtered_df["Order ID"].nunique()
    if "Order ID" in filtered_df.columns
    else len(filtered_df)
)

average_profit_margin = filtered_df[
    "Profit Margin Percentage"
].mean()


# ============================================================
# KPI DISPLAY
# ============================================================

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

with col3:
    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )

with col4:
    st.metric(
        "Avg. Profit Margin",
        f"{average_profit_margin:.2f}%"
    )


st.divider()


# ============================================================
# SALES BY CATEGORY
# ============================================================

st.subheader("Sales Performance by Category")

sales_category = (
    filtered_df
    .groupby("Category", as_index=False)["Sales"]
    .sum()
)

fig_category = px.bar(
    sales_category,
    x="Category",
    y="Sales",
    title="Total Sales by Category",
    text_auto=".2s"
)

fig_category.update_layout(
    xaxis_title="Product Category",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)


# ============================================================
# SALES BY REGION
# ============================================================

st.subheader("Regional Sales Performance")

sales_region = (
    filtered_df
    .groupby("Region", as_index=False)["Sales"]
    .sum()
)

fig_region = px.bar(
    sales_region,
    x="Region",
    y="Sales",
    title="Total Sales by Region",
    text_auto=".2s"
)

fig_region.update_layout(
    xaxis_title="Region",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)


# ============================================================
# PROFIT BY CATEGORY
# ============================================================

st.subheader("Profitability by Category")

profit_category = (
    filtered_df
    .groupby("Category", as_index=False)["Profit"]
    .sum()
)

fig_profit = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    title="Total Profit by Category",
    text_auto=".2s"
)

fig_profit.update_layout(
    xaxis_title="Product Category",
    yaxis_title="Profit"
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)


# ============================================================
# SALES TREND OVER TIME
# ============================================================

if "Order Date" in filtered_df.columns:

    st.subheader("Sales Trend Over Time")

    sales_time = (
        filtered_df
        .dropna(subset=["Order Date"])
        .groupby("Order Date", as_index=False)["Sales"]
        .sum()
    )

    fig_time = px.line(
        sales_time,
        x="Order Date",
        y="Sales",
        title="Sales Trend Over Time"
    )

    fig_time.update_layout(
        xaxis_title="Order Date",
        yaxis_title="Sales"
    )

    st.plotly_chart(
        fig_time,
        use_container_width=True
    )


# ============================================================
# SALES CATEGORY ANALYSIS
# ============================================================

if "Sales Category" in filtered_df.columns:

    st.subheader("Sales Transaction Categories")

    sales_category_count = (
        filtered_df["Sales Category"]
        .value_counts()
        .reset_index()
    )

    sales_category_count.columns = [
        "Sales Category",
        "Number of Transactions"
    ]

    fig_sales_class = px.pie(
        sales_category_count,
        names="Sales Category",
        values="Number of Transactions",
        title="Distribution of Sales Categories"
    )

    st.plotly_chart(
        fig_sales_class,
        use_container_width=True
    )


# ============================================================
# DECISION SUPPORT
# ============================================================

st.divider()

st.subheader("Decision-Support Insights")

if not filtered_df.empty:

    best_category = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    best_region = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    most_profitable_category = (
        filtered_df
        .groupby("Category")["Profit"]
        .sum()
        .idxmax()
    )

    st.write(
        f"**Highest Sales Category:** {best_category}"
    )

    st.write(
        f"**Highest Sales Region:** {best_region}"
    )

    st.write(
        f"**Most Profitable Category:** "
        f"{most_profitable_category}"
    )

    st.write(
        "These indicators can support decisions concerning "
        "resource allocation, product strategy and regional performance."
    )


# ============================================================
# DATA PREVIEW
# ============================================================

st.divider()

with st.expander("View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

st.caption(
    "Business Intelligence Dashboard — Milestone 5"
)