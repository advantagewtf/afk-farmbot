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
from extrafuncs import *

green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
reset = colorama.Fore.RESET
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
jumpPercentage = 0  # Jump every X hits
hotbar_keybind = "r"
jumpKeybind = " "

hit_delay = 0.63  # 0.63 is exact time but a lil delay in case of fps or lag error
enable_Debug = True
eat_Food = False
food_Hotkey = "7"
foodPng = "full.png"
advanced = False
sellitem = False
sellComand = "sellall inventory"  # no /
sellOften = 100  # every 100 cycles
spam = False
hold = True
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


SpamMessages = [
   
]


while not keyauth(input("Enter Key:")):
    pass
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
            debug(f"Spammed {spamm} times")
    if not jumpPercentage == 0:
        if x == jumpPercentage:
            key.click(jumpKeybind)
            debug("Jumped")
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
