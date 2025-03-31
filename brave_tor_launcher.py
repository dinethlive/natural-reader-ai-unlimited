import pyautogui
import subprocess
import time
import tkinter as tk
import os
import platform

# === CONFIGURATION ===
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
TARGET_URL = "https://www.naturalreaders.com/online/"

# === FUNCTIONS ===

def launch_and_automate():
    subprocess.Popen([BRAVE_PATH])
    time.sleep(5)
    pyautogui.hotkey('alt', 'shift', 'n')
    time.sleep(5)
    pyautogui.hotkey('alt', 'd')
    time.sleep(0.5)
    pyautogui.typewrite(TARGET_URL, interval=0.05)
    pyautogui.press('enter')

def close_brave():
    system = platform.system()
    try:
        if system == "Windows":
            os.system('taskkill /f /im brave.exe')
        elif system == "Darwin":  # macOS
            os.system('pkill -f "Brave Browser"')
        elif system == "Linux":
            os.system('pkill brave')
    except Exception as e:
        print(f"Error closing Brave: {e}")

# === GUI SETUP ===
root = tk.Tk()
root.title("Auto-Tor Brave Launcher")
root.geometry("300x160")
root.resizable(False, False)

label = tk.Label(root, text="Launch Natural Readers via Tor", font=("Arial", 12))
label.pack(pady=10)

btn_launch = tk.Button(root, text="Launch via Tor", command=launch_and_automate, bg="green", fg="white", width=25)
btn_launch.pack(pady=5)

btn_close = tk.Button(root, text="Close Brave Windows", command=close_brave, bg="red", fg="white", width=25)
btn_close.pack(pady=5)

note = tk.Label(root, text="* Keep screen focused during automation", font=("Arial", 8))
note.pack(pady=10)

root.mainloop()
