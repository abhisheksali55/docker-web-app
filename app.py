from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps App</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
                background-color: #111;
                color: white;
            }

            .loader {
                margin: 40px auto;
                width: 80px;
                height: 80px;
                border: 8px solid #444;
                border-top: 8px solid #00ffcc;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>

        <h2>Hello dosto welcome to the DevOps batch! 🚀</h2>

        <div class="loader"></div>

        <p>Docker DevOps App Running...</p>

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
