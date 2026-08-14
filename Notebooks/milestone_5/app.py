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

data_file = (
    Path(__file__).resolve().parents[2]
    / "Data"
    / "sampledata_processed.csv"
)

if not data_file.exists():
    st.error(f"Dataset not found: {data_file}")
    st.stop()

try:
    df = pd.read_csv(data_file)
except Exception as e:
    st.error(f"Unable to load the dataset: {e}")
    st.stop()


# ============================================================
# DATA VALIDATION
# ============================================================

required_columns = [
    "Sales",
    "Profit",
    "Category",
    "Region"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(
        "The following required columns are missing from the dataset: "
        + ", ".join(missing_columns)
    )
    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

# Convert Order Date to a proper datetime object.
# This is important for chronological time-series analysis.

if "Order Date" in df.columns:

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

# Use the existing Profit Margin Percentage from
# previous milestones where available.
# Otherwise calculate it.

if "Profit Margin Percentage" not in df.columns:

    df["Profit Margin Percentage"] = (
        df["Profit"]
        .div(df["Sales"])
        .mul(100)
    )

    df["Profit Margin Percentage"] = (
        df["Profit Margin Percentage"]
        .replace(
            [float("inf"), -float("inf")],
            0
        )
        .fillna(0)
    )


# ============================================================
# DASHBOARD TITLE
# ============================================================

st.title("📊 Business Intelligence Dashboard")

st.markdown(
    "### Interactive Visual Analytics System"
)

st.markdown(
    """
    This dashboard integrates the data preparation, feature engineering,
    exploratory visualization and statistical findings developed through
    Milestones 1–4 into an interactive business intelligence environment.
    """
)

st.divider()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")

# ------------------------------------------------------------
# Region
# ------------------------------------------------------------

regions = (
    ["All"]
    + sorted(
        df["Region"]
        .dropna()
        .unique()
        .tolist()
    )
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)


# ------------------------------------------------------------
# Category
# ------------------------------------------------------------

categories = (
    ["All"]
    + sorted(
        df["Category"]
        .dropna()
        .unique()
        .tolist()
    )
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)


# ------------------------------------------------------------
# Segment
# ------------------------------------------------------------

if "Segment" in df.columns:

    segments = (
        ["All"]
        + sorted(
            df["Segment"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    selected_segment = st.sidebar.selectbox(
        "Select Segment",
        segments
    )

else:

    selected_segment = "All"


# ------------------------------------------------------------
# Ship Mode
# ------------------------------------------------------------

if "Ship Mode" in df.columns:

    ship_modes = (
        ["All"]
        + sorted(
            df["Ship Mode"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    selected_ship_mode = st.sidebar.selectbox(
        "Select Ship Mode",
        ship_modes
    )

else:

    selected_ship_mode = "All"


# ------------------------------------------------------------
# Date Range
# ------------------------------------------------------------

selected_date_range = None

if "Order Date" in df.columns:

    valid_dates = df["Order Date"].dropna()

    if not valid_dates.empty:

        min_date = valid_dates.min().date()
        max_date = valid_dates.max().date()

        selected_date_range = st.sidebar.date_input(
            "Select Order Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


# Region filter
if selected_region != "All":

    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]


# Category filter
if selected_category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]


# Segment filter
if (
    selected_segment != "All"
    and "Segment" in filtered_df.columns
):

    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]


# Ship Mode filter
if (
    selected_ship_mode != "All"
    and "Ship Mode" in filtered_df.columns
):

    filtered_df = filtered_df[
        filtered_df["Ship Mode"] == selected_ship_mode
    ]


# Date filter
if (
    selected_date_range is not None
    and "Order Date" in filtered_df.columns
):

    if len(selected_date_range) == 2:

        start_date = pd.Timestamp(
            selected_date_range[0]
        )

        end_date = pd.Timestamp(
            selected_date_range[1]
        ) + pd.Timedelta(days=1)

        filtered_df = filtered_df[
            (
                filtered_df["Order Date"] >= start_date
            )
            &
            (
                filtered_df["Order Date"] < end_date
            )
        ]


# ============================================================
# FILTER STATUS
# ============================================================

st.caption(
    f"Showing {len(filtered_df):,} transactions "
    f"from {len(df):,} total transactions."
)


# ============================================================
# HANDLE EMPTY FILTER RESULTS
# ============================================================

if filtered_df.empty:

    st.warning(
        "No records match the selected filters. "
        "Please adjust the dashboard filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()


# Use unique Order ID where available.
if "Order ID" in filtered_df.columns:

    total_orders = filtered_df["Order ID"].nunique()

else:

    total_orders = len(filtered_df)


# Calculate overall profit margin from totals.
# This is more representative than simply averaging
# transaction-level percentages.

if total_sales != 0:

    overall_profit_margin = (
        total_profit / total_sales
    ) * 100

else:

    overall_profit_margin = 0


# ============================================================
# KPI DISPLAY
# ============================================================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        label="Total Sales",
        value=f"${total_sales:,.2f}"
    )


with col2:

    st.metric(
        label="Total Profit",
        value=f"${total_profit:,.2f}"
    )


with col3:

    st.metric(
        label="Total Orders",
        value=f"{total_orders:,}"
    )


with col4:

    st.metric(
        label="Overall Profit Margin",
        value=f"{overall_profit_margin:.2f}%"
    )


st.divider()


# ============================================================
# DASHBOARD TABS
# ============================================================

overview_tab, sales_tab, profitability_tab, trend_tab, data_tab = (
    st.tabs(
        [
            "📊 Overview",
            "💰 Sales Analysis",
            "📈 Profitability",
            "📅 Trends",
            "🗃️ Data Explorer"
        ]
    )
)


# ============================================================
# OVERVIEW TAB
# ============================================================

with overview_tab:

    st.subheader("Business Performance Overview")

    overview_col1, overview_col2 = st.columns(2)


    # --------------------------------------------------------
    # Sales by Category
    # --------------------------------------------------------

    with overview_col1:

        sales_category = (
            filtered_df
            .groupby("Category", as_index=False)["Sales"]
            .sum()
            .sort_values(
                "Sales",
                ascending=False
            )
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
            yaxis_title="Sales",
            hovermode="x unified"
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )


    # --------------------------------------------------------
    # Sales by Region
    # --------------------------------------------------------

    with overview_col2:

        sales_region = (
            filtered_df
            .groupby("Region", as_index=False)["Sales"]
            .sum()
            .sort_values(
                "Sales",
                ascending=False
            )
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
            yaxis_title="Sales",
            hovermode="x unified"
        )

        st.plotly_chart(
            fig_region,
            use_container_width=True
        )


# ============================================================
# SALES ANALYSIS TAB
# ============================================================

with sales_tab:

    st.subheader("💰 Sales Performance Analysis")


    # --------------------------------------------------------
    # Sales by Category
    # --------------------------------------------------------

    sales_category = (
        filtered_df
        .groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_category_sales = px.bar(
        sales_category,
        x="Category",
        y="Sales",
        title="Sales Performance by Category",
        text_auto=".2s"
    )

    fig_category_sales.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Total Sales"
    )

    st.plotly_chart(
        fig_category_sales,
        use_container_width=True
    )


    # --------------------------------------------------------
    # Regional Sales
    # --------------------------------------------------------

    sales_region = (
        filtered_df
        .groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_region_sales = px.bar(
        sales_region,
        x="Region",
        y="Sales",
        title="Regional Sales Performance",
        text_auto=".2s"
    )

    fig_region_sales.update_layout(
        xaxis_title="Region",
        yaxis_title="Total Sales"
    )

    st.plotly_chart(
        fig_region_sales,
        use_container_width=True
    )


    # --------------------------------------------------------
    # Sales Category Distribution
    # --------------------------------------------------------

    if "Sales Category" in filtered_df.columns:

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
# PROFITABILITY TAB
# ============================================================

with profitability_tab:

    st.subheader("📈 Profitability Analysis")


    # --------------------------------------------------------
    # Profit by Category
    # --------------------------------------------------------

    profit_category = (
        filtered_df
        .groupby("Category", as_index=False)["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=False
        )
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
        yaxis_title="Total Profit"
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )


    # --------------------------------------------------------
    # Profit Margin by Category
    # --------------------------------------------------------

    category_margin = (
        filtered_df
        .groupby("Category")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .reset_index()
    )

    category_margin["Profit Margin"] = (
        category_margin["Profit"]
        / category_margin["Sales"]
        * 100
    )

    category_margin = category_margin.replace(
        [float("inf"), -float("inf")],
        0
    ).fillna(0)

    fig_margin = px.bar(
        category_margin,
        x="Category",
        y="Profit Margin",
        title="Profit Margin by Category",
        text_auto=".2f"
    )

    fig_margin.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Profit Margin (%)"
    )

    st.plotly_chart(
        fig_margin,
        use_container_width=True
    )


    # --------------------------------------------------------
    # Profitability Summary
    # --------------------------------------------------------

    profitability_col1, profitability_col2 = st.columns(2)


    with profitability_col1:

        if not profit_category.empty:

            most_profitable_category = (
                profit_category.iloc[0]["Category"]
            )

            highest_profit = (
                profit_category.iloc[0]["Profit"]
            )

            st.metric(
                "Most Profitable Category",
                most_profitable_category
            )

            st.caption(
                f"Total profit: ${highest_profit:,.2f}"
            )


    with profitability_col2:

        if not category_margin.empty:

            best_margin_category = (
                category_margin
                .sort_values(
                    "Profit Margin",
                    ascending=False
                )
                .iloc[0]["Category"]
            )

            best_margin = (
                category_margin
                .sort_values(
                    "Profit Margin",
                    ascending=False
                )
                .iloc[0]["Profit Margin"]
            )

            st.metric(
                "Highest Profit Margin Category",
                best_margin_category
            )

            st.caption(
                f"Profit margin: {best_margin:.2f}%"
            )


# ============================================================
# TREND ANALYSIS TAB
# ============================================================

with trend_tab:

    st.subheader("📅 Sales Trend Over Time")

    if "Order Date" not in filtered_df.columns:

        st.warning(
            "Order Date is not available, so time-series analysis "
            "cannot be displayed."
        )

    else:

        # Remove invalid dates before analysis.
        trend_df = filtered_df.dropna(
            subset=["Order Date"]
        ).copy()


        if trend_df.empty:

            st.warning(
                "No valid dates are available for the selected filters."
            )

        else:

            # ------------------------------------------------
            # IMPORTANT M5 IMPROVEMENT:
            # Create a true monthly time index.
            # ------------------------------------------------

            trend_df["Month"] = (
                trend_df["Order Date"]
                .dt.to_period("M")
                .dt.to_timestamp()
            )


            # Aggregate sales by actual calendar month.
            monthly_sales = (
                trend_df
                .groupby("Month", as_index=False)["Sales"]
                .sum()
                .sort_values("Month")
            )


            # ------------------------------------------------
            # Monthly Sales Chart
            # ------------------------------------------------

            fig_time = px.line(
                monthly_sales,
                x="Month",
                y="Sales",
                markers=True,
                title="Monthly Sales Trend"
            )

            fig_time.update_layout(
                xaxis_title="Month",
                yaxis_title="Total Sales",
                hovermode="x unified"
            )

            fig_time.update_xaxes(
                tickformat="%b %Y"
            )

            st.plotly_chart(
                fig_time,
                use_container_width=True
            )


            # ------------------------------------------------
            # Trend Summary
            # ------------------------------------------------

            if len(monthly_sales) >= 2:

                first_month_sales = (
                    monthly_sales.iloc[0]["Sales"]
                )

                latest_month_sales = (
                    monthly_sales.iloc[-1]["Sales"]
                )

                if first_month_sales != 0:

                    sales_change = (
                        (
                            latest_month_sales
                            - first_month_sales
                        )
                        / first_month_sales
                    ) * 100

                else:

                    sales_change = 0


                trend_col1, trend_col2, trend_col3 = (
                    st.columns(3)
                )


                with trend_col1:

                    st.metric(
                        "First Month Sales",
                        f"${first_month_sales:,.2f}"
                    )


                with trend_col2:

                    st.metric(
                        "Latest Month Sales",
                        f"${latest_month_sales:,.2f}"
                    )


                with trend_col3:

                    st.metric(
                        "Change Across Period",
                        f"{sales_change:+.2f}%"
                    )


            st.caption(
                "Sales are aggregated by calendar month using the "
                "original Order Date field. Months are displayed "
                "chronologically."
            )


# ============================================================
# DATA EXPLORER TAB
# ============================================================

with data_tab:

    st.subheader("🗃️ Filtered Dataset Explorer")

    st.markdown(
        "The table below shows the records matching the "
        "currently selected dashboard filters."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )

    st.caption(
        f"{len(filtered_df):,} filtered records displayed."
    )


# ============================================================
# DECISION SUPPORT
# ============================================================

st.divider()

st.subheader("🎯 Decision-Support Insights")

if not filtered_df.empty:

    # --------------------------------------------------------
    # Highest Sales Category
    # --------------------------------------------------------

    category_sales = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_category = category_sales.index[0]

    best_category_sales = category_sales.iloc[0]


    # --------------------------------------------------------
    # Highest Sales Region
    # --------------------------------------------------------

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_region = region_sales.index[0]

    best_region_sales = region_sales.iloc[0]


    # --------------------------------------------------------
    # Most Profitable Category
    # --------------------------------------------------------

    category_profit = (
        filtered_df
        .groupby("Category")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    most_profitable_category = (
        category_profit.index[0]
    )

    most_profitable_category_profit = (
        category_profit.iloc[0]
    )


    # --------------------------------------------------------
    # Display Summary
    # --------------------------------------------------------

    insight_col1, insight_col2, insight_col3 = (
        st.columns(3)
    )


    with insight_col1:

        st.metric(
            "Highest Sales Category",
            best_category
        )

        st.caption(
            f"Sales: ${best_category_sales:,.2f}"
        )


    with insight_col2:

        st.metric(
            "Highest Sales Region",
            best_region
        )

        st.caption(
            f"Sales: ${best_region_sales:,.2f}"
        )


    with insight_col3:

        st.metric(
            "Most Profitable Category",
            most_profitable_category
        )

        st.caption(
            f"Profit: "
            f"${most_profitable_category_profit:,.2f}"
        )


    # --------------------------------------------------------
    # Business Interpretation
    # --------------------------------------------------------

    st.markdown("### Business Interpretation")

    st.write(
        f"**Sales leadership:** {best_category} generates "
        f"the highest sales among the categories visible "
        f"under the current filters."
    )

    st.write(
        f"**Regional performance:** {best_region} has the "
        f"highest sales among the currently selected records."
    )

    st.write(
        f"**Profitability:** {most_profitable_category} "
        f"generates the highest total profit among the "
        f"currently selected categories."
    )

    st.info(
        "These indicators can support decisions concerning "
        "resource allocation, product strategy, profitability "
        "management and regional performance."
    )


# ============================================================
# M4 STATISTICAL EVIDENCE SUMMARY
# ============================================================

st.divider()

with st.expander(
    "🔬 Statistical Evidence from Milestone 4"
):

    st.markdown(
        """
        The following findings were established through the
        statistical analysis conducted in Milestone 4.

        **Discount and Profit**

        The analysis identified a statistically significant
        negative relationship between discount and profit.

        **Sales and Profit**

        Sales and profit showed a moderate positive relationship.

        **Sales Trend**

        The time-series analysis identified a statistically
        significant increasing sales trend.

        **Important note:** These results are presented as
        previously validated findings from Milestone 4.
        The advanced interactive statistical exploration
        will be developed as part of Milestone 6.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Business Intelligence Dashboard — Milestone 5 | "
    "Interactive Visual Analytics System"
)