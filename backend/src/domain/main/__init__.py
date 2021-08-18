from flask import Flask, Blueprint

api_main = Blueprint("main", __name__)


@api_main.route("/")
def index():
    return "HELLO_WORLD"