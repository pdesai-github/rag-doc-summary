from interfaces.document_reader import DocumentReader
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

class PdfReader(DocumentReader):

    def read(self, file_path):
        pdf_path = Path(file_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"pdf not found - {file_path}")
        
        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError(f"Unsupported file format - {pdf_path.suffix}")
        
        loader = PyMuPDFLoader(str(pdf_path))

        documents = loader.load()

        for index, document in enumerate(documents):
            document.metadata.update({
                "file_name" : pdf_path.name,
                "page_number": index + 1,
                "document_type": "pdf"
            })

        return documents
