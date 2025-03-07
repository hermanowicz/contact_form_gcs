from bottle import route, run, request, template
from itsdangerous import URLSafeSerializer
from loguru import logger
from os import getenv
import secrets

# vars for files, buckets, etc ...

SECRET = secrets.token_urlsafe(48)
BUCKET = "contact-form-app"
DB_FILE = "contacts.json"
LOCAL = "/tmp/" + DB_FILE

# config for itsdangerous,
s = URLSafeSerializer(SECRET, "just-for-fun")

@route("/")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")

@route("/contact")
def contact():
    if request.method == "POST":
        logger.info(f"form post to: {request.path}, from: {request.remote_addr} was made.")
    else:
        return template("contact")

@route("/privacy-policy")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("privacy-policy")



run(host='0.0.0.0', debug=True, reloader=True)
