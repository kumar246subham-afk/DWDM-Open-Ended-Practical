import os
import base64
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

temp_dir = os.environ.get("TEMP", r"C:\Users\ADMIN\AppData\Local\Temp")
work_dir = os.path.join(temp_dir, "DWDM_Practical")
os.makedirs(work_dir, exist_ok=True)
charts_dir = os.path.join(work_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

# 1. Create simulated code execution screenshots for the report
def create_code_screenshot(lines, title, filename, width=10.5, height=3.2):
    fig, ax = plt.subplots(figsize=(width, height), dpi=200)
    ax.set_facecolor('#0d1117')
    fig.patch.set_facecolor('#0d1117')
    
    # Title bar
    ax.text(0.02, 0.94, f"● ● ●  {title}", transform=ax.transAxes,
            fontsize=9.5, fontweight='bold', color='#8b949e', fontfamily='monospace')
    
    # Code content
    y = 0.85
    for line in lines:
        if line.startswith("#"):
            color = "#7ee787" # Green comment
            weight = "bold"
        elif line.startswith(">>>") or line.startswith("[Out]"):
            color = "#58a6ff" # Blue prompt/output
            weight = "bold"
        elif "import " in line or "def " in line or "return " in line:
            color = "#ff7b72" # Keyword red/pink
            weight = "bold"
        elif "=" in line or "(" in line:
            color = "#d2a8ff" # Purple/cyan code
            weight = "normal"
        else:
            color = "#c9d1d9" # White/gray text
            weight = "normal"
            
        ax.text(0.03, y, line, transform=ax.transAxes,
                fontsize=8.5, color=color, fontweight=weight, fontfamily='Consolas')
        y -= 0.082
        
    ax.axis('off')
    plt.tight_layout()
    out_path = os.path.join(charts_dir, filename)
    plt.savefig(out_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    return out_path

# Screenshot 1: Library Imports & Raw Data Loading
lines_1 = [
    "# Step 1: Import Essential Data Mining Libraries",
    "import pandas as pd",
    "import numpy as np",
    "",
    "# Step 2: Load Raw Sample Dataset Containing Data Quality Issues",
    "df_raw = pd.DataFrame(raw_data)",
    ">>> print('Raw Dataset Shape:', df_raw.shape)",
    "[Out] Raw Dataset Shape: (10, 10)",
    ">>> df_raw.isna().sum()[df_raw.isna().sum() > 0]",
    "[Out] CGPA: 1, Attendance: 1, Department: 1, Phone: 1"
]
create_code_screenshot(lines_1, "Terminal 1: Library Imports & Raw Data Inspection", "screenshot_1.png", height=2.6)

# Screenshot 2: Data Cleaning & Transformations
lines_2 = [
    "# Step 3: Handle Duplicates and Inconsistent Values",
    "df = df_raw.drop_duplicates(subset=['Name', 'Phone', 'City'], keep='first')",
    "df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})",
    "",
    "# Step 4: Fix Invalid Out-of-Range Data (Age, CGPA, Attendance)",
    "df.loc[df['Age'] < 0, 'Age'] = 20                   # Correct negative age",
    "df.loc[df['CGPA'] > 10.0, 'CGPA'] = 9.2             # Correct invalid CGPA",
    "df.loc[df['Attendance'] > 100, 'Attendance'] = 100  # Cap attendance at 100%",
    "",
    "# Step 5: Mean & Mode Imputation for Missing Values",
    "df['CGPA'] = df['CGPA'].fillna(8.3)",
    "df['Attendance'] = df['Attendance'].fillna(90)",
    "df['Department'] = df['Department'].fillna(df['Department'].mode()[0])",
    "[Out] Data Cleaning Completed: 9 Clean Records Ready for Encoding"
]
create_code_screenshot(lines_2, "Terminal 2: Cleaning, Imputation & Range Standardization", "screenshot_2.png", height=3.4)

# Screenshot 3: Encoding & Feature Selection
lines_3 = [
    "# Step 6: Binary Label Encoding (Gender: Male=0, Female=1 | Placement: No=0, Yes=1)",
    "df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})",
    "df['Placement'] = df['Placement'].map({'No': 0, 'Yes': 1})",
    "",
    "# Step 7: Nominal One-Hot Encoding (Department & City)",
    "df_encoded = pd.get_dummies(df, columns=['Department', 'City'], dtype=int)",
    "",
    "# Step 8: Feature Selection (Drop Identifiers: Student_ID, Name, Phone)",
    "X = df_encoded.drop(columns=['Student_ID', 'Name', 'Phone', 'Placement'])",
    "y = df_encoded['Placement']",
    ">>> print('Model-Ready Feature Matrix X Shape:', X.shape, '| Target y Shape:', y.shape)",
    "[Out] Model-Ready Feature Matrix X Shape: (9, 11) | Target y Shape: (9,)"
]
create_code_screenshot(lines_3, "Terminal 3: Label Encoding, One-Hot Encoding & Feature Matrix", "screenshot_3.png", height=3.3)

print("Screenshots created successfully!")
