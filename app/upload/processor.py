import fitz

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class PDFProcessor:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def process(self, pdf_path):

        pdf = fitz.open(pdf_path)

        docs = []

        for page_no, page in enumerate(pdf):

            text = page.get_text()

            docs.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path,
                        "page": page_no
                    }
                )
            )

        chunks = self.splitter.split_documents(docs)

        return chunks