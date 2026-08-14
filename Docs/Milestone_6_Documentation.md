# Milestone 6 — Technical Documentation

## 1. Overview

Milestone 6 extends the Interactive Visual Analytics System developed in Milestone 5.

The main contribution is an interactive Profitability Quadrant that combines multiple business performance measures into a single visual analytical view.

---

## 2. M6 Objective

The objective of M6 is to extend the dashboard beyond individual metric comparisons and provide multidimensional visual analysis that supports more advanced business decision-making.

---

## 3. Advanced Visualisation

The M6 system introduces an interactive scatter-based profitability analysis.

The visualisation uses:

| Visual Element | Measure |
|---|---|
| X-axis | Total Sales |
| Y-axis | Profit Margin |
| Bubble Size | Total Profit |
| Colour | Performance Quadrant |
| Hover Data | Sales, Profit, Margin and Orders |

---

## 4. Performance Quadrants

The visualisation divides business groups using median Sales and median Profit Margin.

### High Sales / High Margin

Represents strong-performing areas with both high sales and strong profitability.

### High Sales / Low Margin

Represents high-revenue areas where profitability may require investigation.

### Low Sales / High Margin

Represents areas with strong margins but lower sales volume.

### Low Sales / Low Margin

Represents lower-performing areas requiring further investigation.

---

## 5. Interactive Grouping

Users can select an available business grouping such as:

- Category
- Sub-Category
- Region
- Segment

The visualisation is recalculated according to the selected grouping.

---

## 6. System Improvement

M6 improves the M5 system by:

- Adding multidimensional visual analysis.
- Providing interactive profitability classification.
- Combining Sales, Profit and Profit Margin.
- Allowing analysis at different business levels.
- Adding hover-based analytical detail.
- Adding median reference lines.
- Adding a profitability summary table.
- Using cached data loading to reduce unnecessary dataset reloads.

---

## 7. Data Handling

The project uses a static processed CSV dataset.

Real-time streaming functionality is not applicable to the current dataset.

The system therefore focuses on efficient local data handling through:

- Cached dataset loading.
- Filtering.
- Aggregation.
- Group-level calculations.
- Efficient visualisation of aggregated data.

---

## 8. Research Contribution

M6 investigates whether multidimensional interactive visualisation can improve the identification of business performance patterns compared with viewing individual metrics separately.

The main research question is:

> How can multidimensional interactive visualisation improve the identification of sales and profitability patterns in a Business Intelligence system compared with analysing individual performance metrics separately?

The proposed contribution allows users to identify business groups that may not be obvious when Sales, Profit and Profit Margin are viewed independently.

---

## 9. M5 to M6 Progression

M5 provided:

- Interactive filters
- KPIs
- Sales analysis
- Profit analysis
- Time-series analysis
- Decision-support insights

M6 extends this functionality with:

- Multidimensional analysis
- Profitability quadrants
- Dynamic grouping
- Interactive analytical exploration
- Advanced decision support

---

## 10. Testing

The M6 visualisation should be tested using:

- Different categories.
- Different regions.
- Different segments.
- Multiple dashboard filters.
- Empty filter results.
- Negative profit values.
- Zero sales values.
- Different analytical groupings.

The expected result is that the visualisation updates correctly without breaking the existing M5 functionality.

---

## 11. Limitations

The M6 system uses a static historical dataset and does not provide real-time streaming analysis.

The quadrant boundaries are based on median values within the selected dataset. Therefore, the classification is relative to the currently selected data rather than being an absolute industry benchmark.

The visualisation is intended to support decision-making and does not independently establish causal relationships.

---

## 12. Outcome

M6 extends the Business Intelligence dashboard with an advanced interactive visualisation that allows Sales, Profit and Profit Margin to be examined simultaneously.

The feature provides a more multidimensional view of business performance and strengthens the decision-support capability of the final system.