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
    margin: 0;
    color: white;
    text-align: center;
    font-family: Arial;
    overflow-x: hidden;
}

/* 🌌 BLACK HOLE BACKGROUND */
.blackhole-bg {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 120%;
    height: 120%;
    transform: translate(-50%, -50%);
    background: url("{{ url_for('static', filename='blackhole.jpg') }}") center/cover no-repeat;
    animation: spin 80s linear infinite;
    z-index: -2;
    filter: brightness(0.7) contrast(1.2);
}

/* 🌟 STARS */
.stars {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: -1;
}

.stars::after {
    content: "";
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    box-shadow:
        20px 30px white,
        80px 120px white,
        150px 200px white,
        300px 50px white,
        450px 180px white,
        600px 100px white,
        750px 220px white,
        900px 90px white,
        1100px 160px white,
        1300px 60px white,
        1500px 200px white;
    animation: blink 2s infinite alternate;
}

@keyframes blink {
    0% { opacity: 0.3; }
    100% { opacity: 1; }
}

/* 🔄 BLACK HOLE ROTATION */
@keyframes spin {
    0% { transform: translate(-50%, -50%) rotate(0deg) scale(1.1); }
    100% { transform: translate(-50%, -50%) rotate(360deg) scale(1.1); }
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 15px 30px;
    background: rgba(0,0,0,0.6);
}

/* SVG */
svg {
    width: 300px;
    height: 200px;
}

.bg {
    fill: none;
    stroke: #ccc;
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

.aws { background: #ff9900; }
.azure { background: #007fff; }
.gcp { background: #34a853; }

/* SERVICES */
.services {
    display: none;
    margin-top: 20px;
}

.card {
    background: rgba(0,0,0,0.6);
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
    color: black;
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
    background: rgba(0,0,0,0.8);
    display: none;
    border-radius: 10px;
}
</style>
</head>

<body>

<!-- 🌌 BACKGROUND -->
<div class="blackhole-bg"></div>
<div class="stars"></div>

<!-- NAVBAR -->
<div class="navbar">
    <div>☰ Menu</div>
    <div>⚙️ Settings | 🔐 Login</div>
</div>

<h2>SPACE UNIVERSE 🪐</h2>

<!-- INFINITY SNAKE -->
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

<!-- SERVICES -->
<div id="aws" class="services">
    <div class="card">EC2</div>
    <div class="card">S3</div>
    <div class="card">Lambda</div>
</div>

<div id="azure" class="services">
    <div class="card">VM</div>
    <div class="card">Blob</div>
    <div class="card">Functions</div>
</div>

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
