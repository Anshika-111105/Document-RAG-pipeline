from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "PEFT.pdf"

if pdf_path.exists():
    try:
        loader = PyPDFLoader(file_path=str(pdf_path))
        documents = loader.load()
        
        if documents and len(documents) > 5:
            print(f"✅ Successfully loaded {len(documents)} pages")
            print(f"\nPage 6 content:\n{documents[5].page_content[:500]}")
        else:
            print(f"⚠️ Document loaded but has only {len(documents)} pages")
    except Exception as e:
        print(f"❌ Error loading PDF: {str(e)}")
else:
    print(f"❌ PDF file not found: {pdf_path}")
    print("   Make sure PEFT.pdf exists in the project root")
