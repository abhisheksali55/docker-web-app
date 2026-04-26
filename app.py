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
                margin-top: 80px;
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
        </style>
    </head>
    <body>

        <h2>Hello dosto welcome to DevOps batch 🚀</h2>

        <svg viewBox="0 0 200 100">
            <!-- REAL infinity shape -->
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

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
