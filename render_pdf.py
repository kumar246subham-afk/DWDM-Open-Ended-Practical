import os
import base64
import shutil
import subprocess

temp_dir = os.environ.get("TEMP", r"C:\Users\ADMIN\AppData\Local\Temp")
work_dir = os.path.join(temp_dir, "DWDM_Practical")
charts_dir = os.path.join(work_dir, "charts")

def get_b64(fname):
    p = os.path.join(charts_dir, fname)
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_tcs = get_b64("candle_company_1.png")
img_rel = get_b64("candle_company_2.png")
img_infy = get_b64("candle_company_3.png")
img_cmp = get_b64("comparative_metrics.png")

template_path = os.path.join(work_dir, "template.html")
with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("__IMG_TCS__", img_tcs)
html = html.replace("__IMG_REL__", img_rel)
html = html.replace("__IMG_INFY__", img_infy)
html = html.replace("__IMG_CMP__", img_cmp)

out_html_path = os.path.join(work_dir, "DWDM_Open_Ended_Practical_5NumberSummary.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Generated HTML:", out_html_path)

# Find Edge
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_exe):
    edge_exe = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

out_pdf_path = os.path.join(work_dir, "DWDM_Open_Ended_Practical_5NumberSummary.pdf")

if os.path.exists(edge_exe):
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_path}",
        out_html_path
    ]
    print("Converting HTML to PDF via Microsoft Edge...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_pdf_path):
        kb = os.path.getsize(out_pdf_path) / 1024
        print(f"SUCCESS: PDF created ({kb:.1f} KB) at {out_pdf_path}")
    else:
        print("Error: PDF not found. Stderr:", res.stderr)
else:
    print("Edge not found at:", edge_exe)

# Copy to Desktop .net folder as well
desktop_target = r"c:\Users\ADMIN\OneDrive\Desktop\.net\DWDM_Practical"
try:
    os.makedirs(desktop_target, exist_ok=True)
    shutil.copy2(out_html_path, os.path.join(desktop_target, "DWDM_Open_Ended_Practical_5NumberSummary.html"))
    if os.path.exists(out_pdf_path):
        shutil.copy2(out_pdf_path, os.path.join(desktop_target, "DWDM_Open_Ended_Practical_5NumberSummary.pdf"))
    print("Copied files to desktop folder:", desktop_target)
except Exception as e:
    print("Note on copying to desktop:", e)
