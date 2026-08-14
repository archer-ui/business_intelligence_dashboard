import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Business Intelligence Dashboard - M6",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

# Find the project root from the location of this file.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

data_file = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "sampledata_processed.csv"
)

# Fallback for the previous project structure.
if not data_file.exists():
    data_file = (
        PROJECT_ROOT
        / "Data"
        / "sampledata_processed.csv"
    )

if not data_file.exists():
    st.error(
        f"Dataset not found.\n\nExpected location:\n{data_file}"
    )
    st.stop()


@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)


df = load_data(data_file)


# ============================================================
# DATA PREPARATION
# ============================================================

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

if "Sales" in df.columns:
    df["Sales"] = pd.to_numeric(
        df["Sales"],
        errors="coerce"
    )

if "Profit" in df.columns:
    df["Profit"] = pd.to_numeric(
        df["Profit"],
        errors="coerce"
    )

if "Profit Margin Percentage" not in df.columns:
    df["Profit Margin Percentage"] = (
        df["Profit"] / df["Sales"] * 100
    )

df["Profit Margin Percentage"] = (
    df["Profit Margin Percentage"]
    .replace([float("inf"), -float("inf")], 0)
    .fillna(0)
)


# ============================================================
# DASHBOARD TITLE
# ============================================================

st.title("Business Intelligence Dashboard")

st.markdown(
    "### Interactive Visual Analytics System"
)

st.markdown(
    "This dashboard integrates the analytical work from "
    "Milestones 1–5 and introduces an advanced visual "
    "analytics contribution developed for Milestone 6."
)

st.divider()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Dashboard Filters")

filtered_df = df.copy()


# Region
if "Region" in df.columns:

    regions = ["All"] + sorted(
        df["Region"].dropna().unique().tolist()
    )

    selected_region = st.sidebar.selectbox(
        "Select Region",
        regions
    )

    if selected_region != "All":
        filtered_df = filtered_df[
            filtered_df["Region"] == selected_region
        ]


# Category
if "Category" in df.columns:

    categories = ["All"] + sorted(
        df["Category"].dropna().unique().tolist()
    )

    selected_category = st.sidebar.selectbox(
        "Select Category",
        categories
    )

    if selected_category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]


# Segment
if "Segment" in df.columns:

    segments = ["All"] + sorted(
        df["Segment"].dropna().unique().tolist()
    )

    selected_segment = st.sidebar.selectbox(
        "Select Segment",
        segments
    )

    if selected_segment != "All":
        filtered_df = filtered_df[
            filtered_df["Segment"] == selected_segment
        ]


# Ship Mode
if "Ship Mode" in df.columns:

    ship_modes = ["All"] + sorted(
        df["Ship Mode"].dropna().unique().tolist()
    )

    selected_ship_mode = st.sidebar.selectbox(
        "Select Ship Mode",
        ship_modes
    )

    if selected_ship_mode != "All":
        filtered_df = filtered_df[
            filtered_df["Ship Mode"] == selected_ship_mode
        ]


# Date Range
if "Order Date" in df.columns:

    valid_dates = df["Order Date"].dropna()

    if not valid_dates.empty:

        min_date = valid_dates.min().date()
        max_date = valid_dates.max().date()

        selected_dates = st.sidebar.date_input(
            "Select Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )

        if isinstance(selected_dates, tuple):

            if len(selected_dates) == 2:

                start_date, end_date = selected_dates

                filtered_df = filtered_df[
                    (
                        filtered_df["Order Date"].dt.date
                        >= start_date
                    )
                    &
                    (
                        filtered_df["Order Date"].dt.date
                        <= end_date
                    )
                ]


# ============================================================
# FILTER STATUS
# ============================================================

st.sidebar.divider()

st.sidebar.metric(
    "Filtered Records",
    f"{len(filtered_df):,}"
)


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "No records match the selected filters. "
        "Please adjust the filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

if "Order ID" in filtered_df.columns:

    total_orders = filtered_df["Order ID"].nunique()

else:

    total_orders = len(filtered_df)


if total_sales != 0:

    overall_profit_margin = (
        total_profit / total_sales
    ) * 100

else:

    overall_profit_margin = 0


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
        "Overall Profit Margin",
        f"{overall_profit_margin:.2f}%"
    )


st.divider()


# ============================================================
# SALES BY CATEGORY
# ============================================================

if "Category" in filtered_df.columns:

    st.subheader("Sales Performance by Category")

    sales_category = (
        filtered_df
        .groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
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

if "Region" in filtered_df.columns:

    st.subheader("Regional Sales Performance")

    sales_region = (
        filtered_df
        .groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
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

if "Category" in filtered_df.columns:

    st.subheader("Profitability by Category")

    profit_category = (
        filtered_df
        .groupby("Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
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
# SALES TREND
# ============================================================

if "Order Date" in filtered_df.columns:

    st.subheader("Sales Trend Over Time")

    trend_df = (
        filtered_df
        .dropna(subset=["Order Date"])
        .copy()
    )

    if not trend_df.empty:

        trend_df["Month"] = (
            trend_df["Order Date"]
            .dt.to_period("M")
            .dt.to_timestamp()
        )

        sales_time = (
            trend_df
            .groupby("Month", as_index=False)["Sales"]
            .sum()
            .sort_values("Month")
        )

        fig_time = px.line(
            sales_time,
            x="Month",
            y="Sales",
            markers=True,
            title="Monthly Sales Trend"
        )

        fig_time.update_layout(
            xaxis_title="Month",
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
# M6 — ADVANCED VISUAL ANALYTICS
# ============================================================

st.divider()

st.header("Milestone 6 — Advanced Visual Analytics")

st.markdown(
    """
    ### Interactive Profitability Quadrant

    This visualisation extends the M5 dashboard by combining
    sales performance and profitability into a single
    multidimensional analytical view.
    """
)


# ============================================================
# SELECT ANALYTICAL LEVEL
# ============================================================

available_levels = []

for column in [
    "Category",
    "Sub-Category",
    "Region",
    "Segment"
]:

    if column in filtered_df.columns:
        available_levels.append(column)


if not available_levels:

    st.warning(
        "No suitable grouping variables are available "
        "for the M6 profitability analysis."
    )

else:

    selected_level = st.selectbox(
        "Analyse Business Performance By",
        available_levels
    )


    # ========================================================
    # CREATE M6 AGGREGATION
    # ========================================================

    quadrant_df = (
        filtered_df
        .groupby(selected_level, as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=(
                "Order ID",
                "nunique"
            ) if "Order ID" in filtered_df.columns
            else ("Sales", "count")
        )
    )


    quadrant_df["Profit Margin"] = (
        quadrant_df["Profit"]
        / quadrant_df["Sales"]
        * 100
    )

    quadrant_df["Profit Margin"] = (
        quadrant_df["Profit Margin"]
        .replace(
            [float("inf"), -float("inf")],
            0
        )
        .fillna(0)
    )


    # ========================================================
    # QUADRANT THRESHOLDS
    # ========================================================

    sales_median = quadrant_df["Sales"].median()

    margin_median = quadrant_df["Profit Margin"].median()


    # ========================================================
    # QUADRANT CLASSIFICATION
    # ========================================================

    def classify_quadrant(row):

        high_sales = row["Sales"] >= sales_median
        high_margin = row["Profit Margin"] >= margin_median

        if high_sales and high_margin:
            return "High Sales / High Margin"

        elif high_sales and not high_margin:
            return "High Sales / Low Margin"

        elif not high_sales and high_margin:
            return "Low Sales / High Margin"

        return "Low Sales / Low Margin"


    quadrant_df["Performance Quadrant"] = (
        quadrant_df.apply(
            classify_quadrant,
            axis=1
        )
    )


    # ========================================================
    # INTERACTIVE SCATTER PLOT
    # ========================================================

    fig_quadrant = px.scatter(
        quadrant_df,
        x="Sales",
        y="Profit Margin",
        size="Profit",
        color="Performance Quadrant",
        hover_name=selected_level,
        hover_data={
            "Sales": ":,.2f",
            "Profit": ":,.2f",
            "Profit Margin": ":.2f",
            "Orders": ":,",
            "Performance Quadrant": True
        },
        title=(
            "Interactive Profitability Quadrant"
            f" — {selected_level}"
        ),
        labels={
            "Sales": "Total Sales",
            "Profit Margin": "Profit Margin (%)",
            "Performance Quadrant":
                "Performance Classification"
        }
    )


    # ========================================================
    # REFERENCE LINES
    # ========================================================

    fig_quadrant.add_vline(
        x=sales_median,
        line_dash="dash",
        annotation_text="Median Sales"
    )

    fig_quadrant.add_hline(
        y=margin_median,
        line_dash="dash",
        annotation_text="Median Profit Margin"
    )


    fig_quadrant.update_layout(
        xaxis_title="Total Sales",
        yaxis_title="Profit Margin (%)",
        legend_title="Performance Quadrant"
    )


    st.plotly_chart(
        fig_quadrant,
        use_container_width=True
    )


    # ========================================================
    # M6 EXPLANATION
    # ========================================================

    st.subheader("How to Interpret the Quadrants")

    interpretation_col1, interpretation_col2 = st.columns(2)

    with interpretation_col1:

        st.markdown(
            """
            **High Sales / High Margin**

            Strong-performing business areas with both
            high sales and strong profitability.

            **High Sales / Low Margin**

            High-revenue areas where profitability may
            require further investigation.
            """
        )

    with interpretation_col2:

        st.markdown(
            """
            **Low Sales / High Margin**

            Areas with strong profitability but lower
            sales volume.

            **Low Sales / Low Margin**

            Areas that may require further investigation
            regarding performance and business value.
            """
        )


    # ========================================================
    # M6 SUMMARY TABLE
    # ========================================================

    st.subheader("Profitability Analysis Summary")

    display_columns = [
        selected_level,
        "Sales",
        "Profit",
        "Profit Margin",
        "Orders",
        "Performance Quadrant"
    ]

    st.dataframe(
        quadrant_df[display_columns]
        .sort_values("Sales", ascending=False),
        use_container_width=True
    )


# ============================================================
# DECISION SUPPORT
# ============================================================

st.divider()

st.subheader("Decision-Support Insights")

if not filtered_df.empty:

    if "Category" in filtered_df.columns:

        best_category = (
            filtered_df
            .groupby("Category")["Sales"]
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
            f"**Highest Sales Category:** "
            f"{best_category}"
        )

        st.write(
            f"**Most Profitable Category:** "
            f"{most_profitable_category}"
        )


    if "Region" in filtered_df.columns:

        best_region = (
            filtered_df
            .groupby("Region")["Sales"]
            .sum()
            .idxmax()
        )

        st.write(
            f"**Highest Sales Region:** "
            f"{best_region}"
        )


st.write(
    "The dashboard supports decisions relating to "
    "product strategy, regional performance, "
    "profitability and resource allocation."
)


# ============================================================
# FILTERED DATA
# ============================================================

st.divider()

with st.expander("View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "Business Intelligence Dashboard — "
    "Milestones 1–6"
)