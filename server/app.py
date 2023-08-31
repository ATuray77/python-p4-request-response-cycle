#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views.</h1>"

@app.route('/print_string/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}<h2>'

@app.route('/count/<int:num>')
def count(num):
    return 'br'.join(str(i) for i in range(1, num+1))
    

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return  num1 + num2
    elif operation == '-':
        return  num1 - num2
    elif operation == '*':
        return  num1 * num2
    elif operation == 'div':
        return num1 / num2
    elif operation == '%':
        return num1 % num2

    else:
        return "Invalid operation!"
  
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
