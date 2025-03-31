import pyautogui
import subprocess
import time
import tkinter as tk
import os
import platform

# === CONFIGURATION ===
# Path to the Brave browser executable
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# The URL to open in Tor window
TARGET_URL = "https://www.naturalreaders.com/online/"

# === FUNCTIONS ===

def launch_and_automate():
    """
    Launch Brave, open a new Tor window, navigate to the target URL.
    Requires screen to stay focused during automation.
    """
    subprocess.Popen([BRAVE_PATH])  # Start Brave
    time.sleep(5)  # Wait for it to load

    # Open new Tor window with Alt + Shift + N
    pyautogui.hotkey('alt', 'shift', 'n')
    time.sleep(5)  # Wait for Tor window to load

    # Focus address bar and type URL
    pyautogui.hotkey('alt', 'd')
    time.sleep(0.5)
    pyautogui.typewrite(TARGET_URL, interval=0.05)
    pyautogui.press('enter')

def close_brave():
    """
    Kill all Brave browser windows.
    Cross-platform support: Windows, macOS, Linux.
    """
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

# Initialize main window
root = tk.Tk()
root.title("Auto-Tor Brave Launcher")
root.geometry("300x160")
root.resizable(False, False)

# App title
label = tk.Label(root, text="Launch Natural Readers via Tor", font=("Arial", 12))
label.pack(pady=10)

# Button to launch Brave and automate
btn_launch = tk.Button(
    root,
    text="Launch via Tor",
    command=launch_and_automate,
    bg="green",
    fg="white",
    width=25
)
btn_launch.pack(pady=5)

# Button to close all Brave windows
btn_close = tk.Button(
    root,
    text="Close Brave Windows",
    command=close_brave,
    bg="red",
    fg="white",
    width=25
)
btn_close.pack(pady=5)

# Helper note
note = tk.Label(
    root,
    text="* Keep screen focused during automation",
    font=("Arial", 8)
)
note.pack(pady=10)

# Start GUI event loop
root.mainloop()
