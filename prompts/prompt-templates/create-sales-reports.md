# Create Sales Reports

## Source
https://claude.com/resources/use-case/create-sales-reports

## Template Prompt

I need a {QUARTER|Q1,Q2,Q3,Q4} sales report for our {AUDIENCE|exec team,board,department,sales team} meeting {TIMEFRAME|next week,this Friday,end of month}. Pull {START_MONTH} through {END_MONTH} from {DATA_SOURCE|HubSpot,Salesforce,Google Drive,CRM system}.

Show me:

**Revenue Analysis:**
- Total revenue vs {COMPARISON_PERIOD|previous quarter,same quarter last year,annual target}—how much did we grow, and was it from {GROWTH_FACTORS|more deals or bigger deals,new customers or expansion,product mix changes}?
- {REVENUE_BREAKDOWN|Revenue breakdown,Growth trajectory,Year-over-year comparison}

**Segment Performance:**
Break it down by {SEGMENT_TYPE|segment,region,product line,sales channel}: {SEGMENT_OPTIONS|Enterprise, Mid-Market, and SMB,North America, EMEA, APAC,Product A, Product B, Product C}. For each one, show:
- Revenue and {GROWTH_METRIC|growth percentage,variance from target,year-over-year change}
- Number of deals and {VOLUME_METRIC|average deal size,deal velocity,conversion rate}
- Win rate and {EFFICIENCY_METRIC|sales cycle length,pipeline coverage,quota attainment}

**Sales Cycle Analysis:**
- How long are sales cycles taking now compared to {COMPARISON_PERIOD}?
- {CYCLE_METRICS|Average time-to-close by segment,Bottlenecks in the pipeline,Stage conversion rates}
- {TREND_ANALYSIS|Acceleration or deceleration trends,Seasonal patterns,Forecasting implications}

**Pipeline Health:**
- Current pipeline value and {PIPELINE_METRICS|coverage ratio,stage distribution,expected close dates}
- {PIPELINE_QUALITY|Win probability weighted value,Pipeline aging analysis,Risk assessment}
- {FORECAST|Next quarter forecast,At-risk deals,Upside opportunities}

**Team Performance:**
- Top {TOP_COUNT|3,5,10} reps by {PERFORMANCE_METRIC|revenue,deal count,quota attainment} with their numbers
- {TEAM_METRICS|Team-wide quota attainment,Performance distribution,Ramp time for new reps}
- {RECOGNITION|Notable achievements,Improvement highlights,Coaching opportunities}

**Strategic Insights:**
- What's actually working and what needs to change
- {ANALYSIS_AREAS|Channel effectiveness,Product performance,Market trends,Competitive dynamics}
- {RECOMMENDATIONS|Action items,Resource allocation suggestions,Process improvements,Investment priorities}

**Formatting Requirements:**
Create this as a professional document with:
- {FONT_STYLE|Clean serif fonts,Modern sans-serif,Corporate brand fonts}
- {LAYOUT|Information dense with tight spacing,Balanced white space,Executive summary format}
- Proper text hierarchy with {HIERARCHY_ELEMENTS|section headers,callout statistics,executive summary}
- Embedded {CHART_TYPE|chart PNGs,interactive charts,data tables,infographics} that seamlessly integrate into the layout as opposed to looking pasted in
- {STYLE_DIRECTION|Proper business style. Opt out of using your default styles,Modern and clean aesthetic,Traditional corporate format,Data-journalism style}

## Use Case Description

This template helps create comprehensive sales reports by integrating with CRM systems to extract live metrics, then synthesizing that data into polished business reports. The workflow analyzes performance trends, creates data visualizations, and delivers actionable insights formatted for executive presentation—all without manual data extraction or formatting.

## Variables Explanation

- **QUARTER**: Which fiscal quarter is being reported
- **AUDIENCE**: Who will receive the report
- **TIMEFRAME**: When the report is needed
- **START_MONTH**: Beginning of reporting period
- **END_MONTH**: End of reporting period
- **DATA_SOURCE**: Where sales data is stored
- **COMPARISON_PERIOD**: Time period for comparison
- **GROWTH_FACTORS**: What drove growth or decline
- **REVENUE_BREAKDOWN**: How to analyze revenue
- **SEGMENT_TYPE**: How to segment the business
- **SEGMENT_OPTIONS**: Specific segments to analyze
- **GROWTH_METRIC**: Revenue performance indicators
- **VOLUME_METRIC**: Deal volume indicators
- **EFFICIENCY_METRIC**: Sales efficiency indicators
- **CYCLE_METRICS**: Sales cycle analysis details
- **TREND_ANALYSIS**: Pattern and trend insights
- **PIPELINE_METRICS**: Pipeline health indicators
- **PIPELINE_QUALITY**: Pipeline quality assessment
- **FORECAST**: Forward-looking projections
- **TOP_COUNT**: Number of top performers to highlight
- **PERFORMANCE_METRIC**: How to rank performance
- **TEAM_METRICS**: Team-wide statistics
- **RECOGNITION**: Individual achievements to note
- **ANALYSIS_AREAS**: Strategic analysis topics
- **RECOMMENDATIONS**: Types of recommendations to provide
- **FONT_STYLE**: Typography choices
- **LAYOUT**: Document layout style
- **HIERARCHY_ELEMENTS**: Document structure elements
- **CHART_TYPE**: Data visualization format
- **STYLE_DIRECTION**: Overall design approach
