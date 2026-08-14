# Business Intelligence Dashboard

A collaborative Business Intelligence and Visual Analytics system developed for the Data Visualization course.

The project uses the Sample Superstore dataset to progress from data preparation and exploratory analysis to statistical analysis, interactive dashboards, and advanced visual analytics.

---

## Project Status

| Milestone | Objective | Status |
|---|---|---|
| M1 | Data Representation & Foundations | COMPLETED |
| M2 | Data Processing & Transformation | COMPLETED |
| M3 | Visualization & Exploratory Analysis | COMPLETED |
| M4 | Statistical Inference & Analytical Modeling | COMPLETED |
| M5 | Interactive Visual Analytics System | COMPLETED |
| M6 | Research Contribution & Advanced Analytics | COMPLETED |

---

## Project Objectives

The project aims to:

- Prepare and analyse a real-world business dataset.
- Identify data-quality issues and important business variables.
- Develop exploratory and statistical analyses.
- Create meaningful business visualisations.
- Build an interactive Business Intelligence dashboard.
- Provide decision-support insights.
- Extend the dashboard with an advanced visual analytics contribution.
- Produce a final integrated system, research paper and presentation.

---

## Dataset

**Dataset:** Sample Superstore Dataset  
**Source:** Tableau Sample Data Website  
**Business Domain:** Retail  
**Records:** Approximately 10,000  
**Features:** 21

### Key Variables

- Customer orders
- Products
- Categories
- Sales
- Profit
- Quantity
- Discount
- Regions
- Geographic information
- Shipping
- Order dates

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Analysis and application development |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Plotly | Interactive visualisations |
| Streamlit | Interactive dashboard |
| Jupyter Notebook | Milestone analysis |
| Git/GitHub | Version control and collaboration |

---

## Repository Structure

```text
business_intelligence_dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── load_dataset.ipynb
│   ├── milestone_1_foundations.ipynb
│   ├── milestone_2.ipynb
│   ├── milestone_3.ipynb
│   ├── milestone_4.ipynb
│   ├── milestone_5.ipynb
│   └── milestone_6.ipynb
│
├── visuals/
│
├── reports/
│   ├── data_quality_report.md
│   ├── statistical_summary.md
│   ├── project_report.md
│   └── milestone_reports/
│
├── docs/
│   ├── contribution_guidelines.md
│   ├── project_specification.md
│   ├── data_dictionary.md
│   ├── milestone_5_documentation.md
│   └── milestone_6_documentation.md
│
├── src/
├── presentation/
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder Guide

- `data/` — raw, processed and external datasets.
- `notebooks/` — milestone analysis and experimentation.
- `visuals/` — exported figures and visual assets.
- `reports/` — formal academic reports.
- `docs/` — technical and project documentation.
- `src/` — reusable Python code.
- `presentation/` — final presentation materials.

---

# Milestones

## M1 — Data Representation & Foundations

**Status: COMPLETED**

Established the project and business understanding, explored the dataset, identified important variables and investigated initial data-quality issues.

---

## M2 — Data Processing & Transformation

**Status: COMPLETED**

Completed:

- Data preprocessing
- Missing-value handling
- Feature engineering
- Data transformation
- Business visualisations
- Insight analysis
- Business recommendations

The processed dataset became the foundation for later milestones.

---

## M3 — Visualization & Exploratory Analysis

**Status: COMPLETED**

Focused on exploratory visual analysis of:

- Sales
- Profit
- Categories
- Regions
- Relationships between variables
- Time-based patterns
- Distributions

The findings provided the foundation for the interactive dashboard.

---

## M4 — Statistical Inference & Analytical Modeling

**Status: COMPLETED**

Extended the exploratory analysis through statistical investigation.

Key relationships examined included:

- Sales and profit
- Discount and profit
- Sales over time

The statistical findings provide supporting evidence for the visual analysis used in later milestones.

---

## M5 — Interactive Visual Analytics System

**Status: COMPLETED**

M5 transformed the previous analytical work into an interactive Business Intelligence dashboard using Streamlit, Pandas and Plotly.

### Main Features

- Interactive filtering
- Key Performance Indicators
- Total Sales
- Total Profit
- Total Orders
- Profit Margin
- Sales by Category
- Sales by Region
- Profit by Category
- Profitability analysis
- Sales trend analysis
- Decision-support insights
- Filtered data exploration

### M5 Workflow

```text
Processed Dataset
       ↓
Data Preparation
       ↓
Interactive Filters
       ↓
Filtered Dataset
       ↓
KPIs & Visualisations
       ↓
Decision-Support Insights
```

Technical details are documented in:

```text
docs/milestone_5_documentation.md
```

---

# M6 — Research Contribution & Advanced Analytics

**Status: IN PROGRESS**

M6 extends the completed M5 dashboard with an advanced visual analytics contribution.

The milestone requires:

- An advanced analytical or visualisation method
- System improvement or innovation
- Research-level explanation
- Final integrated system
- Research paper draft
- Final presentation and demonstration

## M6 Research Direction

Because this project focuses on Data Visualization, M6 will introduce an advanced interactive visualisation rather than a separate machine learning model.

The proposed contribution is an interactive **Profitability Analysis / Profitability Quadrant**.

The visualisation will combine:

- Sales
- Profit
- Profit Margin
- Category or another suitable business grouping

This allows users to identify patterns such as:

```text
High Sales + High Profitability
High Sales + Low Profitability
Low Sales + High Profitability
Low Sales + Low Profitability
```

The purpose is to improve decision support by analysing multiple business measures simultaneously.

---

## M6 Research Question

> How can multidimensional interactive visualisation improve the identification of sales and profitability patterns in a Business Intelligence system compared with analysing individual performance metrics separately?

The research will consider:

- Pattern identification
- Information density
- User interaction
- Business interpretation
- Decision-support value
- Limitations of the approach

---

## M6 Data Handling

The current project uses a static processed CSV dataset.

Real-time streaming is therefore not applicable to the current dataset.

Where appropriate, M6 may improve data handling through:

- Efficient data loading
- Caching
- Filtering
- Aggregation before visualisation
- Avoiding unnecessary repeated calculations

No streaming functionality should be claimed unless it is actually implemented.

---

## M6 Deliverables

The final M6 submission will include:

- [ ] Final integrated system
- [ ] Advanced visualisation
- [ ] M6 testing
- [ ] M6 technical documentation
- [ ] Research paper draft
- [ ] Final presentation
- [ ] Final system demonstration

---

# Development Workflow

All team members should work through feature branches.

### 1. Update `main`

```powershell
git checkout main
git pull origin main
```

### 2. Create a Feature Branch

```powershell
git checkout -b feature-name
```

Example:

```powershell
git checkout -b milestone-6-visualisation
```

### 3. Develop and Test

Complete the assigned task and test it locally.

### 4. Commit

```powershell
git add .
git commit -m "Added Milestone 6 advanced visualisation"
```

### 5. Push

```powershell
git push -u origin feature-name
```

### 6. Pull Request

Create a Pull Request and wait for review before merging into `main`.

---

# Repository Rules

1. Do not push directly to `main`.
2. Always use a feature branch.
3. Pull the latest `main` before starting work.
4. Use descriptive commit messages.
5. Test changes before opening a Pull Request.
6. Keep notebooks runnable from top to bottom.
7. Keep raw data unchanged.
8. Do not overwrite another member's work without discussion.
9. Update documentation when significant changes are made.
10. Keep the repository organised and reproducible.

---

# Environment Setup

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

# Running the Dashboard

Run the Streamlit application using its project path.

General command:

```powershell
python -m streamlit run path\to\app.py
```

Example:

```powershell
python -m streamlit run .\Notebooks\milestone_5\app.py
```

The exact application path should be kept consistent across the team and documented in the relevant milestone documentation.

---

# Testing

Before merging changes, test:

- Dashboard startup
- Dataset loading
- Filters
- KPI calculations
- Visualisation updates
- Date handling
- Empty filter results
- Missing data
- Required fields
- M6 advanced visualisation
- Multiple filter combinations

---

# Team Members

1. Curtis Njera
2. Sandra Koech
3. Samira Abdiaziz
4. Esther Mwangi
5. Caleb Kyalo

---

# Final System

The project progresses through:

```text
Data Understanding
       ↓
Data Processing
       ↓
Exploratory Visualisation
       ↓
Statistical Analysis
       ↓
Interactive Dashboard
       ↓
Advanced Visual Analytics
       ↓
Final Integrated System
```

M1–M4 provide the analytical foundation.

M5 provides the completed interactive dashboard.

M6 extends the dashboard with advanced visual analytics and a research contribution.

The final project will combine the completed analysis, interactive dashboard, advanced visualisation, research paper and final presentation into one integrated Business Intelligence system.