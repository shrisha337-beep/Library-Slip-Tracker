import streamlit as st
import pandas as pd
import numpy as np
import csv

st.set_page_config(page_title="Library Slip Tracker", layout="wide")
st.title("📚 Library Slip Tracker Dashboard")
st.write("An interactive analytics app to monitor book borrowings, calculate fines, and analyze reader behavior.")

# Load the dataset safely
@st.cache_data
def load_data():
    try:
        # Using the bypass rule we established earlier to prevent crashes
        df = pd.read_csv("library_slip_tracker.csv", quoting=csv.QUOTE_NONE, on_bad_lines='skip')
        
        # Clean column names (remove whitespace and quotes that might come from raw text files)
        df.columns = df.columns.str.replace('"', '').str.replace("'", "").str.strip()
        
        # Standardize date columns if they exist
        for col in ["Issue_Date", "Return_Date", "Due_Date", "Date"]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        return df
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    # --- AUTOMATIC COLUMN DETECTION ---
    # Since CSV structures differ, let's map whatever columns you have available
    cols = {c.lower().replace(" ", "_"): c for c in df.columns}
    
    name_col = cols.get("student_name") or cols.get("name") or df.columns[1]
    roll_col = cols.get("roll_number") or cols.get("roll_no") or cols.get("student_id") or (df.columns[2] if len(df.columns) > 2 else df.columns[0])
    slip_col = cols.get("slip_submitted") or cols.get("submitted")
    fine_col = cols.get("fine_amount") or cols.get("fine")

    # --- METRICS SECTION ---
    st.subheader("📊 Key System Metrics")
    col1, col2, col3 = st.columns(3)
    
    total_records = len(df)
    with col1:
        st.metric("Total Records Tracked", total_records)
        
    with col2:
        if slip_col:
            # Check for records where slip wasn't submitted
            defaulter_count = df[df[slip_col].astype(str).str.strip().str.lower() == "no"].shape[0]
            submission_rate = ((total_records - defaulter_count) / total_records) * 100
            st.metric("Defaulter Count", defaulter_count)
        else:
            defaulter_count = "N/A"
            submission_rate = 100
            st.metric("Defaulters", "No Submission Column")
            
    with col3:
        st.metric("Slip Submission Rate", f"{submission_rate:.1f}%")

    # --- LIVE STUDENT SEARCH & DYNAMIC FINE CHECKER ---
    st.markdown("---")
    st.subheader("🔍 Live Student Record & Fine Lookup")
    st.write("Search for a student using their Roll Number or Name to pull live records and calculate actual fines.")

    # Create search filters
    search_option = st.radio("Search by:", ["Roll Number / ID", "Student Name"], horizontal=True)
    
    if search_option == "Roll Number / ID":
        # Get unique values for dropdown or let them type
        unique_rolls = df[roll_col].dropna().unique()
        search_input = st.selectbox("Select or Type Roll Number", unique_rolls)
        student_records = df[df[roll_col].astype(str) == str(search_input)]
    else:
        unique_names = df[name_col].dropna().unique()
        search_input = st.selectbox("Select or Type Student Name", unique_names)
        student_records = df[df[name_col].astype(str) == str(search_input)]

    # Process search results dynamically
    if not student_records.empty:
        st.success(f"Found {len(student_records)} record(s) for: **{search_input}**")
        
        # Display the specific student's rows
        st.dataframe(student_records)
        
        # Calculate fine dynamically for this specific student
        st.markdown("#### 💸 Fine Breakdown")
        
        for idx, row in student_records.iterrows():
            book_title = row.get("Book_Title") or row.get("Book") or "Assigned Item"
            
            # Check if there's a pre-calculated fine column
            if fine_col and pd.notna(row[fine_col]):
                actual_fine = row[fine_col]
            else:
                # If no fine column exists, calculate dynamically using the rules from your README
                if slip_col:
                    status = str(row[slip_col]).strip().lower()
                    actual_fine = 0 if status in ["yes", "true", "1"] else 2  # ₹2 rule from your README
                else:
                    actual_fine = 0
            
            st.warning(f"👉 **Book:** {book_title} | **Current Owed Fine:** ₹{actual_fine}")
            
    else:
        st.info("No matching student records found. Try adjusting your search query.")

    # --- DATA VIEW ---
    st.markdown("---")
    st.subheader("📋 Entire Database Explorer")
    st.dataframe(df)

else:
    st.warning("The dataset is empty or could not be compiled properly. Check your CSV formatting.")