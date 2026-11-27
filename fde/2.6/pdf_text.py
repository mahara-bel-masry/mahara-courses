from pypdf import PdfReader

reader = PdfReader("invoice.pdf")
print("pages:", len(reader.pages))
text = reader.pages[0].extract_text()
print(text.splitlines()[1])
