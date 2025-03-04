from bottle import route, run, request, template
from itsdangerous import URLSafeSerializer
from loguru import logger
from os import getenv
import datetime

PORT = getenv('PORT')
if PORT == None:
    PORT = 8080

@route("/")
def index():
    logger.info(f"index page request, accepted at: {datetime.datetime.now()}")
    return template("index")

run(host='0.0.0.0', server='gunicorn', port=str(PORT))
