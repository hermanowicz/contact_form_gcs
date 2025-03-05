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
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")

@route("/cloud")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")

@route("/ai-agents")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")

@route("/dev-ops")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")

@route("/contact")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")

@route("/privacy-policy")
def index():
    logger.info(f"request to: {request.path}, from: {request.remote_addr}")
    return template("index")



run(host='0.0.0.0', server='gunicorn', port=str(PORT), reloader=True)
