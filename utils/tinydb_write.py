from tinydb import TinyDB
from loguru import logger

def add_contact(db_file: str, mail:str, message:str, budget:str, gdpr: str):
    db = TinyDB(db_file)
    db.insert({
        "mail": mail,
        "message": message,
        "budget": budget,
        "gdpr": gdpr
    })

    logger.info(f"write record to db for: {mail}")
