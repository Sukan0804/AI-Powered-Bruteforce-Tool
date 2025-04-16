🧠 AI-Powered Brute-Force Attack Tool
A Python-based brute-force attack simulation tool designed for ethical hacking education and research. This tool uses a Markov Chain AI model to generate intelligent password guesses and attempts logins over FTP, SSH, and HTTP protocols — all through a simple and user-friendly GUI.

🔒 Disclaimer: This project is for educational use only. Never use this tool on systems you don’t own or have explicit permission to test.

📌 Features
🧠 AI-based Password Generation using a Markov model.

⚡ Multithreaded Brute-Force Engine supporting:

FTP (via ftplib)

SSH (via paramiko)

HTTP form-based login (via requests)

🖥️ Tkinter GUI for inputs and real-time result display.

🗃️ Modular and Lightweight – easy to customize and expand.

🛠️ Installation
Clone the Repository
git clone https://github.com/Sukan0804/AI-Powered-Bruteforce-Tool.git
cd ai-bruteforce-tool

Install Dependencies:
pip install paramiko requests

Train your own Markov model:
python3 train_model.py

Run the Tool:
python3 bruteforce_tool.py

🧪 How It Works
You input a Target IP, Username, and optionally a login URL.

The tool uses a pre-trained Markov model to generate smart password guesses.

It launches parallel brute-force attacks on FTP, SSH, and HTTP services.

The GUI displays real-time logs of all attempts.


⚖️ Ethical Use
This tool is strictly intended for:

Educational demonstrations

Penetration testing on authorized systems

Academic projects and CTF environments

Unauthorized use may be illegal. Use responsibly. 🚨
