import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load data
df = pd.read_csv("patients.csv")

# Title
st.title("📊 Healthcare Analytics Dashboard")

st.write("Sample dashboard for patient outcomes and readmission analysis.")

# Show data
st.subheader("Patient Dataset")
st.dataframe(df)

st.sidebar.header("Filters")

selected_diagnosis = st.sidebar.selectbox(
    "Select Diagnosis",
    ["All"] + list(df["Diagnosis"].unique())
)

if selected_diagnosis != "All":
    filtered_df = df[df["Diagnosis"] == selected_diagnosis]
else:
    filtered_df = df

# Metrics
st.subheader("Key Metrics")

total_patients = len(filtered_df)

avg_los = round(filtered_df["LengthOfStay"].mean(), 1)

readmission_rate = round(
    (filtered_df["Readmitted"] == "Yes").mean() * 100,
    1
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", total_patients)
col2.metric("Average LOS", avg_los)
col3.metric("Readmission Rate (%)", readmission_rate)

# Diagnosis summary
st.subheader("Average Length of Stay by Diagnosis")

diagnosis_summary = (
    filtered_df.groupby("Diagnosis")["LengthOfStay"]
    .mean()
    .reset_index()
)

st.dataframe(diagnosis_summary)
st.subheader("Average Length of Stay by Diagnosis")

st.bar_chart(
    diagnosis_summary.set_index("Diagnosis")
)
st.subheader("Readmission Distribution")

readmission_counts = (
    filtered_df["Readmitted"]
    .value_counts()
)

st.bar_chart(readmission_counts)
st.subheader("Patient Count by Diagnosis")

diagnosis_counts = (
    filtered_df["Diagnosis"]
    .value_counts()
)

st.bar_chart(diagnosis_counts)
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_patient_data.csv",
    mime="text/csv"
)