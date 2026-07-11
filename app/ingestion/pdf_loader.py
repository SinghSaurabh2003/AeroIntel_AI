import os
import fitz

from app.ingestion.document import Document
from app.ingestion.metadata import MetadataExtractor
from app.utils.logger import logger


class PDFLoader:
    """
    Loads PDF documents and extracts text.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):

        logger.info(f"Loading PDF: {self.file_path}")

        try:
            pdf = fitz.open(self.file_path)

        except Exception as e:
            logger.error(f"Error loading PDF: {e}")
            raise

        logger.info(f"Pages found: {pdf.page_count}")

        text = ""

        for page in pdf:
            text += page.get_text()

        # Extract metadata
        extractor = MetadataExtractor()
        meta = extractor.extract(pdf, self.file_path)

        document = Document(
            filename=meta["filename"],
            title=meta["title"],
            source=meta["source"],
            category=meta["category"],
            pages=meta["pages"],
            text=text,
        )

        pdf.close()

        logger.info("Document created successfully.")

        return document