from app.retrieval.metadata_service import MetadataService

service = MetadataService()

print(service.find_reports("Alaska door plug"))
