# AI-Powered-Bruteforce-Tool
A Python-based brute-force attack simulation tool that integrates AI-driven password generation using a Markov model. It features a simple GUI built with Tkinter and supports brute-force attempts over FTP, SSH, and HTTP login forms — all executed in parallel using multithreading.
🚀 Features:-
🎯 Supports FTP, SSH, and HTTP brute-force attacks.
🧠 AI-powered password guessing using a trained Markov Chain model.
💻 Built with Python 3 and a beginner-friendly GUI (Tkinter).
🔁 Uses multithreading for faster, parallel execution.
📜 Real-time output logs in a scrollable text window.
📦 Lightweight and portable — no database or heavy framework required.

🧠 How AI is Used:-
Trained on common password datasets (like rockyou.txt).
Uses 2-character state transitions to predict next characters.
Generates smart password guesses that mimic real user behavior.

🛠️ Requirements:-
Python 3.8+
Libraries:
pip install paramiko requests

▶️ How to Run:-
Clone the repo:
git clone https://github.com/yourusername/ai-bruteforce-tool.git
cd ai-bruteforce-tool

Train your AI model (optional):
python3 train_model.py

Run the GUI tool:
python3 bruteforce_tool.py

📘 Ethical Usage
This tool is intended solely for educational use, research, and ethical penetration testing. Do not use this tool to attack any system without written authorization. Unauthorized use of brute-force tools may be illegal in your country or violate your organization’s policies.



