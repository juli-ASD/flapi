from types import MethodType
from flask import Flask, jsonify, request
from flask.globals import session
from db import Session, engine
from models import Usuario

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "El método GET responde"})


if __name__ == '__main__':
    app.run(debug=True)

