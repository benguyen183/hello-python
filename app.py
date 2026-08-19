from flask import Flask, render_template, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["op"]

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Vui lòng nhập số hợp lệ"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
