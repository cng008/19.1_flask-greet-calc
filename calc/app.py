from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def to_add():
    """ Add a and b params """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = add(a, b)

    return str(res)

@app.route('/sub')
def to_sub():
    """ Subtract a and b params """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = sub(a, b)

    return str(res)

@app.route('/mult')
def to_mult():
    """ Multiply a and b params """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a, b)

    return str(res)


@app.route('/div')
def to_div():
    """ Divide a and b params """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = div(a, b)

    return str(res)

# PART 2
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