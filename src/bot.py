import time
import random
import mouse
import os
import threading
import ctypes
import string

from config import *
from keyhandler import *
from utils import *


def set_console_title():
    while True:
        randomchar = "".join(random.choices(string.ascii_letters + string.digits, k=16))
        ctypes.windll.kernel32.SetConsoleTitleW(randomchar)
        time.sleep(0.01)


cstitle = threading.Thread(target=set_console_title)
cstitle.daemon = True  # Set the thread as a daemon thread
cstitle.start()


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
    random.seed(str(time.time()) + str(random.random()) + str(os.urandom(16)))
    # completely randomized seed every loop to ensure max randomness

    global x, y, s, sell, spamm
    x += 1
    y += 1
    sell += 1
    s += 1
    
    if eat_Food:
        if FoodFinder(foodPng):
            set_Hotbar(food_Hotkey)
            mouse.press("right")
            time.sleep(1.65)
            mouse.release("right")
            debug("Ate Food")
    
    if advanced:
        advancedAFK()
        debug("Advanced AFK")
        
    if spam:
        if s == spamCycles:
            key.openChat()
            time.sleep(0.3)
            key.write(random.choice(spamMessages), True)
            key.openChat()
            spamm += 1
            s = 0
            debug(f"Spammed Messages: {spamm} times")

    if not jumpCycles == 0:
        if x == jumpCycles:
            key.click(jumpKeybind)
            debug("Jumped")
            x = 0

    if sellitem:
        if sell == sellCycles:
            key.openChat()
            time.sleep(0.3)
            key.write(f"/{sellComand}")
            key.openChat()
            sell = 0
            debug("Sold")

    set_Hotbar(hotbar_keybind)

    mouse.click()

    debug("Hit")
    
    if not legit:
        time.sleep(hit_delay)
    else:
        delay = hit_delay + random.uniform(0.1, 0.3)
        debug ("legit wait: ", delay)
        time.sleep(delay)
        time.sleep(random.uniform(0.05, 0.2))


while not key.WaitUntilPressed("q"):
    if hold:
        while key.WaitUntilPressed(holdKey):
            loop()
    else:
        loop()
