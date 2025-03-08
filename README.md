# Solar Power Performance Analysis: Optimizing Energy Usage & Cost Savings

---

## Project Overview
This project aims to **analyze, optimize, and maximize solar power efficiency** while minimizing reliance on grid electricity. By leveraging **real-time solar energy data** from Lux Power Tek, the dashboard provides **insights into energy consumption, grid dependency, and financial savings**.  

✔ **Live Dashboard Link**: [Solar Power Performance Analysis](https://app.powerbi.com/reportEmbed?reportId=aad797a8-917e-4b98-8d83-e2ca78ed143c&autoAuth=true&ctid=254ba93e-1f6f-48f3-90e6-e2766664b477)  

![Power BI Dashboard](assets/images/dashboard.gif)

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Objective](#objective)
  - [Strategic Goals](#strategic-goals)
  - [Pain Point](#pain-point)
  - [Ideal Solution](#ideal-solution)
- [User Story](#user-story)
- [Data Source](#data-source)
- [Dashboard Design](#dashboard-design)
  - [Home Page](#home-page)
  - [Daily Energy & Power Performance](#daily-energy--power-performance)
  - [Monthly Energy & Cost Breakdown](#monthly-energy--cost-breakdown)
  - [Financial Impact & Cost-Benefit Analysis](#financial-impact--cost-benefit-analysis)
  - [Key Insights & Actions](#key-insights--actions)
- [Tools Used](#tools-used)
- [Development Process](#development-process)
- [Codes Used](#codes-used)
- [Analysis & Insights](#analysis--insights)
  - [Key Takeaways](#key-takeaways)
  - [Recommendations](#recommendations)
  - [Potential ROI](#potential-roi)
  - [Action Plan](#action-plan)
- [Connect with Me](#connect-with-me)
- [Feedback & Suggestions](#feedback--suggestions)

## Feedback & Suggestions
---

## Problem Statement
Electricity costs continue to rise, and **solar power adoption alone does not guarantee maximum savings**. Homeowners need **actionable insights** on:
- **When to use appliances** for **maximum solar efficiency**  
- **How to reduce grid dependency** for better energy independence  
- **When to clean panels** to **prevent efficiency drops**  
- **How much money is saved** and the **ROI of their solar investment**  

A **data-driven solution** is required to help homeowners make **smarter energy decisions** and **maximize their solar investment**.

---

## Objective

### Strategic Goals
- **Optimize energy efficiency** by identifying peak solar hours for optimal appliance usage  
- **Improve solar utilization monitoring** to detect potential panel maintenance needs  
- **Minimize electricity costs** through data-driven decisions  
- **Analyze return on investment (ROI)** to quantify financial savings and long-term benefits  

### Pain Point
Traditional energy monitoring does not provide insights into **how to optimize solar power usage**. Without **real-time tracking**, energy efficiency is **not maximized**, and cost savings are **not fully realized**.

### Ideal Solution
A **Power BI dashboard** that provides:
- **Real-time solar energy production insights**
- **Best time to run appliances** for free solar energy  
- **Grid dependency tracking** to optimize energy consumption  
- **Cost savings analysis** from solar energy usage  
- **Actionable insights** to reduce electricity expenses  

---

## User Story
*"As a homeowner who has invested in solar energy, I want to monitor solar production, consumption, and grid usage in real time so that I can make **data-driven decisions** on when to use high-power appliances and how to **maximize solar efficiency while minimizing costs**."*

*"Since installing solar panels last year, I’ve seen the benefits of reduced electricity expenses, but I know there’s **room for improvement**. I want to identify the **best times to use appliances**, track how much I’m **saving**, and determine whether my **solar panels need cleaning or maintenance** to ensure optimal efficiency. By leveraging **insights from data**, I aim to **reduce grid dependency** and **maximize my return on investment** over time."*

---

## Data Source
- **Data extracted from:** Lux Power Tek (Solar monitoring system)  
- **Data transformation & combination:** Python (Pandas)  
- **Final dataset stored as:** CSV for Power BI integration  

---

## Dashboard Design

### Home Page
**Purpose:**  
Provides an **overview of solar performance metrics**, including total energy consumption, solar energy produced, and cost savings.  

**Cards Used:**  
- Total Solar Energy Produced  
- Electricity Cost  
- Savings  
- Self-Sufficiency Ratio  
- Grid Dependency Ratio  

**Visuals/Charts Used:**  
- KPI Cards for quick performance metrics  

---

### Daily Energy & Power Performance
**Purpose:**  
Tracks **hourly energy consumption, solar generation, and grid import** to identify daily trends.  

**Cards Used:**  
- Energy Consumption  
- Solar Energy Utilization Rate  
- Solar Energy Produced  
- Grid Energy Import  

**Visuals/Charts Used:**  
- Line Chart: **Energy Trends**
- Scatter Plot: **Solar Energy & Grid Usage Correlation**
- Bar Chart: **Energy Distribution**

---

### Monthly Energy & Cost Breakdown
**Purpose:**  
Analyzes **monthly energy usage, savings, and grid dependency trends**.  

**Cards Used:**  
- Energy Consumption  
- Savings from Solar Energy  
- Solar Energy Produced  
- Grid Energy Import  

**Visuals/Charts Used:**  
- Line Chart: **Energy Cost Breakdown**
- Area Chart: **Solar vs. Grid Usage Over Time**
- Stacked Bar Chart: **Solar vs. Grid Contribution**

---

### Financial Impact & Cost-Benefit Analysis
**Purpose:**  
Evaluates **ROI, investment recovery, and cost savings over time**.  

**Cards Used:**  
- Total Investment Cost  
- Cost of Electricity  
- Total Annual Savings  
- Return on Investment  

**Visuals/Charts Used:**  
- Area Chart: **Monthly Electricity Cost vs. Solar Savings**
- Bar Chart: **Investment Recovery Progress**

---

### Key Insights & Actions
**Purpose:**  
Provides **actionable insights based on performance metrics** to optimize solar energy usage.  

**Cards Used:**  
- Best Time to Use More Appliances  
- Total Solar Savings to Date  
- Investment Return Progress  
- Solar Utilization Efficiency  

**Visuals/Charts Used:**  
- Text-based insights & recommendations  

---

## Tools Used

| Tool | Purpose |
|------|---------|
| **Power BI** | Data visualization and interactive dashboard |
| **Python (Pandas)** | Data transformation and combining CSV files |
| **GitHub** | Version control and documentation |

---

## Development Process

### Pseudocode
1. **Extract** solar energy data from Lux Power Tek  
2. **Combine and clean** datasets using Python  
3. **Analyze** key performance metrics (solar utilization, grid dependency, cost savings)  
4. **Develop** Power BI dashboard to visualize real-time trends  
5. **Deploy** interactive insights for decision-making  

---

## Codes Used

```python
# Python code to check data quality
import pandas as pd

df = pd.read_csv("solar_data.csv")
print(f"Row Count: {df.shape[0]}, Column Count: {df.shape[1]}")
print("Data Types:\n", df.dtypes)
print("Duplicate Entries:", df.duplicated().sum())
```

```dax
Day of the Month = FORMAT(luxpower[Datetime], "MMMM d, yyyy")

TimeOnly = FORMAT(luxpower[Datetime], "HH:mm")

_Monthly_Energy_Consumption = 
SUMX(VALUES(luxpower[Datetime]), MAX(luxpower[Energy Consumption]))

_Solar_Utilization_Efficiency = 
DIVIDE([_Monthly_Solar_Energy_Used], [_Monthly_Energy_Consumption], 0)

_Investment_Recovery_Progress = 
CALCULATE(
    SUMX(VALUES(luxpower[Datetime].[Month]), [_Monthly_Savings_New]),
    FILTER(ALL(luxpower), luxpower[Datetime] <= MAX(luxpower[Datetime]))
)

_Optimal_Appliance_Usage_Time = 
VAR _HourlySolarPower = 
    SUMMARIZE(
        luxpower,
        HOUR(luxpower[Datetime]),
        "Avg_SolarPower", AVERAGE(luxpower[Solar Power Produced])
    )
VAR _BestHour = 
    MAXX(TOPN(1, _HourlySolarPower, [Avg_SolarPower], DESC), [Hour])

RETURN FORMAT(_BestHour, "00:00") & " - " & FORMAT(_BestHour + 1, "00:00")
```

---

## Analysis & Insights
### Key Takeaways
- Solar energy production peaks at 11:00 AM - 12:00 PM.  
- Grid dependency remains at 68.43%, highlighting optimization opportunities.  
- Savings from solar energy reached ₱60,998.36, demonstrating financial benefits.  
- Solar utilization efficiency is currently at 3.93%. A drop in this value could indicate dust accumulation or shading on the panels, reducing energy generation.  
- Battery storage could improve energy independence, allowing stored energy for nighttime use.  

### Recommendations
- Run high-power appliances between 11:00 AM - 12:00 PM for free energy.  
- Monitor solar efficiency and clean panels regularly to maintain output.  
- Consider battery storage to store excess solar energy for nighttime use.  

### Potential ROI
- Investment Payback Period: 4.45 years.  
- Savings Projection: ₱58,377.67 in annual cost reductions.  
- Battery Storage ROI: Could further decrease grid dependence by up to 25%.  

### Action Plan
- Optimize usage during peak solar hours to reduce electricity bills.  
- Clean solar panels periodically to maintain efficiency.  
- Install battery storage to maximize overnight solar energy use.
- Monitor and adjust grid dependency with real-time analytics.  

---

## Feedback & Suggestions
I’m just starting my Data Analytics career transition journey, and this is my first challenge. I know I have a long way to go, and I’d love to hear your feedback and suggestions to improve my analysis! Feel free to share your thoughts.  

---

## Connect with Me
📂 GitHub Profile: [github.com/aeronabrahan](https://github.com/aeronabrahan)  
🔗 LinkedIn Profile: [linkedin.com/in/jagabrahan](https://linkedin.com/in/jagabrahan)  
📧 Email Address: [aerongabrahan@gmail.com](mailto:aerongabrahan@gmail.com)

---
