import subprocess
import tkinter as tk
from app import App
import time

def main():
    api_process = subprocess.Popen(["python", "api.py"])

    time.sleep(2)

    root = tk.Tk()
    app = App(root)
    app.root.mainloop()

if __name__ == "__main__":
    main()
