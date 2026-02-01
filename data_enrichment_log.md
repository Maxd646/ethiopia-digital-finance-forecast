# Data Enrichment Log — Task 1

## Purpose

This document records all additional data points, events, and modeled
relationships added beyond the raw unified dataset. The goal of enrichment
is to support downstream exploratory analysis and forecasting of financial
inclusion trends in Ethiopia.

---

## Summary of Enrichment

- Added post-2021 mobile money adoption observations
- Added major policy and market-entry events
- Added impact_link assumptions connecting events to indicators
- All additions follow the unified schema and preserve reproducibility

---

## New Indicator Observations Added

### 1. Mobile Money Account Penetration (2024)

- record_type: indicator
- indicator_code: ACC_MM_ACCOUNT
- pillar: usage
- value_numeric: 9.45
- observation_date: 2024-12-31
- source_name: National Bank of Ethiopia
- source_type: administrative
- confidence: high
- rationale:
  Captures post-Telebirr and post-M-Pesa expansion period, which is
  essential for analyzing the divergence between account registration
  and active usage.

---

## New Events Added

### 1. Telebirr Launch

- record_type: event
- category: product_launch
- observation_date: 2021-05-01
- source_name: Ethio Telecom
- rationale:
  First large-scale mobile money platform in Ethiopia, marking a structural
  shift in digital financial services.

### 2. Safaricom Ethiopia Market Entry

- record_type: event
- category: market_entry
- observation_date: 2022-08-01
- source_name: Safaricom Ethiopia
- rationale:
  Introduced competition in telecom infrastructure, enabling later mobile
  money innovation.

### 3. M-Pesa Ethiopia Launch

- record_type: event
- category: product_launch
- observation_date: 2023-08-01
- source_name: Safaricom Ethiopia
- rationale:
  Second major mobile money provider, expected to accelerate usage
  through competition and interoperability.

---

## New Impact Links Added

### Event → Indicator Relationships

#### Telebirr Launch → Account Ownership

- parent_event: Telebirr Launch
- indicator_code: ACC_OWNERSHIP
- impact_direction: positive
- impact_magnitude: high
- lag_months: 12
- evidence_basis:
  GSMA and World Bank studies on mobile money-led inclusion in Sub-Saharan Africa.

#### M-Pesa Launch → Mobile Money Usage

- parent_event: M-Pesa Ethiopia Launch
- indicator_code: ACC_MM_ACCOUNT
- impact_direction: positive
- impact_magnitude: medium
- lag_months: 6
- evidence_basis:
  Observed adoption dynamics in Kenya and Tanzania following M-Pesa entry.

---

## Notes and Limitations

- Impact links represent informed hypotheses, not causal proof.
- Lag assumptions are approximate and intended for forecasting experiments.
- Some indicators lack annual granularity due to survey-based collection.

All enrichment steps are documented to ensure transparency and auditability.
Researchers should critically assess the assumptions when using enriched data
for analysis or modeling.
