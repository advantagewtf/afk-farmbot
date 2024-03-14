import time
import random
import pyautogui
import keyboard.mouse as mouse
import pygetwindow
import cv2
import numpy as np
import pyautogui
import requests
import keyhandler as key
import os
import colorama

green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
reset = colorama.Fore.RESET
red = colorama.Fore.RED
blue = colorama.Fore.BLUE

logo = f"""
    {blue}
           ______ _  __           ____   ____ _______ 
     /\   |  ____| |/ /          |  _ \ / __ \__   __|
    /  \  | |__  | ' /           | |_) | |  | | | |   
   / /\ \ |  __| |  <            |  _ <| |  | | | |   
  / ____ \| |    | . \           | |_) | |__| | | |   
 /_/    \_\_|    |_|\_\          |____/ \____/  |_|   
                                                      
==============     {red}Made By Drexxy{blue}    =====================

"""


def debug(text):
    global enable_Debug
    if enable_Debug:
        os.system("cls")
        print(logo)
        print(f"{yellow}[debug]{reset}{text}")


def advancedAFK():
    keys = random.choice(["a", "d"])
    delay = random.randint(1, 5) / 100
    key.hold(keys)
    time.sleep(delay)
    key.release(keys)
    if keys == "a":
        key.hold("d")
        time.sleep(delay)
        key.release("d")
    elif keys == "d":
        key.hold("a")
        time.sleep(delay)
        key.release("a")


def FoodFinder(template_path):
    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"{red}[Error]{reset}: Template image not found.")
        return

    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Capture the screen
    screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Match the template
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Threshold for matching result
    threshold = 0.96

    if max_val >= threshold:
        debug(f"hunger at: {max_loc}")
        return True
    else:
        debug("Full not eating now")
        return False


def keyauth(key):
    data = {"key": key}
    response = requests.post(url="http://localhost:5000/check_key", json=data)
    if response.status_code == 200:
        response_data = response.json()
    # Check if the response indicates 'true' or 'false'
    if "valid" in response_data:
        if response_data["valid"]:
            debug(f"{green}[VALID]{reset} The key is valid.")
            return True
        else:
            debug(f"{red}The key is not valid.")
            return False


def set_Hotbar(slot_keybind):
    try:
        key.click(slot_keybind)

    except:
        debug("hotbar keybind is invalid please reset it")
