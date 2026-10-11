import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="Hotel Booking Dashboard", layout="wide")

st.title("🏨 Hotel Booking Demand Analysis")
st.write("An interactive dashboard exploring booking trends, cancellations, and pricing.")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("hotel_bookings.csv")
    df['agent'] = df['agent'].fillna(0)
    df['company'] = df['company'].fillna(0)
    df['country'] = df['country'].fillna('Unknown')
    df = df.dropna(subset=['children'])
    df = df.drop_duplicates()
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_hotel = st.sidebar.multiselect("Select Hotel Type", options=df['hotel'].unique(), default=df['hotel'].unique())
filtered_df = df[df['hotel'].isin(selected_hotel)]

# Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Bookings", f"{len(filtered_df):,}")
col2.metric("Total Cancelled", f"{filtered_df['is_canceled'].sum():,}")
col3.metric("Avg Price (ADR)", f"${filtered_df['adr'].mean():.2f}")

st.markdown("---")

# Visualizations
st.subheader("📊 Booking Demand & Cancellations")
col_chart1, col_chart2 = st.subplots if hasattr(st, 'subplots') else (st.columns(2))

with col_chart1:
    st.markdown("#### Hotel Demand")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x='hotel', ax=ax, palette='Blues_d')
    st.pyplot(fig)

with col_chart2:
    st.markdown("#### Cancellation Rate")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x='is_canceled', ax=ax, palette='Reds_d')
    st.pyplot(fig)

st.markdown("---")
st.subheader("📌 Summary Insights")
st.write("""
- **Lead Time:** Longer lead times strongly correlate with higher cancellation rates.
- **Seasonality:** July and August see the highest booking numbers.
- **Price:** Resort hotels have significantly higher rates during summer months.
""")
