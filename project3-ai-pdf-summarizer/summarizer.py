import PyPDF2
import re
import requests

HF_TOKEN = "YOUR_HUGGINGFACE_TOKEN"

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

pdf_path = "sample_pdfs/sample.pdf"

# 1️⃣ Read PDF
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

# 2️⃣ Clean text
text = re.sub(r"\s+", " ", text).strip()

# 3️⃣ Send to AI
response = requests.post(
    API_URL,
    headers=HEADERS,
    json={"inputs": text[:3000]}
)

result = response.json()

# 4️⃣ Extract summary text
summary_text = result[0]["summary_text"]

# 5️⃣ Save summary to file
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print("✅ AI Summary created and saved to summary.txt\n")
print(summary_text)
