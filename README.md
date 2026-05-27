# 📊 Industry Data Visualizations

> Critical data visualizations for **Automotive** and **Healthcare** industries using Python, Pandas, Matplotlib, Seaborn, and Plotly — built with example datasets to uncover actionable insights.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-79A6BF?style=for-the-badge)](https://seaborn.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📁 Project Structure

```
industry-data-visualizations/
│
├── 📂 automotive/
│   ├── datasets/
│   │   ├── ev_sales_data.csv            # EV & ICE vehicle sales 2015–2024
│   │   ├── fuel_efficiency.csv          # MPG trends by manufacturer & segment
│   │   ├── vehicle_recalls.csv          # NHTSA recall data by make/year
│   │   └── production_supply_chain.csv  # Production volumes & supply disruptions
│   └── automotive_visualizations.py     # All automotive charts & plots
│
├── 📂 healthcare/
│   ├── datasets/
│   │   ├── patient_outcomes.csv         # Hospital readmissions & mortality rates
│   │   ├── disease_prevalence.csv       # Chronic disease rates by age/region
│   │   ├── healthcare_costs.csv         # Cost trends by procedure & payer type
│   │   └── hospital_performance.csv     # Quality scores & wait times
│   └── healthcare_visualizations.py     # All healthcare charts & plots
│
├── requirements.txt
└── README.md
```

---

## 🚗 Automotive Industry — Critical Visualizations

### Key Metrics Covered
| Visualization | Chart Type | Insight |
|---|---|---|
| EV vs ICE Sales Trends (2015–2024) | Line + Area Chart | EV adoption acceleration |
| Top 10 Manufacturers by Market Share | Horizontal Bar | Competitive landscape |
| Fuel Efficiency by Vehicle Segment | Box Plot | MPG distribution across segments |
| Vehicle Recall Frequency by Make | Heatmap | Safety & quality risk by brand |
| EV Adoption Rate by State | Choropleth Map | Geographic adoption patterns |
| Production Volume vs Supply Chain Disruptions | Dual-axis Line | COVID/chip shortage impact |

### Sample Charts Preview
- 📈 EV sales grew **8x** from 2015 to 2024 while ICE declined 12%
- 🔥 Top recall brands and root cause analysis heatmap
- 🗺️ EV adoption hotspots: CA, WA, NY lead adoption
- 📦 Supply chain disruption in 2021–2022 cut production by 23%

---

## 🏥 Healthcare Industry — Critical Visualizations

### Key Metrics Covered
| Visualization | Chart Type | Insight |
|---|---|---|
| Hospital Readmission Rates by Condition | Bar + Error Chart | 30-day readmission risk |
| Chronic Disease Prevalence by Age Group | Stacked Bar | Age-risk correlation |
| Healthcare Cost Trends (2015–2024) | Multi-line Chart | Cost inflation analysis |
| Mortality Rate by Procedure Type | Scatter Plot | Outcome vs complexity |
| Payer Mix: Medicare/Medicaid/Private | Pie + Donut | Revenue source breakdown |
| Hospital Performance Scores vs Wait Times | Scatter + Regression | Quality-efficiency tradeoff |

### Sample Charts Preview
- 🏥 Heart failure has **21% readmission rate** — highest among chronic conditions
- 💰 Healthcare costs rose **47%** from 2015–2024, outpacing inflation 3x
- 👴 Diabetes prevalence is **4.8x higher** in 65+ vs 18–34 age group
- ⏱️ Top-performing hospitals average 28 min ER wait vs 94 min at low performers

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/mmandalapu30/industry-data-visualizations.git
cd industry-data-visualizations
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run visualizations
```bash
# Automotive dashboards
python automotive/automotive_visualizations.py

# Healthcare dashboards
python healthcare/healthcare_visualizations.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Pandas** | Data loading, cleaning, aggregation |
| **Matplotlib** | Static charts & publication-quality plots |
| **Seaborn** | Statistical visualizations |
| **Plotly** | Interactive dashboards & choropleth maps |
| **NumPy** | Numerical operations & synthetic data generation |

---

## 📊 Dataset Sources & Description

### Automotive Datasets
- `ev_sales_data.csv` — Synthetic based on IEA Global EV Outlook patterns (2015–2024)
- `fuel_efficiency.csv` — Modeled after EPA fuel economy database structure
- `vehicle_recalls.csv` — Based on NHTSA recall reporting patterns
- `production_supply_chain.csv` — Reflects OICA production statistics structure

### Healthcare Datasets
- `patient_outcomes.csv` — Modeled after CMS Hospital Compare readmission data
- `disease_prevalence.csv` — Based on CDC BRFSS chronic disease prevalence patterns
- `healthcare_costs.csv` — Reflects CMS National Health Expenditure trends
- `hospital_performance.csv` — Based on Leapfrog Hospital Safety Grade structure

> **Note:** All datasets are synthetically generated for demonstration purposes, closely mirroring real-world distributions and patterns from authoritative public sources.

---

## 👨‍💻 Author

**Mahesh Mandalapu** — Senior Data Engineer | Detroit, MI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/maheshmandalapu)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-100000?style=flat&logo=github)](https://github.com/mmandalapu30)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=flat&logo=gmail)](mailto:mmandalapu30@gmail.com)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
⭐ If this project helped you, please give it a star!
</div>
