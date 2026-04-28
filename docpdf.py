from pypdf import PdfReader

path = "acc.pdf"

reader = PdfReader(path)
print("Total pages:", len(reader.pages), flush=True)
a =[]
with open("acc_chua_check.txt", 'a', encoding='utf-8') as f:

    for i, page in enumerate(reader.pages[6930:], start = 6931):
        if i % 100 == 0:
            print(f"Đang xử lý trang {i}/{len(reader.pages)}", flush=True)

        text = page.extract_text() or ""
        f.write(f"{text}\n")

        if text.strip():
            print(f"\n--- Page {i} ---", flush=True)
        