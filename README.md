# 📚 Library Slip Tracker | Library Analytics & Fine Management System

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red.svg)

> Built a library analytics system using Pandas and NumPy to track borrowings, automate fine calculations, identify defaulters, and generate data-driven insights from library slip records.

🌐 **Live Demo:** https://library-slip-tracker.streamlit.app/

---

## 📌 Overview

Library Slip Tracker is a Python-based analytics and management system designed to simplify library record tracking while providing actionable insights into borrowing behavior.

The project processes library slip records to monitor book borrowings, detect late returns, calculate fines automatically, identify frequent defaulters, and analyze reading trends over time.

Built using Pandas and NumPy, the system demonstrates real-world applications of data cleaning, time-series analysis, conditional transformations, aggregation operations, and reporting.

Whether used by schools, colleges, or educational institutions, Library Slip Tracker transforms raw library records into meaningful analytics through an intuitive workflow.

---

## ✨ Key Features

* 📅 Late Return Detection
* 💸 Automated Fine Calculation
* 🧑‍🎓 Borrower History Analysis
* 📚 Most Borrowed Books Identification
* 📈 Monthly Borrowing Trend Analysis
* 🚨 Defaulter Tracking
* 📊 Fine Collection Reporting
* 📥 CSV & Excel Export Support
* 🌐 Interactive Streamlit Dashboard

---

## ⚖️ Why Library Slip Tracker?

| Traditional LMS Tools                   | Library Slip Tracker                  |
| --------------------------------------- | ------------------------------------- |
| Focus on tracking and permissions       | Focus on analytics and insights       |
| Difficult to customize                  | Fully customizable and open-source    |
| Black-box dashboards                    | Transparent data pipeline             |
| Limited reporting flexibility           | Fine-grained analytics and reporting  |
| Harder to integrate with data workflows | Built entirely using Pandas and NumPy |

---

## 🏗️ System Architecture

```text
Library Slip Records
         │
         ▼
Data Cleaning & Validation
         │
         ▼
Date Processing
         │
         ▼
Fine Calculation Engine
         │
         ▼
Analytics & Insights
         │
         ▼
Visualizations & Reports
         │
         ▼
Streamlit Dashboard
```

---

## 🧠 Core Dataset Structure

The project operates on library slip records containing fields such as:

| Field               | Description            |
| ------------------- | ---------------------- |
| Slip_ID             | Unique slip identifier |
| Student_ID          | Student identifier     |
| Student_Name        | Student name           |
| Book_Title          | Borrowed book          |
| Genre               | Book genre             |
| Issue_Date          | Date of issue          |
| Due_Date            | Expected return date   |
| Return_Date         | Actual return date     |
| Fine                | Calculated penalty     |
| Department          | Student department     |
| Librarian_Issued_By | Issuing librarian      |

### Sample Record

| Slip_ID | Student_Name | Book_Title         | Issue_Date | Return_Date | Due_Date   | Fine |
| ------- | ------------ | ------------------ | ---------- | ----------- | ---------- | ---- |
| 001     | Rahul Sharma | Introduction to ML | 2024-08-01 | 2024-08-16  | 2024-08-15 | ₹5   |

---

## 📊 Analytics Performed

### 1. Late Return Detection

Identifies overdue books by comparing return dates against due dates.

```python
df["Delay_Days"] = (df["Return_Date"] - df["Due_Date"]).dt.days
```

---

### 2. Fine Calculation

Automatically calculates fines based on delayed returns.

```python
df["Fine"] = np.where(
    df["Delay_Days"] > 0,
    df["Delay_Days"] * 5,
    0
)
```

---

### 3. Borrower Behavior Analysis

Tracks:

* Total books borrowed
* Average delay duration
* Total fines accumulated
* Borrowing frequency

---

### 4. Book Popularity Analysis

Identifies:

* Most borrowed books
* Popular genres
* Frequently issued titles

---

### 5. Monthly Borrowing Trends

Analyzes:

* Monthly borrowing volume
* Seasonal reading patterns
* Library usage trends

---

### 6. Defaulter Identification

Detects students with:

* Repeated late returns
* High accumulated fines
* Poor submission history

---

## 📈 Project Statistics

| Metric                  | Value         |
| ----------------------- | ------------- |
| Records Processed       | 500+          |
| Analytics Modules       | 6+            |
| Fine Calculation System | Automated     |
| Export Formats          | CSV, XLSX     |
| Dashboard               | Streamlit     |
| Core Libraries          | Pandas, NumPy |

---

## 📸 Screenshots

### Dashboard Overview

![Dashboard](screenshots/dashboard.png)

### Borrowing Trends

![Borrowing Trends](screenshots/borrowing-trends.png)

### Fine Analysis

![Fine Analysis](screenshots/fine-analysis.png)

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Web Application

* Streamlit

### Development Environment

* Google Colab
* VS Code

---

## 📂 Project Structure

```text
library-slip-tracker/
│
├── data/
│   └── slips.csv
│
├── src/
│   ├── slip_analysis.py
│   ├── fine_calculator.py
│   └── cli_interface.py
│
├── visuals/
│   └── charts.png
│
├── screenshots/
│   ├── dashboard.png
│   ├── borrowing-trends.png
│   └── fine-analysis.png
│
├── tracker.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shrisha337-beep/Library-Slip-Tracker.git

cd Library-Slip-Tracker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📊 Example Outputs

The system can generate:

* 📈 Monthly Borrowing Reports
* 💸 Fine Distribution Analysis
* 🏆 Most Borrowed Books Rankings
* 🚨 Defaulter Leaderboards
* 📅 Borrowing Trend Visualizations
* 📥 Exportable CSV/XLSX Reports

---

## 📄 Research Publication

This project contributed to a research paper presented at an international technical conference focusing on library analytics, fine management systems, and data-driven educational resource tracking.

---

## 🚀 Future Enhancements

* Google Sheets Integration
* Email Notifications for Due Dates
* Automated Reminder System
* AI-Based Book Recommendation Engine
* Student Reading Analytics Dashboard
* Multi-Library Support
* Cloud Database Integration

---

## 👩‍💻 Author

**Shrisha**

Computer Science Engineering Student
Ajay Kumar Garg Engineering College (AKGEC)

### Connect With Me

* GitHub: https://github.com/shrisha337-beep
* LinkedIn: [(https://www.linkedin.com/in/shri04/)
](url)
---

## 📄 License

This project is licensed under the MIT License.
