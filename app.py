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

            /* 🔥 Buttons Container */
            .btn-container {
                margin-top: 40px;
            }

            /* 🔥 Curved Buttons */
            .btn {
                padding: 12px 25px;
                margin: 10px;
                border: none;
                border-radius: 30px; /* curved look */
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
            <button class="btn aws">AWS</button>
            <button class="btn azure">AZURE</button>
            <button class="btn gcp">GCP</button>
        </div>

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
