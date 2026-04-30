from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Payment App</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 100px;
            background: #f2f2f2;
        }
        .box {
            background: white;
            padding: 30px;
            display: inline-block;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        input {
            padding: 10px;
            width: 200px;
            margin: 10px;
        }
        button {
            padding: 10px 20px;
            background: green;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>Payment Page</h2>
    <form method="POST">
        <input type="number" name="amount" placeholder="Enter Amount" required><br>
        <button type="submit">Pay Now</button>
    </form>

    {% if success %}
        <h3 style="color: green;">Payment of ₹{{amount}} Successful ✅</h3>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        amount = request.form.get("amount")
        return render_template_string(HTML_PAGE, success=True, amount=amount)

    return render_template_string(HTML_PAGE, success=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
