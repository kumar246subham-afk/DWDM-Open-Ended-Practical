import os
import base64
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

work_dir = os.environ.get("TEMP", r"C:\Users\ADMIN\AppData\Local\Temp")
work_dir = os.path.join(work_dir, "DWDM_Practical")
os.makedirs(work_dir, exist_ok=True)
charts_dir = os.path.join(work_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

# Set high resolution aesthetic style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9.5
plt.rcParams['axes.linewidth'] = 1.1

companies = [
    {
        "name": "Tata Consultancy Services (TCS)",
        "ticker": "NSE: TCS",
        "sector": "Information Technology",
        "color": "#1565C0",
        "daily": {
            "title": "Daily Candle (Intraday Hourly Intervals - Oct 25, 2024)",
            "data": [4142.50, 4155.00, 4165.40, 4178.20, 4185.00, 4192.50, 4205.00, 4212.00, 4218.00, 4225.00],
            "open": 4150.00, "close": 4220.00
        },
        "weekly": {
            "title": "Weekly Candle (5 Trading Days - Oct 21-25, 2024)",
            "data": [4095.00, 4115.00, 4138.00, 4152.00, 4170.00, 4185.00, 4200.00, 4225.00, 4245.00, 4268.00],
            "open": 4110.00, "close": 4250.00
        },
        "monthly": {
            "title": "Monthly Candle (October 2024 - 4 Weeks Trading Data)",
            "data": [3980.00, 4040.00, 4090.00, 4130.00, 4175.00, 4210.00, 4250.00, 4290.00, 4320.00, 4345.00],
            "open": 4020.00, "close": 4310.00
        }
    },
    {
        "name": "Reliance Industries Limited (RELIANCE)",
        "ticker": "NSE: RELIANCE",
        "sector": "Energy, Oil & Retail Conglomerate",
        "color": "#2E7D32",
        "daily": {
            "title": "Daily Candle (Intraday Hourly Intervals - Oct 25, 2024)",
            "data": [2715.00, 2724.00, 2735.00, 2742.00, 2750.00, 2758.00, 2768.00, 2776.00, 2785.00, 2795.50],
            "open": 2725.00, "close": 2788.00
        },
        "weekly": {
            "title": "Weekly Candle (5 Trading Days - Oct 21-25, 2024)",
            "data": [2685.00, 2705.00, 2722.00, 2740.00, 2760.00, 2778.00, 2795.00, 2810.00, 2822.00, 2830.00],
            "open": 2698.00, "close": 2815.00
        },
        "monthly": {
            "title": "Monthly Candle (October 2024 - 4 Weeks Trading Data)",
            "data": [2620.00, 2665.00, 2700.00, 2735.00, 2775.00, 2805.00, 2835.00, 2860.00, 2880.00, 2895.00],
            "open": 2640.00, "close": 2870.00
        }
    },
    {
        "name": "Infosys Limited (INFY)",
        "ticker": "NSE: INFY",
        "sector": "Information Technology & Consulting",
        "color": "#D84315",
        "daily": {
            "title": "Daily Candle (Intraday Hourly Intervals - Oct 25, 2024)",
            "data": [1855.00, 1862.00, 1870.00, 1878.00, 1888.50, 1895.00, 1902.00, 1910.00, 1916.00, 1922.00],
            "open": 1860.00, "close": 1915.00
        },
        "weekly": {
            "title": "Weekly Candle (5 Trading Days - Oct 21-25, 2024)",
            "data": [1830.00, 1850.00, 1868.00, 1882.00, 1895.00, 1912.00, 1930.00, 1942.00, 1950.00, 1958.00],
            "open": 1845.00, "close": 1948.00
        },
        "monthly": {
            "title": "Monthly Candle (October 2024 - 4 Weeks Trading Data)",
            "data": [1785.00, 1820.00, 1855.00, 1880.00, 1910.00, 1940.00, 1965.00, 1985.00, 1998.00, 2010.00],
            "open": 1805.00, "close": 1995.00
        }
    }
]

def calc_stats(arr):
    arr_s = np.sort(arr)
    minimum = float(np.min(arr_s))
    q1 = float(np.percentile(arr_s, 25))
    median = float(np.median(arr_s))
    q3 = float(np.percentile(arr_s, 75))
    maximum = float(np.max(arr_s))
    iqr = q3 - q1
    mean = float(np.mean(arr_s))
    std = float(np.std(arr_s))
    skew = float((3 * (mean - median)) / std) if std > 0 else 0.0
    return {
        "min": minimum, "q1": q1, "median": median, "q3": q3, "max": maximum,
        "iqr": iqr, "mean": mean, "std": std, "skew": skew
    }

for comp in companies:
    comp["daily"]["stats"] = calc_stats(comp["daily"]["data"])
    comp["weekly"]["stats"] = calc_stats(comp["weekly"]["data"])
    comp["monthly"]["stats"] = calc_stats(comp["monthly"]["data"])

def plot_company_candles(comp, filename):
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.5), dpi=200)
    timeframes = [("Daily", comp["daily"]), ("Weekly", comp["weekly"]), ("Monthly", comp["monthly"])]
    
    for ax, (tf_name, tf_data) in zip(axes, timeframes):
        st = tf_data["stats"]
        open_val = tf_data["open"]
        close_val = tf_data["close"]
        is_bullish = close_val >= open_val
        body_color = '#26a69a' if is_bullish else '#ef5350'
        edge_color = '#004d40' if is_bullish else '#b71c1c'
        
        # Whisker line
        ax.plot([1, 1], [st["min"], st["max"]], color='#212121', linewidth=1.8, zorder=2)
        
        # Caps
        cap_width = 0.10
        ax.plot([1 - cap_width, 1 + cap_width], [st["min"], st["min"]], color='#212121', linewidth=1.8, zorder=2)
        ax.plot([1 - cap_width, 1 + cap_width], [st["max"], st["max"]], color='#212121', linewidth=1.8, zorder=2)
        
        # Box Body (Q1 to Q3)
        box_width = 0.42
        box = patches.Rectangle(
            (1 - box_width/2, st["q1"]), box_width, st["iqr"],
            linewidth=1.5, edgecolor=edge_color, facecolor=body_color, alpha=0.85, zorder=3
        )
        ax.add_patch(box)
        
        # Median line (Q2)
        ax.plot([1 - box_width/2, 1 + box_width/2], [st["median"], st["median"]], color='#FFD600', linewidth=2.4, linestyle='-', zorder=4)
        
        # Labels
        y_span = st["max"] - st["min"]
        ax.text(1.26, st["max"], f"Max: ₹{st['max']:.1f}", va='center', fontsize=8, fontweight='bold', color='#212121')
        ax.text(1.26, st["q3"], f"Q3: ₹{st['q3']:.1f}", va='center', fontsize=8, fontweight='bold', color='#004d40')
        ax.text(0.74, st["median"], f"Med: ₹{st['median']:.1f}", va='center', ha='right', fontsize=8, fontweight='bold', color='#E65100')
        ax.text(1.26, st["q1"], f"Q1: ₹{st['q1']:.1f}", va='center', fontsize=8, fontweight='bold', color='#004d40')
        ax.text(1.26, st["min"], f"Min: ₹{st['min']:.1f}", va='center', fontsize=8, fontweight='bold', color='#212121')
        
        # Subtext badge
        ax.text(0.05, 0.94, f"IQR: ₹{st['iqr']:.1f}\nMean: ₹{st['mean']:.1f}\nSkew: {st['skew']:+.2f}",
                transform=ax.transAxes, va='top', fontsize=7.5,
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.9, edgecolor='#B0BEC5'))
        
        ax.set_title(f"{tf_name} Candle", fontsize=10.5, fontweight='bold', color='#1A237E', pad=8)
        ax.set_xlim(0.3, 1.8)
        ax.set_ylim(st["min"] - y_span * 0.12, st["max"] + y_span * 0.12)
        ax.set_xticks([1])
        ax.set_xticklabels([f"{tf_name} Window"], fontweight='bold', fontsize=9)
        ax.set_ylabel("Stock Price (₹)", fontsize=9, fontweight='bold')
        ax.grid(axis='y', linestyle=':', alpha=0.6)
        ax.set_facecolor('#FAFAFA')

    fig.suptitle(f"{comp['name']} ({comp['ticker']}) - 5-Number Summary Candles", fontsize=11.5, fontweight='bold', y=1.02, color='#0D47A1')
    plt.tight_layout()
    filepath = os.path.join(charts_dir, filename)
    plt.savefig(filepath, dpi=200, bbox_inches='tight')
    plt.close()
    return filepath

comp_imgs = {}
for i, comp in enumerate(companies):
    fn = f"candle_company_{i+1}.png"
    img_path = plot_company_candles(comp, fn)
    with open(img_path, "rb") as f:
        comp_imgs[i] = base64.b64encode(f.read()).decode("utf-8")

# Cross-comparison chart
fig, ax = plt.subplots(figsize=(9.8, 3.2), dpi=200)
c_names = ["TCS (IT)", "RELIANCE (Energy)", "INFY (IT)"]
iqr_vals = [comp["monthly"]["stats"]["iqr"] for comp in companies]
spread_vals = [comp["monthly"]["stats"]["max"] - comp["monthly"]["stats"]["min"] for comp in companies]
std_vals = [comp["monthly"]["stats"]["std"] for comp in companies]

x = np.arange(len(c_names))
w = 0.25
ax.bar(x - w, iqr_vals, width=w, label='Monthly IQR (Spread of middle 50%)', color='#1976D2', edgecolor='#0D47A1')
ax.bar(x, spread_vals, width=w, label='Full Price Range (Max - Min)', color='#388E3C', edgecolor='#1B5E20')
ax.bar(x + w, std_vals, width=w, label='Standard Deviation (σ)', color='#F57C00', edgecolor='#E65100')

for i in range(len(c_names)):
    ax.text(x[i] - w, iqr_vals[i] + 3, f"₹{iqr_vals[i]:.1f}", ha='center', fontsize=7.5, fontweight='bold')
    ax.text(x[i], spread_vals[i] + 3, f"₹{spread_vals[i]:.1f}", ha='center', fontsize=7.5, fontweight='bold')
    ax.text(x[i] + w, std_vals[i] + 3, f"₹{std_vals[i]:.1f}", ha='center', fontsize=7.5, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(c_names, fontweight='bold', fontsize=9.5)
ax.set_ylabel("Price Dispersion (₹)", fontweight='bold', fontsize=9)
ax.set_title("Cross-Company Monthly Volatility & Spread Metrics Comparison", fontweight='bold', fontsize=11, color='#0D47A1', pad=8)
ax.legend(framealpha=0.9, loc='upper right', fontsize=8)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.set_facecolor('#FAFAFA')
plt.tight_layout()
cmp_chart_path = os.path.join(charts_dir, "comparative_metrics.png")
plt.savefig(cmp_chart_path, dpi=200, bbox_inches='tight')
plt.close()

with open(cmp_chart_path, "rb") as f:
    comp_cmp_img = base64.b64encode(f.read()).decode("utf-8")

print("SUCCESS: All charts generated and base64 encoded successfully!")
