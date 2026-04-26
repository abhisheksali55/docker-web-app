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
                margin-top: 60px;
                font-family: Arial;
            }

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

            .btn-container {
                margin-top: 30px;
            }

            .btn {
                padding: 12px 25px;
                margin: 10px;
                border: none;
                border-radius: 30px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                cursor: pointer;
                transition: 0.3s;
            }

            .aws {
                background: linear-gradient(45deg, #ff9900, #ff6600);
            }

            .azure {
                background: linear-gradient(45deg, #007fff, #00c6ff);
            }

            .gcp {
                background: linear-gradient(45deg, #ea4335, #34a853);
            }

            .btn:hover {
                transform: scale(1.1);
                box-shadow: 0 0 15px rgba(255,255,255,0.3);
            }

            /* 🔥 Services box */
            .services {
                margin-top: 20px;
                display: none;
            }

            .card {
                background: #111;
                padding: 10px 20px;
                margin: 10px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0 0 10px rgba(0,255,200,0.2);
            }
        </style>
    </head>
    <body>

        <h2>Hello dosto welcome to DevOps batch 🚀</h2>

        <svg viewBox="0 0 200 100">
            <path class="bg"
                d="M 20 50 
                   C 20 10, 80 10, 100 50 
                   C 120 90, 180 90, 180 50 
                   C 180 10, 120 10, 100 50 
                   C 80 90, 20 90, 20 50" />

            <path class="snake"
                d="M 20 50 
                   C 20 10, 80 10, 100 50 
                   C 120 90, 180 90, 180 50 
                   C 180 10, 120 10, 100 50 
                   C 80 90, 20 90, 20 50" />
        </svg>

        <p>Docker DevOps App Running...</p>

        <div class="btn-container">
            <button class="btn aws" onclick="showAWS()">AWS</button>
            <button class="btn azure">AZURE</button>
            <button class="btn gcp">GCP</button>
        </div>

        <!-- 🔥 AWS Services -->
        <div id="aws-services" class="services">
            <div class="card">EC2</div>
            <div class="card">S3</div>
            <div class="card">Lambda</div>
            <div class="card">RDS</div>
            <div class="card">CloudFront</div>
        </div>

        <script>
            function showAWS() {
                let box = document.getElementById("aws-services");
                if (box.style.display === "none" || box.style.display === "") {
                    box.style.display = "block";
                } else {
                    box.style.display = "none";
                }
            }
        </script>

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
