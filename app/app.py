"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/tripleA", methods=['GET'])
def tripleA_get():
    return CalculatorController.triple_a()


@app.route("/pylint", methods=['GET'])
def pylint_get():
    return CalculatorController.pylint()


@app.route("/design", methods=['GET'])
def design_get():
    return CalculatorController.design()


@app.route("/azure", methods=['GET'])
def azure_get():
    return CalculatorController.azure()


@app.route("/oop", methods=['GET'])
def oop_get():
    return CalculatorController.oop()


@app.route("/command", methods=['GET'])
def command_get():
    return CalculatorController.command()


@app.route("/git", methods=['GET'])
def git_get():
    return CalculatorController.git()


@app.route("/docker", methods=['GET'])
def docker_get():
    return CalculatorController.docker()
