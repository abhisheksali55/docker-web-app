from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>EB Bank</title>
    <style>
        body {
            margin:0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg,#0f172a,#1e293b);
            color:white;
        }

        .navbar {
            background:#020617;
            padding:15px;
            text-align:center;
            font-size:22px;
            font-weight:bold;
        }

        .container {
            width:350px;
            margin:80px auto;
            background:#1e293b;
            padding:30px;
            border-radius:15px;
            box-shadow:0px 0px 20px rgba(0,0,0,0.5);
        }

        input {
            width:100%;
            padding:12px;
            margin:10px 0;
            border:none;
            border-radius:8px;
        }

        button {
            width:100%;
            padding:12px;
            background:#22c55e;
            border:none;
            border-radius:8px;
            color:white;
            font-size:16px;
            cursor:pointer;
        }

        .card {
            background:#0f172a;
            padding:15px;
            border-radius:10px;
            margin-top:15px;
        }

        .success {
            color:#22c55e;
        }
    </style>
</head>

<body>

<div class="navbar">🏦 EB Bank</div>

<div class="container">

{% if not logged %}
    <h2>Secure Login</h2>
    <form method="POST">
        <input name="user" placeholder="Username" required>
        <input name="pass" type="password" placeholder="Password" required>
        <button>Login</button>
    </form>
{% else %}
    <h2>Welcome, Admin</h2>

    <div class="card">
        <h3>Balance</h3>
        <h2>₹50,000</h2>
    </div>

    <div class="card">
        <h3>Send Money</h3>
        <form method="POST">
            <input name="amount" type="number" placeholder="Enter Amount" required>
            <button name="send">Transfer</button>
        </form>
    </div>

    {% if msg %}
        <p class="success">{{msg}}</p>
    {% endif %}
{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        if "user" in request.form:
            if request.form["user"]=="admin" and request.form["pass"]=="1234":
                return render_template_string(HTML, logged=True, msg="")
        if "amount" in request.form:
            return render_template_string(HTML, logged=True, msg="✅ Transaction Successful")
    return render_template_string(HTML, logged=False, msg="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
