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
                background: #111;
                color: white;
                text-align: center;
                margin-top: 50px;
            }

            svg {
                width: 300px;
                height: 300px;
            }

            .path {
                fill: none;
                stroke: #444;
                stroke-width: 6;
            }

            .snake {
                fill: none;
                stroke: #00ffcc;
                stroke-width: 6;
                stroke-linecap: round;
                stroke-dasharray: 80;
                stroke-dashoffset: 0;
                animation: move 2s linear infinite;
            }

            @keyframes move {
                0% { stroke-dashoffset: 0; }
                100% { stroke-dashoffset: 300; }
            }
        </style>
    </head>
    <body>

        <h2>Hello dosto welcome to DevOps batch 🚀</h2>

        <svg viewBox="0 0 200 200">
            <!-- Infinity shape -->
            <path class="path"
                d="M50,100 
                   C50,50 150,50 150,100 
                   C150,150 50,150 50,100" />

            <!-- Snake moving -->
            <path class="snake"
                d="M50,100 
                   C50,50 150,50 150,100 
                   C150,150 50,150 50,100" />
        </svg>

        <p>Docker DevOps App Running...</p>

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
