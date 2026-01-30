# Forecasting Financial Inclusion in Ethiopia

## Project Overview
This repository contains a data science and forecasting system designed to track, explain, and forecast Ethiopia’s financial inclusion trajectory using time series methods, event impact modeling, and scenario-based projections.

The project is developed in the context of Ethiopia’s rapid digital financial transformation, marked by the expansion of mobile money platforms (Telebirr, M-Pesa), payment infrastructure growth, and major regulatory reforms. Despite strong supply-side growth, demand-side financial inclusion indicators (as measured by the World Bank Global Findex) have shown signs of deceleration. This project aims to explain that divergence and forecast future outcomes.

The work is carried out as a policy- and decision-oriented analytics exercise, suitable for regulators, development finance institutions, and financial service providers.

---

## Business Problem
Stakeholders seek to understand:

- What factors drive financial inclusion in Ethiopia
- How policies, product launches, and infrastructure investments affect inclusion outcomes
- How financial inclusion evolved in 2025 and how it is expected to change in 2026–2027

The system focuses on the two Global Findex core dimensions:

- **Access**: Account Ownership Rate
- **Usage**: Digital Payment Adoption Rate

---

## Objectives

1. Build a unified, extensible dataset combining survey data, administrative data, and event metadata
2. Analyze historical trends and structural breaks in financial inclusion indicators
3. Model the impact of national and sectoral events on access and usage
4. Forecast financial inclusion outcomes under multiple scenarios (baseline, optimistic, pessimistic)
5. Communicate results through a transparent methodology and an interactive dashboard

---

## Data Sources

### Core Dataset
- **Global Findex Database** (2011–2024)
- Starter dataset: `ethiopia_fi_unified_data.csv`

### Enriched Data (Task 1)
- IMF Financial Access Survey (FAS)
- National Bank of Ethiopia publications
- GSMA mobile money indicators
- Ethio Telecom and mobile network coverage reports
- Digital ID (Fayda) program updates
- Market intelligence (e.g., Shega Media)

All data additions follow a unified schema and are fully documented in `data_enrichment_log.md`.

---

## Methodology

### 1. Data Architecture
The project uses a unified data schema where all records share the same structure. Each row is interpreted using a `record_type` field:

- **observation**: Measured indicators (survey, administrative, infrastructure data)
- **event**: Policies, product launches, regulatory changes, milestones
- **impact_link**: Modeled relationships between events and indicators
- **target**: Official policy goals (e.g., NFIS-II targets)

This design avoids bias by not pre-assigning events to pillars. Event effects are captured explicitly through `impact_link` records.

### 2. Exploratory Data Analysis (Task 2)
- Temporal coverage and data quality assessment
- Growth rate and trend analysis for access and usage
- Gender and urban–rural gaps (where data permits)
- Infrastructure and enabler analysis
- Event timeline overlays and correlation analysis

### 3. Event Impact Modeling (Task 3)
- Construction of an event–indicator association matrix
- Use of lagged intervention variables
- Incorporation of comparable-country evidence where local data is sparse
- Validation against observed post-event changes

### 4. Forecasting (Task 4)
Given limited historical survey points, multiple approaches are combined:

- Trend-based regression models
- Event-augmented forecasting models
- Scenario analysis with explicit uncertainty bounds

Forecasts are produced for 2025–2027 for both access and usage indicators.

### 5. Visualization and Communication (Task 5)
- Interactive Streamlit dashboard
- Time series exploration
- Event overlays
- Scenario-based forecast views
- Progress toward national financial inclusion targets

---

## Repository Structure

```
ethiopia-financial-inclusion-forecast/
│
├── data/            # Raw, external, interim, and processed datasets
├── notebooks/       # Analysis and modeling notebooks
├── src/             # Reusable data, feature, and model code
├── models/          # Saved model artifacts
├── dashboard/       # Streamlit application
├── reports/         # Figures, tables, and final written outputs
├── tests/           # Unit tests
├── data_enrichment_log.md
├── requirements.txt
└── README.md
```

---

## Dashboard

The interactive dashboard allows users to:

- Explore financial inclusion trends over time
- View the timing and impact of major events
- Compare baseline and scenario-based forecasts
- Track progress toward national inclusion targets

To run the dashboard locally:

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

---

## Key Assumptions and Limitations

- Financial inclusion survey data is sparse and collected at multi-year intervals
- Event impact magnitudes rely partly on comparable-country evidence
- Administrative data may not align perfectly with demand-side survey definitions
- Forecast uncertainty is intentionally wide to reflect data limitations

All assumptions are explicitly documented in notebooks and reports.

---

## Outputs

- Enriched financial inclusion dataset
- Exploratory data analysis notebooks
- Event–indicator association matrix
- Forecast tables with confidence intervals
- Scenario visualizations
- Interactive dashboard
- Final analytical report (blog-style)

---

## Intended Audience

- Financial regulators and policymakers
- Development finance institutions
- Mobile money operators and banks
- Researchers and analysts working on financial inclusion

---

## License

This project is provided for educational and analytical purposes. Data sources retain their original licenses and attribution requirements.