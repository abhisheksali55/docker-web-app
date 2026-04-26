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
                font-size: 20px;
            }

            /* CHAT BOX */
            .chatbox {
                position: fixed;
                bottom: 80px;
                right: 20px;
                width: 300px;
                background: #111;
                border-radius: 15px;
                display: none;
                box-shadow: 0 0 15px rgba(0,255,200,0.5);
            }

            .chat-header {
                padding: 10px;
                background: #00ffcc;
                color: black;
                border-radius: 15px 15px 0 0;
            }

            .chat-body {
                height: 200px;
                overflow-y: auto;
                padding: 10px;
                text-align: left;
            }

            .chat-input {
                display: flex;
            }

            .chat-input input {
                flex: 1;
                padding: 10px;
                border: none;
                outline: none;
            }

            .chat-input button {
                padding: 10px;
                background: #00ffcc;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <div class="navbar">
            <div>☰ Menu</div>
            <div>⚙️ Settings | 🔐 Login</div>
        </div>

        <h2>DevOps App Running 🚀</h2>

        <!-- 🤖 AI BUTTON -->
        <div class="ai-btn" onclick="toggleChat()">🤖</div>

        <!-- 💬 CHATBOX -->
        <div id="chatbox" class="chatbox">
            <div class="chat-header">AI Assistant</div>
            <div id="chat-body" class="chat-body"></div>
            <div class="chat-input">
                <input id="msg" placeholder="Type message...">
                <button onclick="sendMsg()">Send</button>
            </div>
        </div>

        <script>
            function toggleChat() {
                let box = document.getElementById("chatbox");
                box.style.display = box.style.display === "block" ? "none" : "block";
            }

            function sendMsg() {
                let input = document.getElementById("msg");
                let chat = document.getElementById("chat-body");

                let userMsg = input.value;
                if(userMsg === "") return;

                chat.innerHTML += "<p><b>You:</b> " + userMsg + "</p>";

                // Simple AI reply
                let reply = "I am your DevOps AI 🤖";
                if(userMsg.toLowerCase().includes("aws")) reply = "AWS is cloud platform ☁️";
                if(userMsg.toLowerCase().includes("docker")) reply = "Docker is container tool 🐳";

                chat.innerHTML += "<p><b>AI:</b> " + reply + "</p>";

                input.value = "";
                chat.scrollTop = chat.scrollHeight;
            }
        </script>

    </body>
    </html>
    """)

app.run(host="0.0.0.0", port=5000)
