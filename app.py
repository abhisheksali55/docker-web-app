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

            .aws { background: linear-gradient(45deg, #ff9900, #ff6600); }
            .azure { background: linear-gradient(45deg, #007fff, #00c6ff); }
            .gcp { background: linear-gradient(45deg, #ea4335, #34a853); }

            .btn:hover {
                transform: scale(1.1);
                box-shadow: 0 0 15px rgba(255,255,255,0.3);
            }

            /* 🔥 Services Section */
            .services {
                display: none;
                margin-top: 20px;
            }

            .card {
                background: #111;
                padding: 12px 20px;
                margin: 10px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0 0 10px rgba(0,255,200,0.2);
                transition: 0.3s;
            }

            .card:hover {
                transform: scale(1.1);
                box-shadow: 0 0 20px rgba(0,255,200,0.5);
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

        <!-- 🔥 Buttons -->
        <div class="btn-container">
            <button class="btn aws" onclick="showSection('aws')">AWS</button>
            <button class="btn azure" onclick="showSection('azure')">AZURE</button>
            <button class="btn gcp" onclick="showSection('gcp')">GCP</button>
        </div>

        <!-- 🔥 AWS -->
        <div id="aws" class="services">
            <div class="card">EC2 - Virtual Server</div>
            <div class="card">S3 - Storage</div>
            <div class="card">Lambda - Serverless</div>
            <div class="card">RDS - Database</div>
            <div class="card">CloudFront - CDN</div>
        </div>

        <!-- 🔥 AZURE -->
        <div id="azure" class="services">
            <div class="card">VM - Virtual Machine</div>
            <div class="card">Blob Storage</div>
            <div class="card">Azure Functions</div>
            <div class="card">SQL Database</div>
            <div class="card">App Service</div>
        </div>

        <!-- 🔥 GCP -->
        <div id="gcp" class="services">
            <div class="card">Compute Engine</div>
            <div class="card">Cloud Storage</div>
            <div class="card">Cloud Functions</div>
            <div class="card">BigQuery</div>
            <div class="card">App Engine</div>
        </div>

        <script>
            function showSection(id) {
                // sab hide karo
                document.getElementById("aws").style.display = "none";
                document.getElementById("azure").style.display = "none";
                document.getElementById("gcp").style.display = "none";

                // selected show karo
                document.getElementById(id).style.display = "block";
            }
        </script>

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
