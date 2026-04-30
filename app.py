<!DOCTYPE html>
<html>
<head>
    <title>EB Bank</title>
    <style>
        body {
            font-family: Arial;
            margin: 0;
            background: #0f172a;
            color: white;
        }

        .container {
            width: 300px;
            margin: 100px auto;
            background: #1e293b;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 10px;
            border: none;
            border-radius: 5px;
        }

        button {
            padding: 10px 20px;
            background: #22c55e;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        .dashboard {
            display: none;
            padding: 20px;
        }

        .card {
            background: #1e293b;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
        }

        .topbar {
            background: #020617;
            padding: 15px;
            text-align: center;
            font-size: 20px;
        }
    </style>
</head>

<body>

<div class="topbar">🏦 EB Bank</div>

<!-- LOGIN -->
<div class="container" id="loginBox">
    <h2>Login</h2>
    <input type="text" id="user" placeholder="Username"><br>
    <input type="password" id="pass" placeholder="Password"><br>
    <button onclick="login()">Login</button>
</div>

<!-- DASHBOARD -->
<div class="dashboard" id="dashboard">

    <div class="card">
        <h3>Account Balance</h3>
        <h2 id="balance">₹50,000</h2>
    </div>

    <div class="card">
        <h3>Send Money</h3>
        <input type="number" id="amount" placeholder="Enter Amount">
        <button onclick="sendMoney()">Send</button>
    </div>

    <div class="card">
        <h3>Transaction Status</h3>
        <p id="status">No transactions yet</p>
    </div>

</div>

<script>
function login() {
    let u = document.getElementById("user").value;
    let p = document.getElementById("pass").value;

    if (u === "admin" && p === "1234") {
        document.getElementById("loginBox").style.display = "none";
        document.getElementById("dashboard").style.display = "block";
    } else {
        alert("Invalid Login");
    }
}

function sendMoney() {
    let amt = document.getElementById("amount").value;
    let bal = 50000;

    if (amt > 0 && amt <= bal) {
        bal -= amt;
        document.getElementById("balance").innerText = "₹" + bal;
        document.getElementById("status").innerText = "Sent ₹" + amt + " successfully";
    } else {
        alert("Invalid Amount");
    }
}
</script>

</body>
</html>
