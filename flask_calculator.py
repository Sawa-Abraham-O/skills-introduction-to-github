

#app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<html>
<body>
<h1>Simple Calculator</h1>
<form action="/" method="post">
<input type="number" name="num1" placeholder="Number 1">
<select name="operator">
<option value="+">+</option>
<option value="-">-</option>
<option value="_">_</option>
<option value="/">/</option>
</select>
<input type="number" name="num2" placeholder="Number 2">
<input type="submit" value="Calculate">
</form>
{% if result %}
<p>Result: {{ result }}</p>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        operator = request.form["operator"]
        num2 = float(request.form["num2"])
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero!"
        return render_template_string(HTML_TEMPLATE, result=result)
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run()

