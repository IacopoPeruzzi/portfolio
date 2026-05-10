import subprocess
import os
import time

def start_server():
    web_app_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app"
    
    print("Starting Vite development server...")
    # Usiamo subprocess.Popen per far girare il server in background
    process = subprocess.Popen(
        "npm run dev",
        shell=True,
        cwd=web_app_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Attendiamo che il server sia pronto (di solito 1-2 secondi)
    time.sleep(2)
    print("Server initialized.")
    return process

if __name__ == "__main__":
    start_server()
