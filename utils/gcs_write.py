from google.cloud import storage
from loguru import logger

def write_file(bucket_name: str, local_path: str):
    sc = storage.Client()
    b = sc.bucket(bucket_name)
    blob = b.blob("contacts.json")
    blob.upload_from_file(local_path)

    logger.info("file uploaded")

