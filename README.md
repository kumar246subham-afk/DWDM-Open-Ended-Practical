# 📊 Marwadi University — Department of Computer Engineering
## 01CE0527 &ndash; Data Warehousing and Data Mining (DWDM)

[![Marwadi University](https://img.shields.io/badge/Marwadi_University-NAAC_A%2B-red?style=for-the-badge)](https://www.marwadiuniversity.ac.in/)
[![Course](https://img.shields.io/badge/Course-01CE0527_DWDM-blue?style=for-the-badge)](https://www.marwadiuniversity.ac.in/)
[![Student](https://img.shields.io/badge/Student-Subham_Kumar_Keshari-blueviolet?style=for-the-badge)]()
[![Enrolment](https://img.shields.io/badge/Enrolment-92400103120-orange?style=for-the-badge)]()
[![Pages](https://img.shields.io/badge/Practical_4_Length-Exactly_6_Pages-success?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Verified-100%25_Complete-brightgreen?style=for-the-badge)]()

---

## 🏫 Academic Credentials & Submission Details

- **University**: Marwadi University, Rajkot, Gujarat (NAAC A+ Accredited)
- **Faculty**: Faculty of Engineering & Technology
- **Department**: Department of Computer Engineering
- **Course Code & Title**: `01CE0527` &ndash; Data Warehousing and Data Mining (DWDM)
- **Subject Faculties**:
  - **Dr. Sivakumar Nadarajan**
  - **Prof. Urvi Dhamecha**
  - **Prof. Sahir Suma**
- **Head of Department**:
  - **Dr. Krunal Vaghela** (Dept. of Computer Engineering)
- **Full Name**: **Subham Kumar Keshari**
- **Enrolment Number**: **92400103120**
- **Format**: Single-Side Print, Page Numbering starting from Page 1 (Page 1 of 6 to Page 6 of 6)

---

## 📑 Practical 4: Data Preprocessing Using a Sample Dataset

### 🎯 Aim
To apply data preprocessing techniques—including data cleaning, handling missing values, noise smoothing (binning), min-max normalization, categorical encoding (Label & One-Hot Encoding), and feature selection—on a real-world multi-attribute student/customer sample dataset.

### 🧠 Learning Outcomes
1. Understand real-world data quality issues: missing attributes, inconsistent casing, duplicate records, outliers, and untyped features.
2. Implement statistical imputation: mean/median imputation for continuous variables and mode imputation for categorical attributes.
3. Apply data smoothing via binning (equal-frequency and bin means) to mitigate variance.
4. Scale continuous features into a bounded range $[0, 1]$ using Min-Max Normalization.
5. Encode categorical nominal and ordinal data using Label Encoding and One-Hot Encoding.
6. Perform feature selection and dimensionality reduction to eliminate zero-variance and redundant identifiers (`StudentID`).

---

### 📋 Sample Dataset Before Preprocessing

| StudentID | Age | City | Score | Grade | PurchasedCourse |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **S101** | 21 | Mumbai | 85 | B | Yes |
| **S102** | 23 | Delhi | 92 | A | No |
| **S103** | `NaN` | Pune | `NaN` | B | Yes |
| **S104** | 20 | delhi *(lower)* | 78 | C | No |
| **S105** | 22 | Bangalore | 88 | B | Yes |
| **S106** | 25 | Pune | 60 | D | No |
| **S107** | 21 | `NaN` | 95 | A | Yes |
| **S108** | 23 | Delhi | 92 | A | No *(Duplicate of S102)* |
| **S109** | 24 | Mumbai | 81 | B | Yes |
| **S110** | 22 | Ahmedabad | 87 | B | Yes |

---

### 🛠️ Data Preprocessing Pipeline & Techniques

1. **Duplicate Detection & Removal**:
   - `S108` was an exact duplicate of `S102` (Age=23, City=Delhi, Score=92, Grade=A, PurchasedCourse=No). Dropped to maintain sample independence.
2. **Handling Missing Values**:
   - Missing `Age` in `S103` imputed using median age: $\text{Median}(\text{Age}) = 22.0$.
   - Missing `Score` in `S103` imputed using mean score: $\text{Mean}(\text{Score}) = 84.6 \approx 85.0$.
   - Missing `City` in `S107` imputed using statistical mode: $\text{Mode}(\text{City}) = \text{"Delhi"}$.
3. **Data Cleaning & Standardization**:
   - Casing inconsistency in `S104` (`"delhi"` $\rightarrow$ `"Delhi"`). Standardized strings across the dataset.
4. **Data Smoothing (Binning)**:
   - Equal-frequency binning applied to `Score` with 3 bins (Low, Medium, High) and smoothing by bin means.
5. **Min-Max Normalization**:
   $$v' = \frac{v - \min(A)}{\max(A) - \min(A)}$$
   - Mapped `Age` ($\min=20, \max=25$) and `Score` ($\min=60, \max=95$) strictly into $[0, 1]$.
6. **Categorical Encoding**:
   - **Label Encoding**: Ordinal Grade mapping (`D: 0, C: 1, B: 2, A: 3`).
   - **One-Hot Encoding**: Nominal City mapping (`City_Ahmedabad`, `City_Bangalore`, `City_Delhi`, `City_Mumbai`, `City_Pune`) and Target (`PurchasedCourse_Yes`).
7. **Feature Selection**:
   - Dropped non-informative identifier attribute `StudentID`.

---

### 📊 Cleaned & Normalized Dataset

| StudentID | Age (Raw) | Age (Norm) | City | Score (Raw) | Score (Norm) | Grade | PurchasedCourse |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **S101** | 21 | 0.20 | Mumbai | 85 | 0.714 | B | Yes |
| **S102** | 23 | 0.60 | Delhi | 92 | 0.914 | A | No |
| **S103** | 22 *(Imp)* | 0.40 | Pune | 85 *(Imp)* | 0.714 | B | Yes |
| **S104** | 20 | 0.00 | Delhi | 78 | 0.514 | C | No |
| **S105** | 22 | 0.40 | Bangalore | 88 | 0.800 | B | Yes |
| **S106** | 25 | 1.00 | Pune | 60 | 0.000 | D | No |
| **S107** | 21 | 0.20 | Delhi *(Imp)* | 95 | 1.000 | A | Yes |
| **S109** | 24 | 0.80 | Mumbai | 81 | 0.600 | B | Yes |
| **S110** | 22 | 0.40 | Ahmedabad | 87 | 0.771 | B | Yes |

---

### 🔍 Special Deep-Dive: S103 Multi-Step Transformation

| Preprocessing Stage | Age Value | Score Value | Transformation Description |
| :--- | :---: | :---: | :--- |
| **1. Raw Input State** | `NaN` | `NaN` | Missing both numerical attributes upon ingestion. |
| **2. Missing Imputation** | `22.0` | `84.6` | Imputed using Median (Age) and Mean (Score). |
| **3. Binning & Smoothing**| `22.0` | `84.6` | Assigned to Medium Bin $[78, 88]$. |
| **4. Min-Max Normalization**| `0.400` | `0.714` | Normalized: $\frac{22-20}{25-20}=0.400$, $\frac{85-60}{95-60}=0.714$. |

---

## 📂 Project Repository Structure

```text
├── DWDM_Practical_4_Data_Preprocessing.pdf    # Complete 6-Page Printable Report (Official Format)
├── DWDM_Practical_4_Data_Preprocessing.html   # Source HTML Template with Print Stylesheet
├── build_practical4_report.py                 # Edge Headless PDF Compiler Script
├── generate_practical4.py                     # Preprocessing Pipeline & Plot Generator
├── check_pages.py                             # Automated PDF Page Count Verifier (Strict 6 Pages)
├── charts/                                    # Generated Dark-Themed IDE Execution Code Screenshots
│   ├── screenshot_1.png                       # Cleaning & Imputation Code Screenshot
│   ├── screenshot_2.png                       # Normalization & Encoding Code Screenshot
│   └── screenshot_3.png                       # Feature Selection & Modeling Pipeline Screenshot
├── DWDM_Open_Ended_Practical_Report.html      # Open-Ended Practical: 5-Number Summary Candlesticks
├── DWDM_Open_Ended_Practical_Report.pdf       # Open-Ended Practical Printable PDF
└── README.md                                  # Repository Documentation
```

---

## 🚀 How to Run & Verify

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kumar246subham-afk/DWDM-Open-Ended-Practical.git
   cd DWDM-Open-Ended-Practical
   ```

2. **Generate Charts and Screenshots**:
   ```bash
   python generate_practical4.py
   ```

3. **Compile Practical 4 PDF**:
   ```bash
   python build_practical4_report.py
   ```

4. **Verify 6-Page PDF**:
   ```bash
   python check_pages.py
   # Output: Total Pages in PDF: 6
   ```

---

## 👨‍🎓 Submitted By
- **Name**: **Subham Kumar Keshari**
- **Enrolment Number**: **92400103120**
- **Department**: Department of Computer Engineering
- **Institute**: Faculty of Engineering & Technology, Marwadi University
