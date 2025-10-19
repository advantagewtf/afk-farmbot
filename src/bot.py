import time
import random
import pyautogui
import mouse
import pygetwindow
import cv2
import numpy as np
import pyautogui
import requests
import os
import colorama
import threading
import ctypes
import string

from util.extrafuncs import * 
from util.keyhandler import *
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
reset = colorama.Fore.RESET
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
jumpPercentage = 0  # Jump every X hits
hotbar_keybind = "q"
jumpKeybind = "space"



def set_console_title():
    while True:
        randomchar = "".join(random.choices(string.ascii_letters + string.digits, k=16))
        ctypes.windll.kernel32.SetConsoleTitleW(randomchar)
        time.sleep(0.01)


cstitle = threading.Thread(target=set_console_title)
cstitle.daemon = True  # Set the thread as a daemon thread
cstitle.start()



SpamMessages = [""]

os.system("cls")
print(logo)
print(f"{yellow}[INFO]{reset}: Wating 5 seconds tab to game!")
time.sleep(5)
os.system("cls")


s = 0
x = 0
y = 0
sell = 0
spamm = 0


def loop():
    global x, y, s, sell, spamm
    x += 1
    y += 1
    sell += 1
    s += 1

    if spam:
        if s == 5:
            key.openChat()
            time.sleep(0.3)
            key.write(random.choice(SpamMessages), True)
            key.openChat()
            spamm += 1
            s = 0
            debug(f"spammed {spamm} times")
    if not jumpPercentage == 0:
        if x == jumpPercentage:
            key.click(jumpKeybind)
            debug("jumped")
            x = 0
    if sellitem:
        if sell == sellOften:
            key.openChat()
            time.sleep(0.3)
            key.write(f"/{sellComand}")
            key.openChat()
            sell = 0
            debug("Sold")
    set_Hotbar(hotbar_keybind)
    mouse.click()
    time.sleep(hit_delay)
    debug("Hit")
    if eat_Food:
        if FoodFinder(foodPng):
            set_Hotbar(food_Hotkey)
            mouse.press("right")
            time.sleep(1.65)
            mouse.release("right")
    if advanced:
        advancedAFK()


while not key.WaitUntilPressed("q"):
    if hold:
        while key.WaitUntilPressed("f"):
            loop()
    else:
        loop()
