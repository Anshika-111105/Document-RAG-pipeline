from pathlib import Path
from langchain.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "PEFT.pdf"

loader = PyPDFLoader(file_path=pdf_path)
documents = loader.load()

print(documents[5].page_content)
