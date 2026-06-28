from services.pdf_service import PdfReader

pdf_reader = PdfReader()

documents = pdf_reader.read("data/ms_annual_report.pdf")

for index, doc in enumerate(documents):
    print(f"page {doc.metadata['page_number']}")
    print(doc.page_content)