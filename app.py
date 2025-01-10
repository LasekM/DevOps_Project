from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        if num1 and num2:
            try:
                num1 = float(num1)
                num2 = float(num2)
                if operation == "add":
                    result = num1 + num2
                elif operation == "subtract":
                    result = num1 - num2
                elif operation == "multiply":
                    result = num1 * num2
                elif operation == "divide":
                    if num2 == 0:
                        result = "Error: Cannot divide by zero."
                    else:
                        result = num1 / num2
            except ValueError:
                result = "Please enter valid numbers."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)