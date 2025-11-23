import extra.keyhandler as key
import cv2
import numpy as np
import pyautogui
import random
import colorama
import ctypes
from ctypes import wintypes
import time
import string
import fade

green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
reset = colorama.Fore.RESET
red = colorama.Fore.RED
blue = colorama.Fore.BLUE

ASCII = fade.purpleblue(
    R"""
             __  __    ____     ____    _   _   _        _____    _____   _    _   _______ 
            |  \/  |  / __ \   / __ \  | \ | | | |      |_   _|  / ____| | |  | | |__   __|
            | \  / | | |  | | | |  | | |  \| | | |        | |   | |  __  | |__| |    | |   
            | |\/| | | |  | | | |  | | | . ` | | |        | |   | | |_ | |  __  |    | |   
            | |  | | | |__| | | |__| | | |\  | | |____   _| |_  | |__| | | |  | |    | |   
            |_|  |_|  \____/   \____/  |_| \_| |______| |_____|  \_____| |_|  |_|    |_|   
                                                                                                                                                           
"""
)
logo = f"""
\t{ASCII}
{reset}
========================================     {red}Made By Ellii{reset}    ========================================

"""

# in the near future i'll probably write a whole libary for handling ctypes. its just nice to have tbh.

user32 = ctypes.WinDLL("user32", use_last_error=True)

user32.GetForegroundWindow.restype = wintypes.HWND
user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.GetWindowTextLengthW.restype = ctypes.c_int
user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetWindowTextW.restype = ctypes.c_int


def sleep(s):
    time.sleep(s)


def log(*args):
    print(f"{green}[info]{reset} ->  ", *args)

def error(*args):
    print(f"{red}[error]{reset} ->", *args)
    raise "error!"

def debug(dbg, *args):
    if not dbg:
        return
    print(f"{yellow}[debug]{reset} ->", *args)

def set_console_title():
    while True:
        randomchar = "minecraft afk | ".join(
            random.choices(string.ascii_letters + string.digits, k=32)
        )
        ctypes.windll.kernel32.SetConsoleTitleA(randomchar)
        sleep(1)

def is_in_minecraft_window():
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        return False

    length = user32.GetWindowTextLengthW(hwnd)
    if length == 0:
        return False

    buffer = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buffer, length + 1)
    window_title = buffer.value.lower()

    return "minecraft" in window_title


def find_food(template_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        error("template image not found!")
        return
    
    screen_width, screen_height = pyautogui.size()
    screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # unused: min_val, min_loc

    threshold = 0.96
    if max_val >= threshold:
        debug(f"found hunger img at: {max_loc}")
        return True
    else:
        return False


def set_hotbar(slot_keybind):
    try:
        key.click(slot_keybind)
    except:
        debug("hotbar keybind is invalid please set it to a valid key")
    # todo: maybe have images and then switch to numbered slots?