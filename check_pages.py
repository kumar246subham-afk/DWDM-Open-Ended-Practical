import re

pdf_path = r"C:\Users\ADMIN\AppData\Local\Temp\DWDM_Practical\DWDM_Practical_4_Data_Preprocessing.pdf"
with open(pdf_path, "rb") as f:
    content = f.read()

pages = re.findall(rb"/Type\s*/Page[^s]", content)
print(f"Total Pages in PDF: {len(pages)}")
