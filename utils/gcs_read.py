from google.cloud import storage
from loguru import logger

def save_file(bucket_name: str, file_name: str, local_path: str):
    sc = storage.Client()
    b = sc.bucket(bucket_name)
    blob = b.blob(file_name)
    blob.download_to_file(local_path)

    logger.info("file downloaded")
