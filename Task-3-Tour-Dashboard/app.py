import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dashboard Layout Setup
st.set_page_config(page_title="Tour Enquiry Dashboard", layout="wide")
st.title("🧳 Tour Enquiry & Analytics Dashboard")
st.write("Real-time analysis of customer travel requests and peak booking times.")

# 2. Simulated Tour Enquiry Dataset (As required by task)
np.random.seed(42)
n_records = 150
data = {
    'Destination': np.random.choice(['Goa', 'Ooty', 'Kerala', 'Manali', 'Maldives'], size=n_records),
    'Enquiry_Time': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'], size=n_records, p=[0.3, 0.2, 0.4, 0.1]),
    'User_Location': np.random.choice(['Chennai', 'Bangalore', 'Mumbai', 'Delhi'], size=n_records)
}
df = pd.DataFrame(data)

# 3. Sidebar Filter for Interactive Control
st.sidebar.header("Filter Options")
selected_loc = st.sidebar.selectbox("Select User Location:", ['All Regions'] + list(df['User_Location'].unique()))

# Filter logic based on user selection
if selected_loc != 'All Regions':
    filtered_df = df[df['User_Location'] == selected_loc]
else:
    filtered_df = df

# 4. Creating Visual Charts Layout (Side by Side)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Most Popular Destinations")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=filtered_df, x='Destination', palette='viridis', order=filtered_df['Destination'].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("⏰ Peak Enquiry Times")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=filtered_df, x='Enquiry_Time', palette='coolwarm', order=['Morning', 'Afternoon', 'Evening', 'Night'], ax=ax)
    st.pyplot(fig)

# 5. Display Clean Structured Data Table
st.subheader("📊 Filtered Raw Enquiry Dataset")
st.dataframe(filtered_df, use_container_width=True)