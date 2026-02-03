# ------------------------------
# Streamlit Dashboard for Ethiopia Financial Inclusion Forecasts
# ------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(" Ethiopia Financial Inclusion Forecasts (2025–2027)")
st.markdown("""
This dashboard allows stakeholders to:
- Explore historical financial inclusion data
- Understand event impacts on key indicators
- View forecast scenarios for 2025–2027
""")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df_hist = pd.read_csv(r"C:\Users\hp\ethiopia-financial-inclusion-forecast\data\processed\ethiopia_fi_unified_data.csv",
                      parse_dates=["observation_date"])
    df_forecast = pd.read_csv(r"C:\Users\hp\ethiopia-financial-inclusion-forecast\data\processed\ethiopia_fi_forecast_2025_2027.csv")

    return df_hist, df_forecast

df_hist, df_forecast = load_data()

# ------------------------------
# Sidebar Controls
# ------------------------------
st.sidebar.header("Controls")
selected_indicator = st.sidebar.multiselect(
    "Select Indicator(s):",
    options=df_hist['indicator_code'].unique(),
    default=df_hist['indicator_code'].unique()
)

selected_scenario = st.sidebar.selectbox(
    "Select Forecast Scenario:",
    options=["base", "optimistic", "pessimistic"]
)

date_range = st.sidebar.date_input(
    "Select Historical Date Range:",
    value=[df_hist['observation_date'].min(), df_hist['observation_date'].max()]
)

# Filter data
df_hist_filt = df_hist[
    (df_hist['indicator_code'].isin(selected_indicator)) &
    (df_hist['observation_date'] >= pd.to_datetime(date_range[0])) &
    (df_hist['observation_date'] <= pd.to_datetime(date_range[1]))
]

df_forecast_filt = df_forecast[
    (df_forecast['indicator'].isin(selected_indicator)) &
    (df_forecast['scenario'] == selected_scenario)
]

# ------------------------------
# Overview Page
# ------------------------------
st.header(" Overview")
st.markdown("Key metrics and recent trends for selected indicators:")

cols = st.columns(len(selected_indicator))
for i, ind in enumerate(selected_indicator):
    current_val = df_hist_filt[df_hist_filt['indicator_code'] == ind].sort_values('observation_date', ascending=False)['value_numeric'].iloc[0]
    growth = current_val - df_hist_filt[df_hist_filt['indicator_code'] == ind]['value_numeric'].iloc[0]
    cols[i].metric(label=f"{ind} (latest)", value=f"{current_val:.2%}", delta=f"{growth:.2%}")

# ------------------------------
# Historical Trends Page
# ------------------------------
st.header(" Historical Trends")
fig_hist = px.line(
    df_hist_filt,
    x="observation_date",
    y="value_numeric",
    color="indicator_code",
    title="Historical Financial Inclusion Indicators",
    markers=True
)
st.plotly_chart(fig_hist, use_container_width=True)

# ------------------------------
# Event Impacts Page
# ------------------------------
st.header(" Event Impacts")
impact_cols = ["parent_id", "related_indicator", "impact_direction", "impact_magnitude", "lag_months"]
if "parent_id" in df_hist.columns:
    events_df = df_hist[df_hist['record_type'] == "event"]
    st.dataframe(events_df[impact_cols].drop_duplicates())
else:
    st.info("No event-impact data available.")

# ------------------------------
# Forecasts Page
# ------------------------------
st.header(" Forecast Scenarios (2025–2027)")
fig_forecast = px.line(
    df_forecast_filt,
    x="year",
    y="forecast_scenario",
    color="indicator",
    line_dash="scenario",
    markers=True,
    title=f"Forecast Scenario: {selected_scenario.capitalize()}"
)
st.plotly_chart(fig_forecast, use_container_width=True)

# ------------------------------
# Inclusion Projections & Targets
# ------------------------------
st.header(" Financial Inclusion Projections & 60% Target")
target = 0.6
for ind in selected_indicator:
    ind_forecast = df_forecast_filt[df_forecast_filt['indicator'] == ind]
    fig_target = px.line(
        ind_forecast,
        x="year",
        y="forecast_scenario",
        title=f"{ind} Projection vs 60% Target",
        markers=True
    )
    fig_target.add_hline(y=target, line_dash="dash", line_color="red", annotation_text="60% Target", annotation_position="top left")
    st.plotly_chart(fig_target, use_container_width=True)

# ------------------------------
# Data Download
# ------------------------------
st.header(" Download Data")
st.download_button(
    label="Download Forecast Data as CSV",
    data=df_forecast_filt.to_csv(index=False),
    file_name="ethiopia_fi_forecast_2025_2027.csv",
    mime="text/csv"
)
