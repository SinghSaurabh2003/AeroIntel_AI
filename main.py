#from app.ingestion.pdf_loader import PDFLoader


#loader = PDFLoader("data/raw/ntsb_accidents/AIR2504.pdf")

#document = loader.load()

#print("=" * 50)
#print(f"Filename : {document.filename}")
#print(f"Title    : {document.title}")
#print(f"Source   : {document.source}")
#print(f"Category : {document.category}")
#print(f"Pages    : {document.pages}")
#print("=" * 50)

#print("\nFirst 1000 characters:\n")
#print(document.text[:1000])


from app.indexing.build_index import IndexBuilder


def main():

    builder = IndexBuilder()

    builder.build()


if __name__ == "__main__":
    main()