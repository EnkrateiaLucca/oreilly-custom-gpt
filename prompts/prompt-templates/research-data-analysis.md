# Research Data Analysis

## Source
Inspired by: https://claude.com/resources/use-case/genomic-data-analysis

## Template Prompt
My colleagues recently published the attached {DATA_TYPE|time-series data,survey results,financial data,sensor data,experimental measurements} that describes {COMPARISON_DESCRIPTION} with a focus on {FOCUS_AREA}. I would like to explore these samples but focus on {SPECIFIC_SUBSET_OR_CONDITION} and differences between {CONDITION_A} and {CONDITION_B}. Can you help me first go through the differential patterns and create a {VISUALIZATION_TYPE|heatmap,scatter plot,line graph,bar chart,box plot} and then also identify trends or clusters that are significant in each sample?
Use Case Description
This template helps researchers and analysts examine datasets by requesting computational analysis of uploaded data files. The prompt guides Claude to examine patterns between different conditions, generate visualizations, and perform statistical analysis to identify significant differences or trends.
Variables Explanation

## Variable Explanations
DATA_TYPE: Type of dataset being analyzed (time-series, survey, financial, etc.)
COMPARISON_DESCRIPTION: What the dataset compares (e.g., "performance metrics between two product versions")
FOCUS_AREA: The domain or aspect being studied (e.g., "user engagement patterns")
SPECIFIC_SUBSET_OR_CONDITION: Specific subset to analyze (e.g., "enterprise users")
CONDITION_A and CONDITION_B: The two conditions being compared (e.g., "before implementation" vs "after implementation")
VISUALIZATION_TYPE: Preferred visualization method for the analysis