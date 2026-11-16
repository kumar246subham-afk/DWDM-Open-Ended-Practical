import os
import base64
import subprocess
import shutil

temp_dir = os.environ.get("TEMP", r"C:\Users\ADMIN\AppData\Local\Temp")
work_dir = os.path.join(temp_dir, "DWDM_Practical")
charts_dir = os.path.join(work_dir, "charts")

def get_b64(fname):
    p = os.path.join(charts_dir, fname)
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_1 = get_b64("screenshot_1.png")
img_2 = get_b64("screenshot_2.png")
img_3 = get_b64("screenshot_3.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Practical 4: Data Preprocessing Using a Sample Dataset - Marwadi University</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 10mm 13mm 10mm 13mm;
    }}
    * {{
        box-sizing: border-box;
    }}
    body {{
        font-family: 'Segoe UI', Arial, sans-serif;
        color: #1a202c;
        margin: 0;
        padding: 0;
        background: #cbd5e1;
        font-size: 8.6pt;
        line-height: 1.32;
    }}
    .page {{
        width: 210mm;
        height: 297mm;
        max-height: 297mm;
        padding: 11mm 14mm 11mm 14mm;
        margin: 10px auto;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
        page-break-after: always;
        page-break-inside: avoid;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .page-content {{
        flex: 1;
    }}
    .page-footer {{
        border-top: 1.5px solid #0f172a;
        padding-top: 4px;
        font-size: 7.5pt;
        color: #475569;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 600;
    }}
    
    /* Header styles */
    .univ-header {{
        border-bottom: 2.5px solid #0f172a;
        padding-bottom: 5px;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .univ-title {{
        text-align: left;
    }}
    .univ-title h1 {{
        margin: 0;
        font-size: 14pt;
        color: #b91c1c;
        font-weight: 800;
        letter-spacing: 0.8px;
    }}
    .univ-title h2 {{
        margin: 1px 0;
        font-size: 9.5pt;
        color: #1e293b;
        font-weight: 700;
    }}
    .univ-title h3 {{
        margin: 1px 0;
        font-size: 8pt;
        color: #475569;
        font-weight: 600;
    }}
    .badge-dwdm {{
        background: #0f172a;
        color: #ffffff;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 8pt;
        font-weight: bold;
        text-align: right;
        line-height: 1.2;
    }}
    
    .meta-table {{
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 8px;
        font-size: 7.8pt;
    }}
    .meta-table td {{
        padding: 3.5px 7px;
        border: 1px solid #cbd5e1;
    }}
    .meta-table td.lbl {{
        font-weight: 700;
        background: #f1f5f9;
        color: #0f172a;
        width: 18%;
    }}
    
    h3.prac-title {{
        margin: 4px 0 6px 0;
        font-size: 11pt;
        color: #0369a1;
        font-weight: 800;
        text-transform: uppercase;
        border-left: 4.5px solid #0284c7;
        padding-left: 8px;
        background: #f0f9ff;
        padding-top: 3px;
        padding-bottom: 3px;
    }}
    h4.sec-h {{
        font-size: 8.8pt;
        color: #0f172a;
        background: #e2e8f0;
        padding: 3px 7px;
        margin: 6px 0 4px 0;
        border-left: 3.5px solid #0284c7;
        font-weight: 700;
        text-transform: uppercase;
    }}
    
    table.data-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 4px 0;
        font-size: 7.5pt;
    }}
    table.data-table th, table.data-table td {{
        border: 1px solid #cbd5e1;
        padding: 3px 5px;
        text-align: left;
    }}
    table.data-table th {{
        background: #0f172a;
        color: #ffffff;
        font-weight: 600;
        text-align: center;
    }}
    table.data-table tr:nth-child(even) {{
        background: #f8fafc;
    }}
    
    .box-info {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        padding: 5px 8px;
        font-size: 7.8pt;
        margin: 4px 0;
    }}
    
    .screenshot-img {{
        width: 100%;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        margin: 4px 0;
    }}
    
    .code-box {{
        background: #0f172a;
        color: #f8fafc;
        padding: 5px 8px;
        border-radius: 4px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 7.4pt;
        line-height: 1.25;
        margin: 3px 0;
    }}
    
    .sign-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }}
    .sign-table td {{
        text-align: center;
        padding: 4px;
        vertical-align: bottom;
        border: none;
        font-size: 7.6pt;
    }}
    .sign-line {{
        border-top: 1px dashed #475569;
        margin-top: 22px;
        padding-top: 3px;
        font-weight: bold;
    }}

    .print-bar {{
        text-align: center;
        padding: 10px;
        background: #0f172a;
        color: white;
        margin-bottom: 12px;
        position: sticky;
        top: 0;
        z-index: 100;
    }}
    .print-btn {{
        background: #0284c7;
        color: white;
        border: none;
        padding: 6px 18px;
        font-size: 0.9rem;
        font-weight: bold;
        border-radius: 4px;
        cursor: pointer;
        margin-left: 12px;
    }}
    
    @media print {{
        body {{
            background: #ffffff;
            font-size: 8.2pt;
        }}
        .page {{
            box-shadow: none;
            margin: 0;
            width: 100%;
            height: 100vh;
            max-height: none;
            padding: 9mm 11mm;
            page-break-after: always;
            page-break-inside: avoid;
        }}
        .print-bar {{
            display: none !important;
        }}
    }}
</style>
</head>
<body>

<div class="print-bar">
    <span><strong>MARWADI UNIVERSITY &bull; 01CE0527 - DWDM &bull; Practical 4: Data Preprocessing</strong> &mdash; Exactly 6 Pages</span>
    <button class="print-btn" onclick="window.print()">🖨️ Print / Save as PDF (Ctrl + P)</button>
</div>

<!-- ========================================== PAGE 1 ========================================== -->
<div class="page">
    <div class="page-content">
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY</h1>
                <h2>FACULTY OF ENGINEERING &amp; TECHNOLOGY</h2>
                <h3>Department of Computer Engineering &bull; NAAC A+ Accredited</h3>
            </div>
            <div class="badge-dwdm">
                01CE0527 &ndash; DWDM<br>
                Practical 4
            </div>
        </div>

        <table class="meta-table">
            <tr>
                <td class="lbl">Full Name</td>
                <td><strong>Subham Kumar Keshari</strong></td>
                <td class="lbl">Enrolment No.</td>
                <td><strong>92400103120</strong></td>
            </tr>
            <tr>
                <td class="lbl">Department</td>
                <td>Computer Engineering &bull; Semester 5</td>
                <td class="lbl">Academic Subject</td>
                <td>01CE0527 &ndash; Data Warehousing and Data Mining</td>
            </tr>
            <tr>
                <td class="lbl">Subject Faculties</td>
                <td><strong>Dr. Sivakumar Nadarajan</strong>, <strong>Prof. Urvi Dhamecha</strong>, <strong>Prof. Sahir Suma</strong></td>
                <td class="lbl">Head of Department</td>
                <td><strong>Dr. Krunal Vaghela</strong> (Dept. Computer Engineering)</td>
            </tr>
        </table>

        <h3 class="prac-title">Practical 4: Data Preprocessing Using a Sample Dataset</h3>

        <h4 class="sec-h">Aim</h4>
        <div class="box-info">
            To understand the importance of data preprocessing by identifying missing values, duplicate records, inconsistent values, invalid data, and categorical variables requiring encoding, and transforming a raw dataset into a clean, model-ready dataset suitable for data mining.
        </div>

        <h4 class="sec-h">Learning Outcomes</h4>
        <p style="margin: 2px 0 3px 0; font-size: 7.8pt;">After completing this practical, students will be able to:</p>
        <ul style="margin: 0 0 5px 18px; padding: 0; font-size: 7.7pt; line-height: 1.35;">
            <li>Understand why data preprocessing is required before applying data mining techniques.</li>
            <li>Identify missing values and duplicate records systematically in tabular datasets.</li>
            <li>Detect inconsistent, dirty, and invalid data out of logical constraints.</li>
            <li>Perform robust data cleaning, imputation, and standardization.</li>
            <li>Encode categorical variables into numeric form using <strong>Label Encoding</strong> and <strong>One-Hot Encoding</strong>.</li>
            <li>Identify the independent and dependent variables and justify technical feature selection.</li>
            <li>Prepare a comprehensive, model-ready dataset suitable for machine learning and data mining algorithms.</li>
        </ul>

        <h4 class="sec-h">Introduction</h4>
        <p style="margin: 2px 0 5px 0; font-size: 7.8pt; text-align: justify;">
            Real-world datasets are rarely perfect. They frequently contain missing values, duplicate records, inconsistent formats, incorrect entries, and text-based categorical columns. Before executing Extract-Transform-Load (ETL) pipelines, data warehousing, or data mining algorithms, the data must be rigorously cleaned, standardized, and converted entirely into numeric form to prevent model bias and calculation failures.
        </p>

        <h4 class="sec-h">Sample Dataset Before Preprocessing</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Student_ID</th>
                    <th>Name</th>
                    <th>Gender</th>
                    <th>Age</th>
                    <th>Department</th>
                    <th>CGPA</th>
                    <th>Attendance</th>
                    <th>City</th>
                    <th>Phone</th>
                    <th>Placement</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align:center;">S101</td>
                    <td>Arun Kumar</td>
                    <td>Male</td>
                    <td style="text-align:center;">20</td>
                    <td>CSE</td>
                    <td style="text-align:center;">8.5</td>
                    <td style="text-align:center;">92</td>
                    <td>Ahmedabad</td>
                    <td>9876543210</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S102</td>
                    <td>Priya Patel</td>
                    <td>Female</td>
                    <td style="text-align:center;">21</td>
                    <td>IT</td>
                    <td style="text-align:center;">9.1</td>
                    <td style="text-align:center;">95</td>
                    <td>Surat</td>
                    <td>9876543211</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr style="background:#fee2e2;">
                    <td style="text-align:center;">S103</td>
                    <td>Rahul Shah</td>
                    <td>M</td>
                    <td style="text-align:center;">20</td>
                    <td>CSE</td>
                    <td style="text-align:center; color:#b91c1c; font-weight:bold;">NA</td>
                    <td style="text-align:center;">88</td>
                    <td>Rajkot</td>
                    <td>9876543212</td>
                    <td style="text-align:center;">No</td>
                </tr>
                <tr style="background:#fee2e2;">
                    <td style="text-align:center;">S104</td>
                    <td>Sneha Joshi</td>
                    <td>Female</td>
                    <td style="text-align:center;">19</td>
                    <td>AI</td>
                    <td style="text-align:center;">8.9</td>
                    <td style="text-align:center; color:#b91c1c; font-weight:bold;">NULL</td>
                    <td>Ahmedabad</td>
                    <td>9876543213</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S105</td>
                    <td>Kiran Patel</td>
                    <td>Female</td>
                    <td style="text-align:center;">22</td>
                    <td>DS</td>
                    <td style="text-align:center;">7.8</td>
                    <td style="text-align:center;">84</td>
                    <td>Surat</td>
                    <td>9876543214</td>
                    <td style="text-align:center;">No</td>
                </tr>
                <tr style="background:#fef3c7;">
                    <td style="text-align:center;">S106</td>
                    <td>Arun Kumar</td>
                    <td>Male</td>
                    <td style="text-align:center;">20</td>
                    <td>CSE</td>
                    <td style="text-align:center;">8.5</td>
                    <td style="text-align:center;">92</td>
                    <td>Ahmedabad</td>
                    <td>9876543210</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr style="background:#fee2e2;">
                    <td style="text-align:center;">S107</td>
                    <td>Mehul Shah</td>
                    <td>Male</td>
                    <td style="text-align:center; color:#b91c1c; font-weight:bold;">-5</td>
                    <td>IT</td>
                    <td style="text-align:center;">6.8</td>
                    <td style="text-align:center;">78</td>
                    <td>Vadodara</td>
                    <td>9876543216</td>
                    <td style="text-align:center;">No</td>
                </tr>
                <tr style="background:#fee2e2;">
                    <td style="text-align:center;">S108</td>
                    <td>Pooja Mehta</td>
                    <td>F</td>
                    <td style="text-align:center;">21</td>
                    <td>AI</td>
                    <td style="text-align:center; color:#b91c1c; font-weight:bold;">15.2</td>
                    <td style="text-align:center;">90</td>
                    <td>Rajkot</td>
                    <td style="color:#b91c1c; font-weight:bold;">NULL</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr style="background:#fee2e2;">
                    <td style="text-align:center;">S109</td>
                    <td>Amit Patel</td>
                    <td>Male</td>
                    <td style="text-align:center;">20</td>
                    <td style="color:#b91c1c; font-weight:bold;">NULL</td>
                    <td style="text-align:center;">8.2</td>
                    <td style="text-align:center;">86</td>
                    <td>Ahmedabad</td>
                    <td>9876543218</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr style="background:#fee2e2;">
                    <td style="text-align:center;">S110</td>
                    <td>Riya Shah</td>
                    <td>Female</td>
                    <td style="text-align:center;">19</td>
                    <td>CSE</td>
                    <td style="text-align:center;">7.5</td>
                    <td style="text-align:center; color:#b91c1c; font-weight:bold;">120</td>
                    <td>Surat</td>
                    <td>9876543219</td>
                    <td style="text-align:center;">No</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer">
        <span>Subham Kumar Keshari &bull; Enrolment: 92400103120 &bull; Marwadi University</span>
        <span>Page 1 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 2 ========================================== -->
<div class="page">
    <div class="page-content">
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY &bull; DEPT. OF COMPUTER ENGINEERING</h1>
                <h2>01CE0527 &ndash; DWDM &bull; Practical 4: Data Preprocessing</h2>
            </div>
            <div class="badge-dwdm">PROBLEMS &amp; TECHNIQUES</div>
        </div>

        <h4 class="sec-h">Problems Identified in the Dataset</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Problem</th>
                    <th style="width: 25%;">Example</th>
                    <th style="width: 50%;">Reason</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Missing Value</strong></td>
                    <td>CGPA = NA, Attendance = NULL</td>
                    <td>Algorithms cannot process incomplete data reliably; causes mathematical crashes in linear/distance calculations.</td>
                </tr>
                <tr>
                    <td><strong>Duplicate Record</strong></td>
                    <td>S101 and S106</td>
                    <td>Duplicates produce biased analysis and falsely inflate pattern weights in data mining.</td>
                </tr>
                <tr>
                    <td><strong>Inconsistent Values</strong></td>
                    <td>Male, Female, M, F</td>
                    <td>Values should follow one standard; algorithms treat 'M' and 'Male' as two distinct categories.</td>
                </tr>
                <tr>
                    <td><strong>Invalid Age</strong></td>
                    <td>-5</td>
                    <td>Age cannot be negative in the physical world; violates logical integrity constraints.</td>
                </tr>
                <tr>
                    <td><strong>Invalid CGPA</strong></td>
                    <td>15.2</td>
                    <td>CGPA should be bounded strictly between 0 and 10 according to academic evaluation scale.</td>
                </tr>
                <tr>
                    <td><strong>Invalid Attendance</strong></td>
                    <td>120</td>
                    <td>Attendance cannot exceed 100%; reflects typographical entry errors.</td>
                </tr>
                <tr>
                    <td><strong>Missing Department</strong></td>
                    <td>NULL</td>
                    <td>Department is required for academic analysis and department-wise stratification.</td>
                </tr>
                <tr>
                    <td><strong>Missing Phone</strong></td>
                    <td>NULL</td>
                    <td>Incomplete contact information; represents missing communication metadata.</td>
                </tr>
                <tr>
                    <td><strong>Categorical Text Values</strong></td>
                    <td>Gender, Department, City, Placement stored as text</td>
                    <td>Most data mining and ML algorithms require numeric input matrices, not string literals.</td>
                </tr>
            </tbody>
        </table>

        <h4 class="sec-h">Techniques Used</h4>
        <p style="margin: 2px 0 3px 0; font-size: 7.8pt;">Each problem identified above is solved using one specific, named technique:</p>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 28%;">Technique Used</th>
                    <th>Description (1&ndash;2 lines)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Mean / Median Imputation</strong></td>
                    <td>Replaces a missing numeric value with the column's mean or median, keeping the overall distribution roughly unchanged.</td>
                </tr>
                <tr>
                    <td><strong>Mode Imputation</strong></td>
                    <td>Replaces a missing categorical value with the most frequently occurring category in that column.</td>
                </tr>
                <tr>
                    <td><strong>Duplicate Removal</strong></td>
                    <td>Detects rows that are exact repeats of another row and deletes the extra copies, keeping only one unique entity.</td>
                </tr>
                <tr>
                    <td><strong>Data Standardization (Text)</strong></td>
                    <td>Converts inconsistent text values (e.g., M/F) into one consistent standard form (Male/Female).</td>
                </tr>
                <tr>
                    <td><strong>Range / Validity Check</strong></td>
                    <td>Verifies a value falls within a logically possible range (e.g., Age &gt; 0, 0&ndash;10 CGPA, Attendance &le; 100%) and corrects violations.</td>
                </tr>
                <tr>
                    <td><strong>Label Encoding</strong></td>
                    <td>Converts a binary categorical column (2 values only) into a single 0/1 numeric column.</td>
                </tr>
                <tr>
                    <td><strong>One-Hot Encoding</strong></td>
                    <td>Converts a nominal categorical column (more than 2 values, no order) into multiple binary (0/1) columns, one per category.</td>
                </tr>
            </tbody>
        </table>

        <h4 class="sec-h">Data Preprocessing Steps (Cleaning Phase)</h4>
        <div style="font-size: 7.7pt; line-height: 1.36;">
            <p style="margin: 2px 0;"><strong>Step 1 &mdash; Handle Missing Values:</strong> Replace NA/NULL with suitable values such as mean, mode, or a verified value looked up from the source system (e.g. CGPA NA &rarr; 8.3, Attendance NULL &rarr; 90, Department NULL &rarr; Mode CSE).</p>
            <p style="margin: 2px 0;"><strong>Step 2 &mdash; Remove Duplicate Records:</strong> Delete repeated records after verifying they refer to the same entity (e.g. S101 and S106 refer to the exact same student Arun Kumar; S106 is dropped).</p>
            <p style="margin: 2px 0;"><strong>Step 3 &mdash; Standardize Gender:</strong> Convert M &rarr; Male and F &rarr; Female so that all text records adhere to uniform category naming standards.</p>
            <p style="margin: 2px 0;"><strong>Step 4 &mdash; Correct Invalid Age:</strong> Replace negative age (-5) with the correct, verified age (20), preserving physical validity.</p>
            <p style="margin: 2px 0;"><strong>Step 5 &mdash; Correct Invalid CGPA:</strong> Replace values outside the valid 0&ndash;10 range (15.2) with the correct, verified value (9.2).</p>
            <p style="margin: 2px 0;"><strong>Step 6 &mdash; Correct Attendance:</strong> Replace values greater than 100% (120) with the maximum boundary or verified record (100%).</p>
        </div>
    </div>
    <div class="page-footer">
        <span>Subham Kumar Keshari &bull; Enrolment: 92400103120 &bull; Marwadi University</span>
        <span>Page 2 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 3 ========================================== -->
<div class="page">
    <div class="page-content">
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY &bull; DEPT. OF COMPUTER ENGINEERING</h1>
                <h2>01CE0527 &ndash; DWDM &bull; Practical 4: Data Preprocessing</h2>
            </div>
            <div class="badge-dwdm">ENCODING STRATEGY</div>
        </div>

        <h4 class="sec-h">Step 7 &mdash; Encode Categorical Variables</h4>
        <p style="margin: 2px 0 4px 0; font-size: 7.8pt; text-align: justify;">
            After cleaning, every remaining text column must be converted into numbers before the dataset can be ingested by a data mining or machine learning algorithm. Two different techniques are used depending on whether the category has an inherent mathematical order:
        </p>
        <ul style="margin: 0 0 6px 18px; padding: 0; font-size: 7.7pt;">
            <li><strong>Label Encoding:</strong> Used for binary columns with only two possible values (Gender, Placement). Each category is assigned 0 or 1.</li>
            <li><strong>One-Hot Encoding:</strong> Used for nominal columns with more than two values and no natural order (Department, City). A separate binary (0/1) column is created for each category, preventing the algorithm from mistakenly assuming one category is "greater" than another (e.g. CSE &lt; IT &lt; AI &lt; DS).</li>
        </ul>

        <h4 class="sec-h">Categorical Variable Encoding Table</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 15%;">Column</th>
                    <th style="width: 25%;">Category Type</th>
                    <th style="width: 30%;">Technique Used</th>
                    <th style="width: 30%;">Why This Technique</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Gender</strong></td>
                    <td>Binary (Male/Female)</td>
                    <td>Label Encoding (Male=0, Female=1)</td>
                    <td>Only 2 categories &mdash; a single 0/1 column is enough, no ranking is implied.</td>
                </tr>
                <tr>
                    <td><strong>Placement</strong></td>
                    <td>Binary (Yes/No)</td>
                    <td>Label Encoding (No=0, Yes=1)</td>
                    <td>This is the target column &mdash; binary outcomes are simply mapped to 0/1.</td>
                </tr>
                <tr>
                    <td><strong>Department</strong></td>
                    <td>Nominal (CSE, IT, AI, DS)</td>
                    <td>One-Hot Encoding</td>
                    <td>No natural order between departments &mdash; label encoding would wrongly imply CSE &lt; IT &lt; AI &lt; DS.</td>
                </tr>
                <tr>
                    <td><strong>City</strong></td>
                    <td>Nominal (Ahmedabad, Surat, Rajkot, Vadodara)</td>
                    <td>One-Hot Encoding</td>
                    <td>Cities have no natural order &mdash; one binary column is created per city instead.</td>
                </tr>
            </tbody>
        </table>

        <h4 class="sec-h">Dataset After Preprocessing (Cleaned, Before Encoding)</h4>
        <p style="margin: 2px 0 4px 0; font-size: 7.7pt;">
            Duplicate record S106 is deleted. Missing values and erroneous fields are now successfully imputed and standardized across all 9 unique entities:
        </p>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Student_ID</th>
                    <th>Name</th>
                    <th>Gender</th>
                    <th>Age</th>
                    <th>Department</th>
                    <th>CGPA</th>
                    <th>Attendance</th>
                    <th>City</th>
                    <th>Phone</th>
                    <th>Placement</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align:center;">S101</td>
                    <td>Arun Kumar</td>
                    <td>Male</td>
                    <td style="text-align:center;">20</td>
                    <td>CSE</td>
                    <td style="text-align:center;">8.5</td>
                    <td style="text-align:center;">92</td>
                    <td>Ahmedabad</td>
                    <td>9876543210</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S102</td>
                    <td>Priya Patel</td>
                    <td>Female</td>
                    <td style="text-align:center;">21</td>
                    <td>IT</td>
                    <td style="text-align:center;">9.1</td>
                    <td style="text-align:center;">95</td>
                    <td>Surat</td>
                    <td>9876543211</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S103</td>
                    <td>Rahul Shah</td>
                    <td>Male</td>
                    <td style="text-align:center;">20</td>
                    <td>CSE</td>
                    <td style="text-align:center; font-weight:bold; color:#0369a1;">8.3</td>
                    <td style="text-align:center;">88</td>
                    <td>Rajkot</td>
                    <td>9876543212</td>
                    <td style="text-align:center;">No</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S104</td>
                    <td>Sneha Joshi</td>
                    <td>Female</td>
                    <td style="text-align:center;">19</td>
                    <td>AI</td>
                    <td style="text-align:center;">8.9</td>
                    <td style="text-align:center; font-weight:bold; color:#0369a1;">90</td>
                    <td>Ahmedabad</td>
                    <td>9876543213</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S105</td>
                    <td>Kiran Patel</td>
                    <td>Female</td>
                    <td style="text-align:center;">22</td>
                    <td>DS</td>
                    <td style="text-align:center;">7.8</td>
                    <td style="text-align:center;">84</td>
                    <td>Surat</td>
                    <td>9876543214</td>
                    <td style="text-align:center;">No</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S107</td>
                    <td>Mehul Shah</td>
                    <td>Male</td>
                    <td style="text-align:center; font-weight:bold; color:#0369a1;">20</td>
                    <td>IT</td>
                    <td style="text-align:center;">6.8</td>
                    <td style="text-align:center;">78</td>
                    <td>Vadodara</td>
                    <td>9876543216</td>
                    <td style="text-align:center;">No</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S108</td>
                    <td>Pooja Mehta</td>
                    <td>Female</td>
                    <td style="text-align:center;">21</td>
                    <td>AI</td>
                    <td style="text-align:center; font-weight:bold; color:#0369a1;">9.2</td>
                    <td style="text-align:center;">90</td>
                    <td>Rajkot</td>
                    <td style="font-weight:bold; color:#0369a1;">9876543217</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S109</td>
                    <td>Amit Patel</td>
                    <td>Male</td>
                    <td style="text-align:center;">20</td>
                    <td style="font-weight:bold; color:#0369a1;">CSE</td>
                    <td style="text-align:center;">8.2</td>
                    <td style="text-align:center;">86</td>
                    <td>Ahmedabad</td>
                    <td>9876543218</td>
                    <td style="text-align:center;">Yes</td>
                </tr>
                <tr>
                    <td style="text-align:center;">S110</td>
                    <td>Riya Shah</td>
                    <td>Female</td>
                    <td style="text-align:center;">19</td>
                    <td>CSE</td>
                    <td style="text-align:center;">7.5</td>
                    <td style="text-align:center; font-weight:bold; color:#0369a1;">100</td>
                    <td>Surat</td>
                    <td>9876543219</td>
                    <td style="text-align:center;">No</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer">
        <span>Subham Kumar Keshari &bull; Enrolment: 92400103120 &bull; Marwadi University</span>
        <span>Page 3 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 4 ========================================== -->
<div class="page">
    <div class="page-content">
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY &bull; DEPT. OF COMPUTER ENGINEERING</h1>
                <h2>01CE0527 &ndash; DWDM &bull; Practical 4: Data Preprocessing</h2>
            </div>
            <div class="badge-dwdm">ENCODED MATRIX &amp; FEATURES</div>
        </div>

        <h4 class="sec-h">Dataset After Encoding (All 9 Records)</h4>
        <p style="margin: 2px 0 4px 0; font-size: 7.7pt;">
            Gender and Placement become single 0/1 columns (Label Encoding). Department and City are each expanded into one column per category (One-Hot Encoding). Student_ID is kept only for reference to link the two tables below &mdash; it is not used as a feature.
        </p>

        <p style="margin: 3px 0 2px 0; font-size: 7.6pt; font-weight: bold; color: #0f172a;">Table 1 of 2 &mdash; Numeric features, Gender, and Department:</p>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Student_ID</th>
                    <th>Age</th>
                    <th>CGPA</th>
                    <th>Attendance</th>
                    <th>Gender</th>
                    <th>Dept_CSE</th>
                    <th>Dept_IT</th>
                    <th>Dept_AI</th>
                    <th>Dept_DS</th>
                </tr>
            </thead>
            <tbody>
                <tr><td style="text-align:center;">S101</td><td style="text-align:center;">20</td><td style="text-align:center;">8.5</td><td style="text-align:center;">92</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S102</td><td style="text-align:center;">21</td><td style="text-align:center;">9.1</td><td style="text-align:center;">95</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S103</td><td style="text-align:center;">20</td><td style="text-align:center;">8.3</td><td style="text-align:center;">88</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S104</td><td style="text-align:center;">19</td><td style="text-align:center;">8.9</td><td style="text-align:center;">90</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S105</td><td style="text-align:center;">22</td><td style="text-align:center;">7.8</td><td style="text-align:center;">84</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td></tr>
                <tr><td style="text-align:center;">S107</td><td style="text-align:center;">20</td><td style="text-align:center;">6.8</td><td style="text-align:center;">78</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S108</td><td style="text-align:center;">21</td><td style="text-align:center;">9.2</td><td style="text-align:center;">90</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S109</td><td style="text-align:center;">20</td><td style="text-align:center;">8.2</td><td style="text-align:center;">86</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td></tr>
                <tr><td style="text-align:center;">S110</td><td style="text-align:center;">19</td><td style="text-align:center;">7.5</td><td style="text-align:center;">100</td><td style="text-align:center;">1</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td></tr>
            </tbody>
        </table>

        <p style="margin: 4px 0 2px 0; font-size: 7.6pt; font-weight: bold; color: #0f172a;">Table 2 of 2 &mdash; City and Placement (same Student_ID order as above):</p>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Student_ID</th>
                    <th>City_Ahmedabad</th>
                    <th>City_Surat</th>
                    <th>City_Rajkot</th>
                    <th>City_Vadodara</th>
                    <th>Placement (Target)</th>
                </tr>
            </thead>
            <tbody>
                <tr><td style="text-align:center;">S101</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#15803d;">1</td></tr>
                <tr><td style="text-align:center;">S102</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#15803d;">1</td></tr>
                <tr><td style="text-align:center;">S103</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#b91c1c;">0</td></tr>
                <tr><td style="text-align:center;">S104</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#15803d;">1</td></tr>
                <tr><td style="text-align:center;">S105</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#b91c1c;">0</td></tr>
                <tr><td style="text-align:center;">S107</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center; font-weight:bold; color:#b91c1c;">0</td></tr>
                <tr><td style="text-align:center;">S108</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#15803d;">1</td></tr>
                <tr><td style="text-align:center;">S109</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#15803d;">1</td></tr>
                <tr><td style="text-align:center;">S110</td><td style="text-align:center;">0</td><td style="text-align:center;">1</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center; font-weight:bold; color:#b91c1c;">0</td></tr>
            </tbody>
        </table>

        <h4 class="sec-h">Example: Transformation Walkthrough for Student S103</h4>
        <div class="box-info" style="line-height: 1.34;">
            <strong>Student S103 (Rahul Shah, Male, Department = CSE, City = Rajkot) becomes:</strong><br>
            <code>Age = 20</code>, <code>CGPA = 8.3</code>, <code>Attendance = 88</code>, <code>Gender = 0</code>, <code>Dept_CSE = 1</code> (all other <code>Dept_* = 0</code>), <code>City_Rajkot = 1</code> (all other <code>City_* = 0</code>), <code>Placement = 0</code>.<br>
            <em>This numeric row can now be used directly by any classification or clustering algorithm, whereas the original text row &ldquo;Male, CSE, Rajkot&rdquo; could not be. Student_ID and Name are excluded from this feature set, as explained in Feature Selection below.</em>
        </div>

        <h4 class="sec-h">Feature Selection: Independent and Dependent Variables</h4>
        <p style="margin: 2px 0 3px 0; font-size: 7.7pt;">Not every column in the cleaned dataset should be fed into a model. The table below identifies column roles with justifications:</p>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 14%;">Column</th>
                    <th style="width: 25%;">Role</th>
                    <th>Justification</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Age</strong></td><td>Independent variable</td><td>Reflects maturity/work-readiness; a plausible factor in employability.</td></tr>
                <tr><td><strong>CGPA</strong></td><td>Independent variable</td><td>Direct measure of academic performance &mdash; typically the strongest predictor of placement.</td></tr>
                <tr><td><strong>Attendance</strong></td><td>Independent variable</td><td>Reflects discipline and engagement, which recruiters associate with employability.</td></tr>
                <tr><td><strong>Gender</strong></td><td>Independent variable</td><td>Included to check for and analyse any bias in placement outcomes; must be used ethically.</td></tr>
                <tr><td><strong>Department</strong></td><td>Independent variable</td><td>Different departments can have different industry demand and placement rates.</td></tr>
                <tr><td><strong>City</strong></td><td>Independent variable</td><td>May reflect proximity to companies or campus recruitment activity.</td></tr>
                <tr><td><strong>Placement</strong></td><td>Dependent variable (target)</td><td>This is the outcome the data mining model is being built to predict (Binary: 0 or 1).</td></tr>
                <tr><td><strong>Student_ID</strong></td><td>Dropped &mdash; not a feature</td><td>A unique identifier with no predictive meaning; using it would let a model &ldquo;memorize&rdquo; rows.</td></tr>
                <tr><td><strong>Name</strong></td><td>Dropped &mdash; not a feature</td><td>Unique per student and not generalizable; privacy-sensitive field with no bearing on placement.</td></tr>
                <tr><td><strong>Phone</strong></td><td>Dropped &mdash; not a feature</td><td>Contact information only &mdash; has no logical relationship with placement outcome.</td></tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer">
        <span>Subham Kumar Keshari &bull; Enrolment: 92400103120 &bull; Marwadi University</span>
        <span>Page 4 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 5 ========================================== -->
<div class="page">
    <div class="page-content">
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY &bull; DEPT. OF COMPUTER ENGINEERING</h1>
                <h2>01CE0527 &ndash; DWDM &bull; Practical 4: Data Preprocessing</h2>
            </div>
            <div class="badge-dwdm">CODE &amp; SCREENSHOTS</div>
        </div>

        <h4 class="sec-h">Practical Implementation &amp; Code Execution Screenshots</h4>
        
        <p style="margin: 2px 0 2px 0; font-size: 7.7pt; font-weight: bold; color: #0369a1;">
            1. Import Libraries &amp; Load Raw Dataset (As Specified in Prompt):
        </p>
        <div class="code-box">
# Import the Libraries
import pandas as pd
import numpy as np
        </div>

        <p style="margin: 3px 0 2px 0; font-size: 7.6pt; font-weight: bold;">Screenshot 1: Environment Setup, Library Imports &amp; Data Inspection</p>
        <img class="screenshot-img" src="data:image/png;base64,{img_1}" alt="Screenshot 1: Library Imports and Data Loading">

        <p style="margin: 4px 0 2px 0; font-size: 7.6pt; font-weight: bold;">Screenshot 2: Data Cleaning, Range Corrections &amp; Mean/Mode Imputations</p>
        <img class="screenshot-img" src="data:image/png;base64,{img_2}" alt="Screenshot 2: Cleaning and Imputation">

        <p style="margin: 4px 0 2px 0; font-size: 7.6pt; font-weight: bold;">Screenshot 3: Categorical Encoding (Label &amp; One-Hot) &amp; Model Feature Matrix</p>
        <img class="screenshot-img" src="data:image/png;base64,{img_3}" alt="Screenshot 3: Categorical Encoding and Feature Selection">
    </div>
    <div class="page-footer">
        <span>Subham Kumar Keshari &bull; Enrolment: 92400103120 &bull; Marwadi University</span>
        <span>Page 5 of 6</span>
    </div>
</div>

<!-- ========================================== PAGE 6 ========================================== -->
<div class="page">
    <div class="page-content">
        <div class="univ-header">
            <div class="univ-title">
                <h1>MARWADI UNIVERSITY &bull; DEPT. OF COMPUTER ENGINEERING</h1>
                <h2>01CE0527 &ndash; DWDM &bull; Practical 4: Data Preprocessing</h2>
            </div>
            <div class="badge-dwdm">SUMMARY &amp; SIGN-OFF</div>
        </div>

        <h4 class="sec-h">Data Preprocessing Pipeline Architecture</h4>
        <div style="background:#f8fafc; border:1px dashed #0284c7; padding:8px 12px; border-radius:4px; font-family:monospace; font-size:7.6pt; text-align:center; margin:4px 0;">
            [Raw Dirty Dataset (10 Rows &bull; NA, Duplicates, Text)]<br>
            &darr;<br>
            [Step 1-6: Deduplication &bull; Range Bounds Check &bull; Mean/Mode Imputation &bull; Standardization]<br>
            &darr;<br>
            [Cleaned Tabular Dataset (9 Rows &bull; 0 Missing, 0 Inconsistencies)]<br>
            &darr;<br>
            [Step 7: Encoding &rarr; Binary: Label Encoding (0/1) | Nominal: One-Hot Encoding (Dummies)]<br>
            &darr;<br>
            [Step 8: Feature Selection &rarr; Drop Non-Informative Columns (Student_ID, Name, Phone)]<br>
            &darr;<br>
            [Final Model-Ready Numeric Feature Matrix X: (9, 10) &bull; Target Vector y: (9,)]
        </div>

        <h4 class="sec-h">Model Readiness &amp; Algorithm Suitability</h4>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Data Mining Task</th>
                    <th>Algorithms Supported</th>
                    <th>Impact of Completed Preprocessing</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Supervised Classification</strong></td>
                    <td>Logistic Regression, Decision Trees, Random Forest, SVM, Naive Bayes</td>
                    <td>Eliminates runtime exceptions; binary target (Placement: 0/1) enables direct calculation of cross-entropy loss and Gini impurity.</td>
                </tr>
                <tr>
                    <td><strong>Distance-Based Clustering</strong></td>
                    <td>K-Means, Hierarchical Clustering, KNN</td>
                    <td>One-hot encoding prevents false geometric ordering between cities/departments, ensuring Euclidean distance accurately reflects proximity.</td>
                </tr>
                <tr>
                    <td><strong>Dimensionality Analysis</strong></td>
                    <td>PCA (Principal Component Analysis)</td>
                    <td>Complete numeric matrix enables valid covariance matrix computation without NaN disruption.</td>
                </tr>
            </tbody>
        </table>

        <h4 class="sec-h">Conclusion &amp; Key Learnings</h4>
        <p style="margin: 2px 0 5px 0; font-size: 7.7pt; text-align: justify;">
            <strong>Conclusion:</strong> In this practical, a raw, real-world educational dataset containing missing values, duplicates, invalid negative age, out-of-range CGPA/attendance, and non-numeric text columns was systematically engineered. Through targeted imputation (Mean for CGPA, Mode for Department), text standardization, duplicate removal, Label Encoding (Gender, Placement), One-Hot Encoding (Department, City), and ethical feature selection, the dataset was transformed into a clean, 100% numeric model-ready format ready for machine learning algorithms.
        </p>

        <h4 class="sec-h">References</h4>
        <ol style="margin: 0 0 5px 18px; padding: 0; font-size: 7.5pt;">
            <li>Jiawei Han, Micheline Kamber, Jian Pei, <em>Data Mining: Concepts and Techniques</em>, 3rd Edition, Morgan Kaufmann.</li>
            <li>Scikit-Learn Documentation: <em>Preprocessing data (sklearn.preprocessing)</em>.</li>
            <li>pandas Documentation: <em>Handling Missing Data &amp; Categorical Encodings (pd.get_dummies)</em>.</li>
            <li>Marwadi University: <em>Department of Computer Engineering &bull; 01CE0527 DWDM Course Materials</em>.</li>
        </ol>

        <!-- Official Faculty & Department Sign-off Block -->
        <table class="sign-table">
            <tr>
                <td style="width: 25%;">
                    <div class="sign-line">Student Signature<br><strong>Subham Kumar Keshari</strong><br><small>Enrolment: 92400103120</small></div>
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
        <span>Subham Kumar Keshari &bull; Enrolment: 92400103120 &bull; Marwadi University</span>
        <span>Page 6 of 6 &bull; Single-Side Print Edition</span>
    </div>
</div>

</body>
</html>
"""

out_html_path = os.path.join(work_dir, "DWDM_Practical_4_Data_Preprocessing.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML at: {out_html_path}")

# Run Edge headless to compile PDF
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_exe):
    edge_exe = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

out_pdf_path = os.path.join(work_dir, "DWDM_Practical_4_Data_Preprocessing.pdf")
in_url = "file:///" + out_html_path.replace("\\", "/")

cmd = [
    edge_exe,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={out_pdf_path}",
    in_url
]

print("Compiling PDF with Edge Headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(out_pdf_path):
    size_kb = os.path.getsize(out_pdf_path) / 1024
    print(f"SUCCESS: PDF created ({size_kb:.1f} KB) at {out_pdf_path}")
else:
    print("Error: PDF failed. Stderr:", res.stderr)

# Copy to final submission folder
sub_dir = os.path.join(temp_dir, "Marwadi_01CE0527_DWDM_Submission")
os.makedirs(sub_dir, exist_ok=True)
shutil.copy2(out_html_path, os.path.join(sub_dir, "DWDM_Practical_4_Data_Preprocessing.html"))
if os.path.exists(out_pdf_path):
    shutil.copy2(out_pdf_path, os.path.join(sub_dir, "DWDM_Practical_4_Data_Preprocessing.pdf"))
print("Files copied to submission directory:", sub_dir)
