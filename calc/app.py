from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<op>')
def math(op):
    """ do some operation on a and b params """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = operators[op](a, b)

    return str(res)