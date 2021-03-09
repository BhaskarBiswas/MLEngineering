from flask import Flask
from flask import request

app = Flask(__name__)


def add(num1, num2):
    """addition"""
    try:
        result = int(num1) + int(num2)
        return str(result)
    except ValueError:
        return "invalid input"
    
def subtract(num1, num2):
    """subtraction"""
    try:
        result = int(num1) - int(num2)
        return str(result)
    except ValueError:
        return "invalid input"
    
def product(num1, num2):
    """product"""
    try:
        result = int(num1) * int(num2)
        return str(result)
    except ValueError:
        return "invalid input"
    
def division(num1, num2):
    """division"""
    try:
        result = int(num1)/int(num2)
        return str(result)
    except ValueError:
        return "invalid input"


@app.route("/")
def index():
    num1 = request.args.get("num1", "")
    num2 = request.args.get("num2", "")
    action = request.args.get("action1", "")
    
    if action == 'add':
        final_result = add(num1, num2)
    elif action == 'subtract':
        final_result = subtract(num1, num2)
    elif action == 'multiply':
        final_result = product(num1, num2)
    elif action == 'divide':
        final_result = division(num1, num2)

    return (
        """<form action="" method="get">
                Number 1: <input type="text" name="num1">
                add/subtract/multiply/divide: <input type="text" name="action1">
                Number 2: <input type="text" name="num2">                               
                <input type="submit" value="Calculate">
            </form>"""
        + num1
        + " "
        + action
        + " "
        + num2
        + " = "
        + final_result
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)