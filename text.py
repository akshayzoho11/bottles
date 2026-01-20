import subprocess
import sys
import time
import os
import pyautogui

# --- CONFIG ---
if "DISPLAY" not in os.environ:
    print("Warning: DISPLAY environment variable not found. Automation might fail.")
    os.environ["DISPLAY"] = ":99"

BOTTLE_NAME = "MQL5Bottle"
WAIT_TIME = 30
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

time.sleep(2)

def take_screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, name)
    try:
        pyautogui.screenshot(path)
        print(f"Screenshot saved: {path}")
    except Exception as e:
        print(f"Error taking screenshot {name}: {e}")

# --- TEST SCREENSHOT ---
take_screenshot("01_after_install.png")

# --- LAUNCH INSTALLER ---
second_path = os.path.join(os.getcwd(), "install-3.exe")
print(f"Launching installer from: {second_path}")

if not os.path.exists(second_path):
    print(f"ERROR: {second_path} not found!")
    sys.exit(1)

# Try Bottles first, fallback to Wine
use_bottles = False
try:
    # Check if Bottles is available
    result = subprocess.run(['flatpak', 'list', '--app'], capture_output=True, text=True)
    if 'com.usebottles.bottles' in result.stdout:
        print("Bottles found, attempting to use it...")
        subprocess.Popen([
            'flatpak', 'run', 'com.usebottles.bottles',
            '-b', BOTTLE_NAME,
            '-e', second_path
        ])
        print(f"Installer launched via Bottles (bottle: {BOTTLE_NAME}).")
        use_bottles = True
    else:
        raise FileNotFoundError("Bottles not installed")
except (FileNotFoundError, subprocess.CalledProcessError) as e:
    print(f"Bottles not available ({e}), falling back to Wine...")
    try:
        subprocess.Popen(['wine', second_path])
        print("Installer launched via Wine.")
        print("Installer launched via Wine.")
    except FileNotFoundError:
        print("ERROR: Neither Bottles nor Wine found!")
        sys.exit(1)

time.sleep(30)
take_screenshot("10_after_launching_installer.png")

# --- AUTOMATION SEQUENCE ---
print("Starting automation sequence...")

pyautogui.press('tab')
time.sleep(10)
take_screenshot("first_tab.png")

pyautogui.press('up')
time.sleep(10)
take_screenshot("first_up.png")

pyautogui.press('space')
time.sleep(10)
take_screenshot("first_space.png")

pyautogui.press('enter')
time.sleep(10)
take_screenshot("first_enter.png")

pyautogui.press('enter')
time.sleep(10)
take_screenshot("11a_after_finishing_second.png")

pyautogui.press('tab')
time.sleep(10)
take_screenshot("second_tab.png")

pyautogui.press('tab')
time.sleep(10)
take_screenshot("third_tab.png")

pyautogui.press('tab')
time.sleep(10)
pyautogui.press('tab')
time.sleep(10)
take_screenshot("fourth_tab.png")

pyautogui.press('enter')
time.sleep(10)
take_screenshot("second_enter.png")

pyautogui.press('tab')
time.sleep(1)
take_screenshot("3.tab1.png")

pyautogui.press('space')
time.sleep(1)
take_screenshot("3.space1.png")

time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
take_screenshot("3.tab2.png")

pyautogui.press('enter')
time.sleep(30)
take_screenshot("3.enter1.png")

pyautogui.press('tab')
time.sleep(1)
take_screenshot("4.tab1.png")

pyautogui.press('right')
time.sleep(1)
take_screenshot("4.right1.png")

pyautogui.press('right')
time.sleep(1)
take_screenshot("4.right2.png")

pyautogui.press('right')
time.sleep(1)
take_screenshot("4.right3.png")

print("Automation completed successfully!")
