# Milestone 6 Research Paper Draft

## Title

### Multidimensional Interactive Visualisation for Sales and Profitability Analysis in Business Intelligence

---

## Abstract

Business Intelligence dashboards commonly present sales, profit and profitability measures through separate charts and indicators. While these views provide useful information, analysing individual metrics separately can make relationships between business performance measures more difficult to identify.

This project extends an interactive Business Intelligence dashboard with a multidimensional profitability visualisation. The proposed approach combines sales, profit and profit margin within an interactive visual analytical view. Business groups are classified according to their relative sales and profitability using median-based quadrants.

The contribution provides an additional decision-support mechanism for identifying high-performing, high-revenue but lower-margin, low-volume but profitable, and lower-performing business areas.

---

## 1. Introduction

Business Intelligence systems transform organisational data into information that can support decision-making. Visualisation plays an important role because it allows users to identify patterns that may be difficult to recognise from tabular data alone.

The earlier milestones of this project established the data-processing, exploratory, visual and statistical foundations of the system. Milestone 5 then integrated these findings into an interactive dashboard.

Milestone 6 extends this system through an advanced multidimensional visualisation.

---

## 2. Research Question

> How can multidimensional interactive visualisation improve the identification of sales and profitability patterns in a Business Intelligence system compared with analysing individual performance metrics separately?

---

## 3. Methodology

The project uses the processed Sample Superstore dataset developed during the previous milestones.

The M6 methodology consists of:

1. Loading the processed dataset.
2. Applying the existing dashboard filters.
3. Aggregating business performance according to a selected grouping.
4. Calculating total Sales and Profit.
5. Calculating Profit Margin.
6. Calculating median Sales and median Profit Margin.
7. Classifying observations into performance quadrants.
8. Displaying the results through an interactive visualisation.
9. Evaluating the analytical value of the visualisation.

---

## 4. Advanced Visualisation Method

The M6 contribution uses an interactive scatter visualisation.

The x-axis represents Total Sales.

The y-axis represents Profit Margin.

Bubble size represents Total Profit.

Colour represents the performance quadrant.

Hover information provides additional business measures.

This allows several variables to be explored simultaneously.

---

## 5. Performance Classification

The visualisation uses median Sales and median Profit Margin as reference points.

Four performance groups are created:

### High Sales / High Margin

These represent relatively strong performers.

### High Sales / Low Margin

These represent high-revenue areas where profitability may require further investigation.

### Low Sales / High Margin

These represent areas with relatively strong margins but lower sales volume.

### Low Sales / Low Margin

These represent areas with both relatively lower sales and profitability.

---

## 6. System Innovation

The M6 feature extends the M5 dashboard from individual metric analysis to multidimensional analysis.

Instead of examining Sales, Profit and Profit Margin separately, the user can investigate their relationships within one interactive visualisation.

The feature also allows the analytical grouping to be changed between available business dimensions.

---

## 7. Results

The completed visualisation allows users to identify business groups according to their relative sales and profitability.

The results should be discussed using screenshots and actual observations from the final dashboard.

Example observations should identify:

- High-sales/high-margin groups.
- High-sales/low-margin groups.
- Low-sales/high-margin groups.
- Low-sales/low-margin groups.

These observations should be based on the final dashboard output rather than assumed in advance.

---

## 8. Discussion

The multidimensional visualisation provides a more integrated view of business performance than individual charts alone.

It allows users to identify cases where high sales do not necessarily correspond to high profitability.

It also highlights business areas with relatively strong margins but lower sales volume.

These patterns can support further investigation into pricing, discounting, costs, product strategy and resource allocation.

---

## 9. Limitations

The dataset is static rather than streaming.

The quadrant thresholds are relative to the selected dataset because they use median values.

The visualisation identifies patterns and associations but does not establish causal relationships.

The system should therefore be used as a decision-support tool rather than an automatic decision-making system.

---

## 10. Research Contribution

The main contribution of M6 is the integration of multidimensional interactive visual analysis into the existing Business Intelligence dashboard.

The approach demonstrates how multiple business performance measures can be combined into a single interactive analytical view.

This extends the system beyond standard KPI and chart-based reporting and provides an additional method for exploring business performance.

---

## 11. Conclusion

Milestone 6 extends the Business Intelligence dashboard developed in Milestone 5 through an advanced interactive profitability visualisation.

The contribution combines Sales, Profit and Profit Margin to provide a multidimensional view of business performance.

The resulting system strengthens the decision-support capability of the dashboard and provides a practical example of how advanced visual analytics can be integrated into a Business Intelligence system.

---

## 12. References

Add the academic and technical sources used to support the final research discussion here.

References should be formatted consistently according to the citation style required by the course.