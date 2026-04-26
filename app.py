from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background: #000;
    color: white;
    text-align: center;
    margin: 0;
    font-family: Arial;
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 15px 30px;
    background: #111;
}

/* SVG */
svg {
    width: 300px;
    height: 200px;
}

.bg {
    fill: none;
    stroke: #333;
    stroke-width: 8;
}

.snake {
    fill: none;
    stroke: #00ffcc;
    stroke-width: 8;
    stroke-linecap: round;
    stroke-dasharray: 100;
    animation: move 2s linear infinite;
}

@keyframes move {
    0% { stroke-dashoffset: 0; }
    100% { stroke-dashoffset: 400; }
}

/* BUTTONS */
.btn {
    padding: 12px 25px;
    margin: 10px;
    border: none;
    border-radius: 30px;
    font-weight: bold;
    color: white;
    cursor: pointer;
}

.aws { background: orange; }
.azure { background: blue; }
.gcp { background: green; }

/* SERVICES */
.services {
    display: none;
    margin-top: 20px;
}

.card {
    background: #111;
    padding: 10px 20px;
    margin: 10px;
    border-radius: 10px;
    display: inline-block;
}

/* AI BUTTON */
.ai-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #00ffcc;
    padding: 15px;
    border-radius: 50%;
    cursor: pointer;
}

/* CHATBOX */
.chatbox {
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 300px;
    background: #111;
    display: none;
    border-radius: 10px;
}

</style>
</head>

<body>

<div class="navbar">
    <div>☰ Menu</div>
    <div>⚙️ Settings | 🔐 Login</div>
</div>

<h2>DevOps App 🚀</h2>

<svg viewBox="0 0 200 100">
    <path class="bg"
        d="M 20 50 C 20 10, 80 10, 100 50 
           C 120 90, 180 90, 180 50 
           C 180 10, 120 10, 100 50 
           C 80 90, 20 90, 20 50" />
    <path class="snake"
        d="M 20 50 C 20 10, 80 10, 100 50 
           C 120 90, 180 90, 180 50 
           C 180 10, 120 10, 100 50 
           C 80 90, 20 90, 20 50" />
</svg>

<p>Docker DevOps App Running...</p>

<!-- BUTTONS -->
<div>
    <button class="btn aws" onclick="show('aws')">AWS</button>
    <button class="btn azure" onclick="show('azure')">AZURE</button>
    <button class="btn gcp" onclick="show('gcp')">GCP</button>
</div>

<!-- AWS -->
<div id="aws" class="services">
    <div class="card">EC2</div>
    <div class="card">S3</div>
    <div class="card">Lambda</div>
</div>

<!-- AZURE -->
<div id="azure" class="services">
    <div class="card">VM</div>
    <div class="card">Blob</div>
    <div class="card">Functions</div>
</div>

<!-- GCP -->
<div id="gcp" class="services">
    <div class="card">Compute</div>
    <div class="card">Storage</div>
    <div class="card">BigQuery</div>
</div>

<!-- AI BUTTON -->
<div class="ai-btn" onclick="toggleChat()">🤖</div>

<div id="chatbox" class="chatbox">
    <div style="padding:10px;">AI Chat</div>
</div>

<script>
function show(id){
    document.getElementById("aws").style.display="none";
    document.getElementById("azure").style.display="none";
    document.getElementById("gcp").style.display="none";
    document.getElementById(id).style.display="block";
}

function toggleChat(){
    let box = document.getElementById("chatbox");
    box.style.display = box.style.display==="block"?"none":"block";
}
</script>

</body>
</html>
""")

app.run(host="0.0.0.0", port=5000)
