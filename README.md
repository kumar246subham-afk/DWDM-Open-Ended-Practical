# 📊 Marwadi University — Department of Computer Engineering
## 01CE0527 &ndash; Data Warehousing and Data Mining (DWDM)
### Open-Ended Practical: Designing Candlesticks using 5-Number Summary

[![Marwadi University](https://img.shields.io/badge/Marwadi_University-NAAC_A%2B-red?style=for-the-badge)](https://www.marwadiuniversity.ac.in/)
[![Course](https://img.shields.io/badge/Course-01CE0527_DWDM-blue?style=for-the-badge)](https://www.marwadiuniversity.ac.in/)
[![Python](https://img.shields.io/badge/Python-3.13-yellow?style=for-the-badge&logo=python)](https://python.org)
[![Pages](https://img.shields.io/badge/Submission_Length-Exactly_6_Pages-success?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Verified-100%25_Complete-brightgreen?style=for-the-badge)]()

---

## 📌 Practical Overview & Problem Statement

> **Problem Statement (As assigned in PDF):**  
> *"Design candles (daily/weekly/monthly) of any 3 stock market-listed companies using the 5 Number Summary.*  
> *Submission in (Printed document, Pages: 5-6, Single side Print)"*

---

## 🏫 Academic Credentials

- **University**: Marwadi University, Rajkot, Gujarat (NAAC A+ Accredited)
- **Faculty**: Faculty of Engineering & Technology
- **Department**: Department of Computer Engineering
- **Program & Semester**: B.Tech Computer Engineering &bull; Semester 5
- **Course Code & Title**: `01CE0527` &ndash; Data Warehousing and Data Mining (DWDM)
- **Subject Faculties**:
  - **Dr. Sivakumar Nadarajan**
  - **Prof. Urvi Dhamecha**
  - **Prof. Sahir Suma**
- **Head of Department**:
  - **Dr. Krunal Vaghela** (Dept. Computer Engineering)
- **Student Name**: **Subham Kumar Keshari**
- **GitHub Repository**: [kumar246subham-afk/DWDM-Open-Ended-Practical](https://github.com/kumar246subham-afk/DWDM-Open-Ended-Practical)

---

## 📈 Companies Analyzed

We analyzed three prominent blue-chip equities listed on the **National Stock Exchange (NSE)** representing diverse market sectors:

| No. | Company Name | Ticker | Sector / Industry | Market Capitalization Class |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Tata Consultancy Services Ltd.** | `NSE: TCS` | Information Technology & Services | Mega Cap (NIFTY 50 Benchmark) |
| **2** | **Reliance Industries Limited** | `NSE: RELIANCE` | Energy, Petrochemicals & Telecom | Mega Cap (#1 Market Cap in India) |
| **3** | **Infosys Limited** | `NSE: INFY` | Technology & Consulting | Large Cap (NIFTY IT Volatility Driver) |

---

## 📐 Mathematical Formulation of the 5-Number Summary

The Five-Number Summary is a descriptive statistic that summarizes a dataset through five non-parametric order statistics:

1. **Minimum ($Min = x_{(1)}$)**: The lowest transaction price in the given temporal window.
2. **First Quartile ($Q_1$ / 25th Percentile)**: Value separating the lowest 25% of trading observations.
3. **Median ($Q_2$ / 50th Percentile)**: The middle value representing the robust central equilibrium price.
4. **Third Quartile ($Q_3$ / 75th Percentile)**: Value separating the lowest 75% of trading observations.
5. **Maximum ($Max = x_{(N)}$)**: The highest transaction price in the given temporal window.

### Key Derived Metrics:
- **Interquartile Range ($IQR$)**:  
  $$IQR = Q_3 - Q_1$$  
  *Measures core volatility (middle 50% price dispersion).*
- **Lower Outlier Boundary ($LF$)**:  
  $$LF = Q_1 - 1.5 \times IQR$$
- **Upper Outlier Boundary ($UF$)**:  
  $$UF = Q_3 + 1.5 \times IQR$$
- **Bowley Skewness Coefficient ($S_k$)**:  
  $$S_k = \frac{(Q_3 - Q_2) - (Q_2 - Q_1)}{Q_3 - Q_1}$$

---

## 🕯️ Candlestick Design from 5-Number Summary

Unlike traditional financial candlesticks that rely solely on 4 discrete boundary points ($Open, High, Low, Close$), our **Distribution Box-Candles** utilize the full statistical density of price observations:

```
          Max ────┬──── Upper Extreme Cap
                  │
                  │   Upper Whisker (Max - Q3)
                  │   (Selling pressure / Rejection)
                  │
            Q3 ┌──┴──┐
               │     │
               │     │   Candle Body (IQR: Q1 to Q3)
               │     │   (Middle 50% Dense Trading Zone)
               ├─────┤ ◄ Median (Q2) Line
               │     │
               │     │
            Q1 └──┬──┘
                  │
                  │   Lower Whisker (Q1 - Min)
                  │   (Buying support / Absorption)
                  │
          Min ────┴──── Lower Extreme Cap
```

---

## 📊 Summary of Computed Results

### 1. Tata Consultancy Services (TCS)
- **Daily Candle**: $Min = 4142.50$, $Q_1 = 4168.60$, $Median = 4188.75$, $Q_3 = 4210.25$, $Max = 4225.00$ &bull; **$IQR = ₹41.65$**
- **Weekly Candle**: $Min = 4095.00$, $Q_1 = 4141.50$, $Median = 4177.50$, $Q_3 = 4218.75$, $Max = 4268.00$ &bull; **$IQR = ₹77.25$**
- **Monthly Candle**: $Min = 3980.00$, $Q_1 = 4100.00$, $Median = 4192.50$, $Q_3 = 4280.00$, $Max = 4345.00$ &bull; **$IQR = ₹180.00$**

### 2. Reliance Industries Limited (RELIANCE)
- **Daily Candle**: $Min = 2715.00$, $Q_1 = 2736.75$, $Median = 2754.00$, $Q_3 = 2774.00$, $Max = 2795.50$ &bull; **$IQR = ₹37.25$**
- **Weekly Candle**: $Min = 2685.00$, $Q_1 = 2726.50$, $Median = 2769.00$, $Q_3 = 2806.25$, $Max = 2830.00$ &bull; **$IQR = ₹79.75$**
- **Monthly Candle**: $Min = 2620.00$, $Q_1 = 2708.75$, $Median = 2790.00$, $Q_3 = 2853.75$, $Max = 2895.00$ &bull; **$IQR = ₹145.00$**

### 3. Infosys Limited (INFY)
- **Daily Candle**: $Min = 1855.00$, $Q_1 = 1872.00$, $Median = 1891.75$, $Q_3 = 1908.00$, $Max = 1922.00$ &bull; **$IQR = ₹36.00$**
- **Weekly Candle**: $Min = 1830.00$, $Q_1 = 1871.50$, $Median = 1903.50$, $Q_3 = 1939.00$, $Max = 1958.00$ &bull; **$IQR = ₹67.50$**
- **Monthly Candle**: $Min = 1785.00$, $Q_1 = 1861.25$, $Median = 1925.00$, $Q_3 = 1980.00$, $Max = 2010.00$ &bull; **$IQR = ₹118.75$**

---

## 📑 Structure of the 6-Page Submission Document

The generated PDF matches the strict requirement: **"Submission in (Printed document, Pages: 5-6, Single side Print)"**:

- **Page 1**: Official Marwadi University Header, Academic Metadata, Introduction to 5-Number Summary in DWDM, Mathematical Formulations & Anatomical Mapping.
- **Page 2**: Multi-Timeframe Analytical Framework (Daily, Weekly, Monthly), Company Profiles, Data ETL Pipeline & Candle Anatomy Table.
- **Page 3**: Company 1 &ndash; **Tata Consultancy Services (TCS)** (Observation Data, Calculations, 3 Multi-Timeframe Candle Plots, Analytical Discussion).
- **Page 4**: Company 2 &ndash; **Reliance Industries Limited (RELIANCE)** (Observation Data, Calculations, 3 Multi-Timeframe Candle Plots, Analytical Discussion).
- **Page 5**: Company 3 &ndash; **Infosys Limited (INFY)** (Observation Data, Calculations, 3 Multi-Timeframe Candle Plots, Analytical Discussion).
- **Page 6**: Cross-Company Volatility Synthesis, Comparison Bar Chart, Python Implementation Snippet, Key Findings, Conclusion, References, and Official Faculty & HOD Sign-off Block.

---

## 🚀 How to Run the Code Locally

```bash
# 1. Clone repository
git clone https://github.com/kumar246subham-afk/DWDM-Open-Ended-Practical.git
cd DWDM-Open-Ended-Practical

# 2. Run Python scripts
python generate_charts.py
python render_pdf.py

# 3. View the generated PDF / HTML
start DWDM_Open_Ended_Practical_5NumberSummary.pdf
```

---

## 👨‍💻 Author

- **Student**: **Subham Kumar Keshari**
- **Degree**: B.Tech Computer Engineering (Semester 5)
- **Institution**: Marwadi University, Rajkot, Gujarat
- **Subject**: 01CE0527 &ndash; Data Warehousing and Data Mining (DWDM)
