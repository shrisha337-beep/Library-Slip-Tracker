import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Library Slip Tracker", layout="wide")
st.title("📚 Library Slip Tracker Dashboard")
st.write("An interactive ML/Data analytics app to monitor book borrowings, calculate fines, and analyze reader behavior.")

# Load the dataset
@st.cache_data
def load_data():
    # Reading your repository's CSV file
    df = pd.read_csv("library_slip_tracker.csv")
    # Convert date columns to datetime if they exist
    for col in ["Issue_Date", "Return_Date", "Due_Date", "Date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    return df

try:
    df = load_data()
    
    # --- METRICS SECTION ---
    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_records = len(df)
        st.metric("Total Records", total_records)
        
    with col2:
        # Checking for defaulters based on your input/output table
        if "Slip Submitted" in df.columns:
            defaulters = df[df["Slip Submitted"].str.lower() == "no"]
            defaulter_count = len(defaulters)
            submission_rate = ((total_records - defaulter_count) / total_records) * 100
            st.metric("Defaulter Count", defaulter_count)
        else:
            st.metric("Defaulter Count", "N/A (Column Missing)")
            submission_rate = 100
            
    with col3:
        st.metric("Slip Submission Rate", f"{submission_rate:.1f}%")

    # --- FINE CALCULATOR TESTER ---
    st.markdown("---")
    st.subheader("💸 Live Fine Calculator Simulation")
    
    input_name = st.text_input("Student Name", "Rahul Sharma")
    input_status = st.selectbox("Slip Submitted?", ["Yes", "No"])
    
    # Simple rule based on your README rules
    fine = 0 if input_status == "Yes" else 5
    st.success(f"Calculated Fine Amount for {input_name}: ₹{fine}")

    # --- DATA VIEW ---
    st.markdown("---")
    st.subheader("🔍 Raw Data Explorer")
    st.dataframe(df)

except Exception as e:
    st.error(f"Error loading dashboard: {e}")
    st.info("Make sure 'library_slip_tracker.csv' matches your data schema format.")
