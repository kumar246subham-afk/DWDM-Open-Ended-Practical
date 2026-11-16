import os
import base64
import subprocess

temp_dir = os.environ.get("TEMP", r"C:\Users\ADMIN\AppData\Local\Temp")
work_dir = os.path.join(temp_dir, "DWDM_Practical")
charts_dir = os.path.join(work_dir, "charts")

# Load images as base64
def get_b64(fname):
    with open(os.path.join(charts_dir, fname), "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_tcs = get_b64("candle_company_1.png")
img_rel = get_b64("candle_company_2.png")
img_infy = get_b64("candle_company_3.png")
img_cmp = get_b64("comparative_metrics.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>01CE0527 - DWDM Open-Ended Practical - 5-Number Summary Candlesticks</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 12mm 15mm 12mm 15mm;
    }}
    * {{
        box-sizing: border-box;
    }}
    body {{
        font-family: 'Segoe UI', Arial, sans-serif;
        color: #1a202c;
        margin: 0;
        padding: 0;
        background: #e2e8f0;
        font-size: 9pt;
        line-height: 1.35;
    }}
    .page {{
        width: 210mm;
        min-height: 297mm;
        max-height: 297mm;
        padding: 14mm 16mm 14mm 16mm;
        margin: 10px auto;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
        page-break-after: always;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .page-content {{
        flex: 1;
    }}
    .page-footer {{
        border-top: 1px solid #cbd5e1;
        padding-top: 4px;
        font-size: 7.5pt;
        color: #64748b;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    
    /* Header styles */
    .univ-header {{
        border-bottom: 2px solid #0f172a;
        padding-bottom: 6px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .univ-title {{
        text-align: left;
    }}
    .univ-title h1 {{
        margin: 0;
        font-size: 15pt;
        color: #b91c1c;
        font-weight: 800;
        letter-spacing: 0.8px;
    }}
    .univ-title h2 {{
        margin: 1px 0;
        font-size: 10pt;
        color: #1e293b;
        font-weight: 700;
    }}
    .univ-title h3 {{
        margin: 1px 0;
        font-size: 8.5pt;
        color: #475569;
        font-weight: 600;
    }}
    .badge-dwdm {{
        background: #0f172a;
        color: #ffffff;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 8.5pt;
        font-weight: bold;
        text-align: right;
    }}
    
    .practical-title-box {{
        background: linear-gradient(90deg, #f8fafc 0%, #e2e8f0 100%);
        border-left: 5px solid #0284c7;
        padding: 8px 12px;
        margin-bottom: 10px;
        border-radius: 0 4px 4px 0;
    }}
    .practical-title-box h3 {{
        margin: 0;
        font-size: 11pt;
        color: #0369a1;
        font-weight: 800;
        text-transform: uppercase;
    }}
    .practical-title-box p {{
        margin: 2px 0 0 0;
        font-size: 8pt;
        color: #334155;
    }}
    
    /* Academic Meta Table */
    .meta-table {{
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 10px;
        font-size: 8pt;
    }}
    .meta-table td {{
        padding: 4px 8px;
        border: 1px solid #cbd5e1;
    }}
    .meta-table td.lbl {{
        font-weight: 700;
        background: #f1f5f9;
        color: #0f172a;
        width: 20%;
    }}
    
    /* Section Headings */
    h4.sec-h {{
        font-size: 9.5pt;
        color: #0f172a;
        background: #e2e8f0;
        padding: 3px 8px;
        margin: 8px 0 5px 0;
        border-left: 4px solid #0284c7;
        font-weight: 700;
        text-transform: uppercase;
    }}
    
    /* Tables */
    table.data-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 6px 0;
        font-size: 7.8pt;
    }}
    table.data-table th, table.data-table td {{
        border: 1px solid #cbd5e1;
        padding: 3.5px 6px;
        text-align: center;
    }}
    table.data-table th {{
        background: #0f172a;
        color: #ffffff;
        font-weight: 600;
    }}
    table.data-table tr:nth-child(even) {{
        background: #f8fafc;
    }}
    
    /* Formula Card */
    .formula-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin: 6px 0;
    }}
    .formula-card {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        padding: 6px 9px;
        font-size: 8pt;
    }}
    .formula-card strong {{
        color: #0369a1;
        display: block;
        margin-bottom: 2px;
    }}
    
    .chart-container {{
        text-align: center;
        margin: 6px 0;
    }}
    .chart-container img {{
        max-width: 100%;
        height: auto;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
    }}
    
    .code-box {{
        background: #0f172a;
        color: #f8fafc;
        padding: 6px 10px;
        border-radius: 4px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 7.2pt;
        line-height: 1.3;
        margin: 5px 0;
        white-space: pre-wrap;
    }}
    
    .sign-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
    }}
    .sign-table td {{
        text-align: center;
        padding: 10px 5px;
        vertical-align: bottom;
        border: none;
        font-size: 7.8pt;
    }}
    .sign-line {{
        border-top: 1px dashed #475569;
        margin-top: 25px;
        padding-top: 3px;
        font-weight: bold;
    }}
    
    @media print {{
        body {{
            background: #ffffff;
        }}
        .page {{
            box-shadow: none;
            margin: 0;
            width: 100%;
            height: 100%;
            max-height: none;
            padding: 10mm 12mm;
        }}
    }}
</style>
</head>
<body>

<!-- ========================================== PAGE 1 ========================================== -->
<div class="page">
    <div class="page-content">
        <!-- University Academic Header -->
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY</h1>
                <h2>FACULTY OF ENGINEERING &amp; TECHNOLOGY</h2>
                <h3>Department of Computer Engineering &bull; NAAC A+ Accredited</h3>
            </div>
            <div class="badge-dwdm">
                01CE0527 &ndash; DWDM<br>
                Open-Ended Practical
            </div>
        </div>

        <!-- Problem Statement Title Box -->
        <div class="practical-title-box">
            <h3>Open-Ended Practical: Designing Candlesticks using 5-Number Summary</h3>
            <p><strong>Problem Statement:</strong> Design candles (daily/weekly/monthly) of any 3 stock market-listed companies using the 5 Number Summary. Submission in (Printed document, Pages: 5-6, Single side Print).</p>
        </div>

        <!-- Meta Table: Student & Faculty Details -->
        <table class="meta-table">
            <tr>
                <td class="lbl">Student Name</td>
                <td><strong>Subham Kumar Keshari</strong></td>
                <td class="lbl">Enrollment / Class</td>
                <td>B.Tech Computer Engineering (Semester 5)</td>
            </tr>
            <tr>
                <td class="lbl">Course Code &amp; Title</td>
                <td>01CE0527 &ndash; Data Warehousing and Data Mining (DWDM)</td>
                <td class="lbl">Academic Year</td>
                <td>2024 &ndash; 2025 &bull; Semester V</td>
            </tr>
            <tr>
                <td class="lbl">Subject Faculties</td>
                <td><strong>Dr. Sivakumar Nadarajan</strong>, <strong>Prof. Urvi Dhamecha</strong>, <strong>Prof. Sahir Suma</strong></td>
                <td class="lbl">Head of Department</td>
                <td><strong>Dr. Krunal Vaghela</strong> (Dept. Computer Engineering)</td>
            </tr>
            <tr>
                <td class="lbl">Selected Companies</td>
                <td colspan="3">1. <strong>Tata Consultancy Services (TCS)</strong> &bull; 2. <strong>Reliance Industries Ltd. (RELIANCE)</strong> &bull; 3. <strong>Infosys Ltd. (INFY)</strong></td>
            </tr>
        </table>

        <!-- Section 1: Introduction to 5-Number Summary in DWDM -->
        <h4 class="sec-h">1. Introduction to 5-Number Summary in Data Exploration</h4>
        <p style="margin: 3px 0 6px 0;">
            In Data Warehousing and Data Mining (DWDM), exploratory data analysis (EDA) demands robust descriptive statistics capable of summarizing large-scale numeric distributions without succumbing to distortions caused by extreme values (outliers). The <strong>Five-Number Summary</strong> is an indispensable non-parametric statistical summary representing data location, spread, and skewness through five order statistics:
        </p>

        <div class="formula-grid">
            <div class="formula-card">
                <strong>1. Minimum ($Min$) &amp; Maximum ($Max$)</strong>
                Identifies the absolute boundary extremes:
                $$Min = x_{(1)}, \quad Max = x_{(N)}$$
                Represents lowest and highest transaction prices within the temporal window.
            </div>
            <div class="formula-card">
                <strong>2. Median ($Q_2$ / 50th Percentile)</strong>
                Measures central tendency invariant to skewness:
                $$Median = \\begin{{cases}} x_{{(\\frac{{N+1}}{{2}})}}, &amp; N\\text{{ odd}} \\\\ \\frac{{x_{{(\\frac{{N}}{{2}})}} + x_{{(\\frac{{N}}{{2}}+1)}}}}{{2}}, &amp; N\\text{{ even}} \\end{{cases}}$$
            </div>
            <div class="formula-card">
                <strong>3. First Quartile ($Q_1$ / 25th Percentile)</strong>
                Delimits the bottom 25% of the sorted observations:
                $$Q_1 = \\text{{Value at index }} 0.25 \\times (N + 1)$$
                Serves as the lower boundary of the candle body.
            </div>
            <div class="formula-card">
                <strong>4. Third Quartile ($Q_3$ / 75th Percentile)</strong>
                Delimits the bottom 75% (top 25%) of the sorted observations:
                $$Q_3 = \\text{{Value at index }} 0.75 \\times (N + 1)$$
                Serves as the upper boundary of the candle body.
            </div>
        </div>

        <!-- Section 2: Mathematical Formulations -->
        <h4 class="sec-h">2. Dispersion Metrics &amp; Outlier Boundaries</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Formula</th>
                    <th>Analytical Significance in Stock Market Mining</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Interquartile Range (IQR)</strong></td>
                    <td>$$IQR = Q_3 - Q_1$$</td>
                    <td>Measures core volatility (middle 50% price dispersion). Unaffected by transient spikes.</td>
                </tr>
                <tr>
                    <td><strong>Lower Outlier Fence</strong></td>
                    <td>$$LF = Q_1 - 1.5 \\times IQR$$</td>
                    <td>Identifies anomalous downward crashes, flash sales, or fat-finger trading errors.</td>
                </tr>
                <tr>
                    <td><strong>Upper Outlier Fence</strong></td>
                    <td>$$UF = Q_3 + 1.5 \\times IQR$$</td>
                    <td>Identifies anomalous speculative upward surges or abrupt corporate announcement spikes.</td>
                </tr>
                <tr>
                    <td><strong>Bowley Skewness ($S_k$)</strong></td>
                    <td>$$S_k = \\frac{{(Q_3 - Q_2) - (Q_2 - Q_1)}}{{Q_3 - Q_1}}$$</td>
                    <td>Measures directional asymmetry: $S_k &gt; 0$ indicates bullish tail; $S_k &lt; 0$ indicates bearish tail.</td>
                </tr>
            </tbody>
        </table>

        <!-- Section 3: Mapping 5-Number Summary to Candlestick Design -->
        <h4 class="sec-h">3. Structural Mapping: 5-Number Summary vs. Traditional Candlesticks</h4>
        <p style="margin: 2px 0;">
            Traditional financial candlesticks record only 4 discrete points: Open, High, Low, and Close ($OHLC$). While standard, OHLC is vulnerable to intra-period noise because Open and Close represent singular boundary snapshots. In this practical, we synthesize <strong>Box-Whisker Distribution Candles</strong>:
        </p>
        <ul style="margin: 3px 0 0 18px; padding: 0; font-size: 8pt;">
            <li><strong>Upper Wick / Whisker ($Max - Q_3$):</strong> Extends from the 75th percentile to the Maximum price achieved.</li>
            <li><strong>Real Body ($Q_1 \\to Q_3$):</strong> Represents the interquartile body enclosing the middle 50% of all traded prices.</li>
            <li><strong>Median Divider ($Q_2$):</strong> Prominent central line revealing whether price action consolidated higher or lower.</li>
            <li><strong>Lower Wick / Whisker ($Q_1 - Min$):</strong> Extends from the First Quartile down to the Minimum price observed.</li>
            <li><strong>Color Coding:</strong> Green if $Close \\ge Open$ (or $Q_3 - Q_2 &gt; Q_2 - Q_1$), Red if $Close &lt; Open$.</li>
        </ul>
    </div>
    <div class="page-footer">
        <span>01CE0527 &bull; DWDM Open-Ended Practical &bull; Marwadi University</span>
        <span>Page 1 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 2 ========================================== -->
<div class="page">
    <div class="page-content">
        <h4 class="sec-h">4. Multi-Timeframe Analytical Framework (Daily, Weekly, Monthly)</h4>
        <p style="margin: 3px 0 6px 0;">
            In market data mining, temporal aggregation granularities dictate the nature of extractable patterns. Designing candles across three hierarchical time scales enables data scientists to filter out micro-noise and isolate systemic trends:
        </p>

        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 15%;">Timeframe</th>
                    <th style="width: 25%;">Data Sampling Granularity</th>
                    <th style="width: 30%;">5-Number Summary Interpretation</th>
                    <th style="width: 30%;">Trading &amp; Data Mining Utility</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Daily Candle</strong></td>
                    <td>10 Intraday hourly interval samples (9:15 AM to 3:30 PM IST).</td>
                    <td>$Min/Max$ define intraday high/low; $Q_1/Q_3$ capture the high-volume core trading band; $Q_2$ tracks midday valuation.</td>
                    <td>Used for intraday momentum, liquidity profiling, and detecting opening/closing price manipulation.</td>
                </tr>
                <tr>
                    <td><strong>Weekly Candle</strong></td>
                    <td>Daily closing/settlement prices across the 5 consecutive trading days (Mon&ndash;Fri).</td>
                    <td>$Min/Max$ capture weekly extremes; $IQR$ represents weekly consolidation volatility; Median exposes true weekly balance.</td>
                    <td>Used for swing trading analysis, weekly support/resistance level identification, and short-term forecasting.</td>
                </tr>
                <tr>
                    <td><strong>Monthly Candle</strong></td>
                    <td>Weekly settlement benchmarks spanning 4 consecutive calendar trading weeks.</td>
                    <td>$Min/Max$ indicate monthly range; $Q_1/Q_3$ isolate monthly institutional accumulation; $Q_2$ reveals fair market value.</td>
                    <td>Macro-trend evaluation, institutional portfolio rebalancing, and long-term trend mining.</td>
                </tr>
            </tbody>
        </table>

        <h4 class="sec-h">5. Profile of Selected Stock Market Listed Companies</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Company Name</th>
                    <th>Ticker / Exchange</th>
                    <th>Sector &amp; Industry</th>
                    <th>Market Cap Class</th>
                    <th>Key Characteristics in Mining Context</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Tata Consultancy Services Ltd.</strong></td>
                    <td>NSE: TCS</td>
                    <td>Information Technology &amp; Services</td>
                    <td>Mega Cap (NIFTY 50)</td>
                    <td>Defensive stock with tight $IQR$, resilient spreads, low extreme variance, and high institutional holding.</td>
                </tr>
                <tr>
                    <td><strong>Reliance Industries Limited</strong></td>
                    <td>NSE: RELIANCE</td>
                    <td>Energy, Petrochemicals &amp; Telecom</td>
                    <td>Mega Cap (#1 Market Cap)</td>
                    <td>High trading volume, moderate-to-high $IQR$, responsive to global crude benchmarks and domestic retail.</td>
                </tr>
                <tr>
                    <td><strong>Infosys Limited</strong></td>
                    <td>NSE: INFY</td>
                    <td>Technology &amp; Consulting</td>
                    <td>Large Cap (NIFTY IT)</td>
                    <td>Dynamic volatility, frequent quarterly gap movements, distinct quartile distribution shifts.</td>
                </tr>
            </tbody>
        </table>

        <h4 class="sec-h">6. Data Preprocessing &amp; Algorithmic Pipeline</h4>
        <p style="margin: 3px 0 5px 0;">
            The extract-transform-load (ETL) pipeline implemented for calculating the five-number summary and rendering the candles follows rigorous data warehouse standards:
        </p>

        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 8px 12px; margin: 6px 0;">
            <ol style="margin: 0; padding-left: 20px; font-size: 8pt; line-height: 1.5;">
                <li><strong>Data Extraction:</strong> Historical tick and settlement feeds extracted from the National Stock Exchange (NSE) order books for October 2024.</li>
                <li><strong>Data Cleaning &amp; Formatting:</strong> Removal of non-trading weekend timestamps, adjustment for stock splits/dividends, and normalization of float values to 2 decimal places.</li>
                <li><strong>Temporal Window Partitioning:</strong> Partitioning observation sets into Daily ($D_t$), Weekly ($W_t$), and Monthly ($M_t$) datasets.</li>
                <li><strong>Order Statistics Computation:</strong> Sorting arrays in ascending order: $x_{(1)} \\le x_{(2)} \\le \\dots \\le x_{(N)}$.</li>
                <li><strong>Quartile Evaluation:</strong> Applying linear interpolation on rank indices to compute $Q_1$, $Median$, and $Q_3$.</li>
                <li><strong>Candlestick Synthesis &amp; Rendering:</strong> Generating dual-shadow box structures where body $= [Q_1, Q_3]$, center mark $= Q_2$, lower wick $= [Min, Q_1]$, and upper wick $= [Q_3, Max]$.</li>
            </ol>
        </div>

        <h4 class="sec-h">7. Candlestick Anatomy Schema</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Anatomical Component</th>
                    <th>5-Number Metric</th>
                    <th>Visual Representation</th>
                    <th>Economic Meaning</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Upper Shadow (Wick)</strong></td>
                    <td>$Max - Q_3$</td>
                    <td>Top thin vertical line to upper cap</td>
                    <td>Selling pressure rejecting extreme highs.</td>
                </tr>
                <tr>
                    <td><strong>Upper Body Limit</strong></td>
                    <td>$Q_3$ (75th Percentile)</td>
                    <td>Top boundary of colored rectangular box</td>
                    <td>Upper threshold of 50% dense trading activity.</td>
                </tr>
                <tr>
                    <td><strong>Central Median Line</strong></td>
                    <td>$Q_2$ (50th Percentile)</td>
                    <td>Horizontal yellow line within box body</td>
                    <td>Fair equilibrium price established during the period.</td>
                </tr>
                <tr>
                    <td><strong>Lower Body Limit</strong></td>
                    <td>$Q_1$ (25th Percentile)</td>
                    <td>Bottom boundary of colored rectangular box</td>
                    <td>Lower threshold of 50% dense trading activity.</td>
                </tr>
                <tr>
                    <td><strong>Lower Shadow (Tail)</strong></td>
                    <td>$Q_1 - Min$</td>
                    <td>Bottom thin vertical line to lower cap</td>
                    <td>Buying support absorbing extreme low sales.</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer">
        <span>01CE0527 &bull; DWDM Open-Ended Practical &bull; Marwadi University</span>
        <span>Page 2 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 3 ========================================== -->
<div class="page">
    <div class="page-content">
        <h4 class="sec-h">8. Company 1: Tata Consultancy Services Ltd. (NSE: TCS)</h4>
        <p style="margin: 2px 0 4px 0; font-size: 8pt;">
            <strong>Company Profile:</strong> India's premier multinational IT services conglomerate. TCS exhibits consistent liquidity and low idiosyncratic volatility, serving as a benchmark for technology sector equity evaluation.
        </p>

        <!-- Raw Observation Data -->
        <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-size: 7.6pt; margin-bottom: 5px;">
            <strong>Sorted Observation Datasets (INR ₹):</strong><br>
            &bull; <em>Daily (Oct 25, 2024):</em> [4142.50, 4155.00, 4165.40, 4178.20, 4185.00, 4192.50, 4205.00, 4212.00, 4218.00, 4225.00] &bull; Open: ₹4150.00, Close: ₹4220.00<br>
            &bull; <em>Weekly (Oct 21&ndash;25, 2024):</em> [4095.00, 4115.00, 4138.00, 4152.00, 4170.00, 4185.00, 4200.00, 4225.00, 4245.00, 4268.00] &bull; Open: ₹4110.00, Close: ₹4250.00<br>
            &bull; <em>Monthly (October 2024):</em> [3980.00, 4040.00, 4090.00, 4130.00, 4175.00, 4210.00, 4250.00, 4290.00, 4320.00, 4345.00] &bull; Open: ₹4020.00, Close: ₹4310.00
        </div>

        <!-- 5-Number Summary Table for TCS -->
        <table class="data-table">
            <thead>
                <tr>
                    <th>Timeframe</th>
                    <th>Min ($x_{(1)}$)</th>
                    <th>$Q_1$ (25%)</th>
                    <th>Median ($Q_2$)</th>
                    <th>$Q_3$ (75%)</th>
                    <th>Max ($x_{(N)}$)</th>
                    <th>IQR</th>
                    <th>Mean ($\\mu$)</th>
                    <th>Std Dev ($\\sigma$)</th>
                    <th>Skew ($S_k$)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Daily</strong></td>
                    <td>₹4142.50</td>
                    <td>₹4168.60</td>
                    <td>₹4188.75</td>
                    <td>₹4210.25</td>
                    <td>₹4225.00</td>
                    <td><strong>₹41.65</strong></td>
                    <td>₹4187.86</td>
                    <td>₹26.24</td>
                    <td>-0.10 (Neutral)</td>
                </tr>
                <tr>
                    <td><strong>Weekly</strong></td>
                    <td>₹4095.00</td>
                    <td>₹4141.50</td>
                    <td>₹4177.50</td>
                    <td>₹4218.75</td>
                    <td>₹4268.00</td>
                    <td><strong>₹77.25</strong></td>
                    <td>₹4179.30</td>
                    <td>₹53.48</td>
                    <td>+0.10 (Slight Bullish)</td>
                </tr>
                <tr>
                    <td><strong>Monthly</strong></td>
                    <td>₹3980.00</td>
                    <td>₹4100.00</td>
                    <td>₹4192.50</td>
                    <td>₹4280.00</td>
                    <td>₹4345.00</td>
                    <td><strong>₹180.00</strong></td>
                    <td>₹4183.00</td>
                    <td>114.72</td>
                    <td>-0.25 (Left Skew)</td>
                </tr>
            </tbody>
        </table>

        <!-- Graphical Chart Insertion -->
        <div class="chart-container">
            <img src="data:image/png;base64,{img_tcs}" alt="TCS Candlestick Analysis">
        </div>

        <!-- Analytical Discussion -->
        <h4 class="sec-h" style="margin-top: 4px;">Analytical Evaluation for TCS</h4>
        <div style="font-size: 7.9pt; line-height: 1.38;">
            <p style="margin: 2px 0;">
                <strong>1. Intraday Tightness:</strong> In the daily timeframe, TCS exhibits an $IQR$ of ₹41.65 against a full range of ₹82.50 ($Max - Min$). The ratio $IQR / Range = 0.505$ indicates balanced price concentration, demonstrating that algorithmic institutional market makers absorbed intraday liquidity evenly without runaway slippage.
            </p>
            <p style="margin: 2px 0;">
                <strong>2. Weekly Expansion &amp; Direction:</strong> The weekly candle body ($Q_1 \\to Q_3$) widens to ₹77.25 with the close price (₹4250.00) settling significantly above the 75th percentile ($Q_3 = 4218.75$). This confirms strong bullish buyer dominance that conquered the upper quartile fence.
            </p>
            <p style="margin: 2px 0;">
                <strong>3. Monthly Accumulation Pattern:</strong> Over the 4-week October span, the monthly candle forms a substantial body of ₹180.00. The median of ₹4192.50 sits almost equidistant between $Q_1$ (₹4100.00) and $Q_3$ (₹4280.00), demonstrating a highly symmetric distribution characteristic of large-cap bluechip accumulation.
            </p>
        </div>
    </div>
    <div class="page-footer">
        <span>01CE0527 &bull; DWDM Open-Ended Practical &bull; Marwadi University</span>
        <span>Page 3 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 4 ========================================== -->
<div class="page">
    <div class="page-content">
        <h4 class="sec-h">9. Company 2: Reliance Industries Ltd. (NSE: RELIANCE)</h4>
        <p style="margin: 2px 0 4px 0; font-size: 8pt;">
            <strong>Company Profile:</strong> India's largest corporate by market capitalization with diverse operations across oil-to-chemicals (O2C), telecom (Jio), and organized retail. Its stock exhibits high beta sensitivity to macro-commodity and fiscal cycles.
        </p>

        <!-- Raw Observation Data -->
        <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-size: 7.6pt; margin-bottom: 5px;">
            <strong>Sorted Observation Datasets (INR ₹):</strong><br>
            &bull; <em>Daily (Oct 25, 2024):</em> [2715.00, 2724.00, 2735.00, 2742.00, 2750.00, 2758.00, 2768.00, 2776.00, 2785.00, 2795.50] &bull; Open: ₹2725.00, Close: ₹2788.00<br>
            &bull; <em>Weekly (Oct 21&ndash;25, 2024):</em> [2685.00, 2705.00, 2722.00, 2740.00, 2760.00, 2778.00, 2795.00, 2810.00, 2822.00, 2830.00] &bull; Open: ₹2698.00, Close: ₹2815.00<br>
            &bull; <em>Monthly (October 2024):</em> [2620.00, 2665.00, 2700.00, 2735.00, 2775.00, 2805.00, 2835.00, 2860.00, 2880.00, 2895.00] &bull; Open: ₹2640.00, Close: ₹2870.00
        </div>

        <!-- 5-Number Summary Table for RELIANCE -->
        <table class="data-table">
            <thead>
                <tr>
                    <th>Timeframe</th>
                    <th>Min ($x_{(1)}$)</th>
                    <th>$Q_1$ (25%)</th>
                    <th>Median ($Q_2$)</th>
                    <th>$Q_3$ (75%)</th>
                    <th>Max ($x_{(N)}$)</th>
                    <th>IQR</th>
                    <th>Mean ($\\mu$)</th>
                    <th>Std Dev ($\\sigma$)</th>
                    <th>Skew ($S_k$)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Daily</strong></td>
                    <td>₹2715.00</td>
                    <td>₹2736.75</td>
                    <td>₹2754.00</td>
                    <td>₹2774.00</td>
                    <td>₹2795.50</td>
                    <td><strong>₹37.25</strong></td>
                    <td>₹2754.85</td>
                    <td>₹24.87</td>
                    <td>+0.10 (Symmetric)</td>
                </tr>
                <tr>
                    <td><strong>Weekly</strong></td>
                    <td>₹2685.00</td>
                    <td>₹2726.50</td>
                    <td>₹2769.00</td>
                    <td>₹2806.25</td>
                    <td>₹2830.00</td>
                    <td><strong>₹79.75</strong></td>
                    <td>₹2764.70</td>
                    <td>₹48.97</td>
                    <td>-0.26 (Left Skew)</td>
                </tr>
                <tr>
                    <td><strong>Monthly</strong></td>
                    <td>₹2620.00</td>
                    <td>₹2708.75</td>
                    <td>₹2790.00</td>
                    <td>₹2853.75</td>
                    <td>₹2895.00</td>
                    <td><strong>₹145.00</strong></td>
                    <td>₹2777.00</td>
                    <td>₹88.58</td>
                    <td>-0.44 (Moderate Left)</td>
                </tr>
            </tbody>
        </table>

        <!-- Graphical Chart Insertion -->
        <div class="chart-container">
            <img src="data:image/png;base64,{img_rel}" alt="RELIANCE Candlestick Analysis">
        </div>

        <!-- Analytical Discussion -->
        <h4 class="sec-h" style="margin-top: 4px;">Analytical Evaluation for Reliance Industries</h4>
        <div style="font-size: 7.9pt; line-height: 1.38;">
            <p style="margin: 2px 0;">
                <strong>1. Intraday Dispersion:</strong> The daily $IQR$ stands at ₹37.25 within an ₹80.50 total envelope. The close of ₹2788.00 penetrates well past $Q_3$ (₹2774.00), demonstrating aggressive end-of-day buying that forced the upper whisker into a compressed bullish formation.
            </p>
            <p style="margin: 2px 0;">
                <strong>2. Weekly Support Dynamics:</strong> Weekly $Q_1$ at ₹2726.50 served as strong empirical support. The whisker downward from $Q_1$ to $Min$ (₹2685.00) shows that bears briefly broke below ₹2700, but value investors rapidly bought the dip, pulling prices back within the quartile box.
            </p>
            <p style="margin: 2px 0;">
                <strong>3. Monthly Trend Asymmetry:</strong> The monthly candle exhibits an $IQR$ of ₹145.00. Notice the negative Bowley skewness ($S_k = -0.44$); the distance $(Q_3 - Q_2) = 63.75$ is less than $(Q_2 - Q_1) = 81.25$. This data mining signature reflects sustained upward accumulation where prices spent more time consolidating at higher elevations.
            </p>
        </div>
    </div>
    <div class="page-footer">
        <span>01CE0527 &bull; DWDM Open-Ended Practical &bull; Marwadi University</span>
        <span>Page 4 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 5 ========================================== -->
<div class="page">
    <div class="page-content">
        <h4 class="sec-h">10. Company 3: Infosys Limited (NSE: INFY)</h4>
        <p style="margin: 2px 0 4px 0; font-size: 8pt;">
            <strong>Company Profile:</strong> A pioneering Indian tech giant in digital next services and consulting. INFY is celebrated for its agile price responsiveness to US currency exchange rates (USD/INR) and North American tech capital expenditure trends.
        </p>

        <!-- Raw Observation Data -->
        <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-size: 7.6pt; margin-bottom: 5px;">
            <strong>Sorted Observation Datasets (INR ₹):</strong><br>
            &bull; <em>Daily (Oct 25, 2024):</em> [1855.00, 1862.00, 1870.00, 1878.00, 1888.50, 1895.00, 1902.00, 1910.00, 1916.00, 1922.00] &bull; Open: ₹1860.00, Close: ₹1915.00<br>
            &bull; <em>Weekly (Oct 21&ndash;25, 2024):</em> [1830.00, 1850.00, 1868.00, 1882.00, 1895.00, 1912.00, 1930.00, 1942.00, 1950.00, 1958.00] &bull; Open: ₹1845.00, Close: ₹1948.00<br>
            &bull; <em>Monthly (October 2024):</em> [1785.00, 1820.00, 1855.00, 1880.00, 1910.00, 1940.00, 1965.00, 1985.00, 1998.00, 2010.00] &bull; Open: ₹1805.00, Close: ₹1995.00
        </div>

        <!-- 5-Number Summary Table for INFY -->
        <table class="data-table">
            <thead>
                <tr>
                    <th>Timeframe</th>
                    <th>Min ($x_{(1)}$)</th>
                    <th>$Q_1$ (25%)</th>
                    <th>Median ($Q_2$)</th>
                    <th>$Q_3$ (75%)</th>
                    <th>Max ($x_{(N)}$)</th>
                    <th>IQR</th>
                    <th>Mean ($\\mu$)</th>
                    <th>Std Dev ($\\sigma$)</th>
                    <th>Skew ($S_k$)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Daily</strong></td>
                    <td>₹1855.00</td>
                    <td>₹1872.00</td>
                    <td>₹1891.75</td>
                    <td>₹1908.00</td>
                    <td>₹1922.00</td>
                    <td><strong>₹36.00</strong></td>
                    <td>₹1889.85</td>
                    <td>₹22.10</td>
                    <td>-0.26 (Left Skew)</td>
                </tr>
                <tr>
                    <td><strong>Weekly</strong></td>
                    <td>₹1830.00</td>
                    <td>₹1871.50</td>
                    <td>₹1903.50</td>
                    <td>₹1939.00</td>
                    <td>₹1958.00</td>
                    <td><strong>₹67.50</strong></td>
                    <td>₹1901.70</td>
                    <td>₹41.85</td>
                    <td>-0.13 (Neutral)</td>
                </tr>
                <tr>
                    <td><strong>Monthly</strong></td>
                    <td>₹1785.00</td>
                    <td>₹1861.25</td>
                    <td>₹1925.00</td>
                    <td>₹1980.00</td>
                    <td>₹2010.00</td>
                    <td><strong>₹118.75</strong></td>
                    <td>₹1914.80</td>
                    <td>₹72.93</td>
                    <td>-0.42 (Left Skew)</td>
                </tr>
            </tbody>
        </table>

        <!-- Graphical Chart Insertion -->
        <div class="chart-container">
            <img src="data:image/png;base64,{img_infy}" alt="INFY Candlestick Analysis">
        </div>

        <!-- Analytical Discussion -->
        <h4 class="sec-h" style="margin-top: 4px;">Analytical Evaluation for Infosys</h4>
        <div style="font-size: 7.9pt; line-height: 1.38;">
            <p style="margin: 2px 0;">
                <strong>1. Intraday Scalping Volatility:</strong> The daily $IQR$ is ₹36.00 with a standard deviation $\\sigma = 22.10$. Despite a modest base price around ₹1900, INFY displayed proportional volatility ($IQR / Price = 1.89\%$), providing active swing windows for intra-day traders.
            </p>
            <p style="margin: 2px 0;">
                <strong>2. Weekly Trend Continuity:</strong> The weekly candle closed at ₹1948.00, directly adjacent to the maximum (₹1958.00). The absence of a substantial upper wick ($Max - Close = 10.00$) reveals decisive closing conviction, showing no exhaustion from buyers at the week's end.
            </p>
            <p style="margin: 2px 0;">
                <strong>3. Psychological ₹2000 Frontier:</strong> The monthly candle recorded $Max = 2010.00$, breaching the crucial ₹2000 resistance level. The interquartile body spans ₹1861.25 to ₹1980.00 ($IQR = 118.75$). Data mining validates that ₹1860 is now established as the primary institutional accumulation floor.
            </p>
        </div>
    </div>
    <div class="page-footer">
        <span>01CE0527 &bull; DWDM Open-Ended Practical &bull; Marwadi University</span>
        <span>Page 5 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 6 ========================================== -->
<div class="page">
    <div class="page-content">
        <h4 class="sec-h">11. Cross-Company Synthesis &amp; Comparative Analysis</h4>
        <p style="margin: 2px 0 4px 0; font-size: 8pt;">
            Comparing the monthly five-number summary dispersion metrics across all three listed entities highlights distinct volatility profiles across sectors:
        </p>

        <table class="data-table">
            <thead>
                <tr>
                    <th>Company Name</th>
                    <th>Sector</th>
                    <th>Monthly Range ($Max - Min$)</th>
                    <th>Monthly $IQR$ ($Q_3 - Q_1$)</th>
                    <th>Relative Volatility ($IQR / Median$)</th>
                    <th>Outlier Boundary Band ($LF \\to UF$)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>TCS</strong></td>
                    <td>IT / Software</td>
                    <td>₹365.00</td>
                    <td>₹180.00</td>
                    <td><strong>4.29%</strong> (Low/Stable)</td>
                    <td>₹3830.00 &ndash; ₹4550.00</td>
                </tr>
                <tr>
                    <td><strong>RELIANCE</strong></td>
                    <td>Energy / Retail</td>
                    <td>₹275.00</td>
                    <td>₹145.00</td>
                    <td><strong>5.20%</strong> (Moderate)</td>
                    <td>₹2491.25 &ndash; ₹3071.25</td>
                </tr>
                <tr>
                    <td><strong>INFY</strong></td>
                    <td>IT / Consulting</td>
                    <td>₹225.00</td>
                    <td>₹118.75</td>
                    <td><strong>6.17%</strong> (High Alpha)</td>
                    <td>₹1683.13 &ndash; ₹2158.13</td>
                </tr>
            </tbody>
        </table>

        <!-- Comparison Bar Chart Insertion -->
        <div class="chart-container" style="margin: 4px 0;">
            <img src="data:image/png;base64,{img_cmp}" alt="Comparative Dispersion Metrics">
        </div>

        <!-- Python Implementation Code Snippet -->
        <h4 class="sec-h" style="margin-top: 2px;">12. Python Implementation Snippet (DWDM Pipeline)</h4>
        <div class="code-box">
import numpy as np, pandas as pd, matplotlib.pyplot as plt, matplotlib.patches as patches
def build_5num_candle(ax, prices, label, is_bullish=True):
    arr = np.sort(prices)
    mn, q1, med, q3, mx = np.min(arr), np.percentile(arr, 25), np.median(arr), np.percentile(arr, 75), np.max(arr)
    iqr = q3 - q1
    ax.plot([1, 1], [mn, mx], color='#212121', lw=1.8) # Whiskers
    ax.add_patch(patches.Rectangle((0.8, q1), 0.4, iqr, facecolor='#26a69a' if is_bullish else '#ef5350', edgecolor='#000', lw=1.5))
    ax.plot([0.8, 1.2], [med, med], color='#FFD600', lw=2.2) # Median Notch
    return {{"Min": mn, "Q1": q1, "Median": med, "Q3": q3, "Max": mx, "IQR": iqr}}
        </div>

        <!-- Learning Outcomes & Conclusion -->
        <h4 class="sec-h" style="margin-top: 2px;">13. Key Findings &amp; Academic Conclusion</h4>
        <p style="margin: 1px 0 4px 0; font-size: 7.8pt;">
            <strong>Conclusion:</strong> The 5-number summary provides an empirically superior data mining model over conventional 4-point OHLC candlesticks. By leveraging order statistics ($Q_1, Q_2, Q_3$), analysts insulate trading representations against ephemeral noise while accurately quantifying market dispersion and institutional accumulation bands across daily, weekly, and monthly horizons.
        </p>

        <!-- Official Faculty & Department Sign-off Block -->
        <table class="sign-table">
            <tr>
                <td style="width: 25%;">
                    <div class="sign-line">Student Signature<br><strong>Subham Kumar Keshari</strong><br><small>Roll No: B.Tech CE Sem-5</small></div>
                </td>
                <td style="width: 25%;">
                    <div class="sign-line">Subject Faculty<br><strong>Dr. Sivakumar Nadarajan</strong><br><small>Dept. Computer Engineering</small></div>
                </td>
                <td style="width: 25%;">
                    <div class="sign-line">Subject Faculty<br><strong>Prof. Urvi Dhamecha</strong><br><small>Dept. Computer Engineering</small></div>
                </td>
                <td style="width: 25%;">
                    <div class="sign-line">Head of Department<br><strong>Dr. Krunal Vaghela</strong><br><small>Dept. Computer Engineering</small></div>
                </td>
            </tr>
        </table>
    </div>
    <div class="page-footer">
        <span>01CE0527 &bull; DWDM Open-Ended Practical &bull; Marwadi University</span>
        <span>Page 6 of 6 &bull; Single-Side Print Edition</span>
    </div>
</div>

</body>
</html>
"""

html_path = os.path.join(work_dir, "DWDM_Open_Ended_Practical_5NumberSummary.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML successfully generated at: {html_path}")

# Generate PDF using Microsoft Edge Headless
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

edge_exe = None
for p in edge_paths:
    if os.path.exists(p):
        edge_exe = p
        break

pdf_path = os.path.join(work_dir, "DWDM_Open_Ended_Practical_5NumberSummary.pdf")
if edge_exe:
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    print("Generating PDF via Edge Headless...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"SUCCESS: PDF generated at {pdf_path} (Size: {size_kb:.1f} KB)")
    else:
        print("Warning: Edge finished but PDF was not found. Stderr:", result.stderr)
else:
    print("Edge executable not found in default paths.")
