import random
import mouse
import os
import threading

from extra.config import config
from extra.keyhandler import *
from extra.utils import *

hotbar_keybind = config["sword_keybind"]
jump_keybind = config["jump_keybind"]
legit_mode = config["legit_delays"]
hit_delay = config["hit_delay"]
enable_debug = config["enable_debug"]
eat_food = config["eat_food"]
food_hotkey = config["food_hotkey"]
food_png = config["food_png"]
sell_items = config["sell_items"]
sell_command = config["sell_command"]
sell_cycles = config["sell_cycles"]
spam = config["spam_chat"]
spam_messages = config["spam_messages"]
spam_cycles = config["spam_cycles"]
hold = config["hold"]
hold_key = config["hold_key"]
jump_cycles = config["jump_cycles"]


def clear():
    os.system("cls")
    print(logo)


cstitle = threading.Thread(target=set_console_title)
cstitle.daemon = True
# https://duckduckgo.com/q=daemon+meaning&ia=web (yes i had to look this up 😭😭😭)
cstitle.start()

clear()

print(f"{yellow}[info]{reset} -> Waiting 5 seconds, tab to game!")
sleep(5)


_spam_cycles = 0
_jump_cycles = 0
_sell_cycles = 0
spam_times = 0


def loop():
    global _jump_cycles, y, _spam_cycles, _sell_cycles, spam_times
    _jump_cycles += 1
    _sell_cycles += 1
    _spam_cycles += 1

    if not is_in_minecraft_window():
        debug(enable_debug, "not tabbed into game waiting 1 second...")
        sleep(1)
        return

    if spam and _spam_cycles >= spam_cycles:
        key.openChat()
        sleep(0.3)
        key.write(random.choice(spam_messages), True)
        key.openChat()
        spam_times += 1
        _spam_cycles = 0
        debug(enable_debug, f"Spammed Messages: {spam_times} times")

    if jump_cycles != 0 and _jump_cycles >= jump_cycles:
        key.click(jump_keybind)
        debug(enable_debug, "Jumped", enable_debug)
        _jump_cycles = 0

    if sell_items and _sell_cycles >= sell_cycles:
        key.openChat()
        sleep(0.3)
        key.write(f"/{sell_command}")
        key.openChat()
        _sell_cycles = 0
        debug(enable_debug, "Sold")

    set_hotbar(hotbar_keybind)
    mouse.click()
    debug(enable_debug, "Hit")
    if not legit_mode:
        sleep(hit_delay)
    else:
        sleep(hit_delay + random.uniform(0.1, 0.3))

    if eat_food and find_food(food_png):
        set_hotbar(food_hotkey)
        mouse.press("right")
        sleep(1.65 + random.uniform(0.1, 0.3))  # randomize eating time
        mouse.release("right")
        debug(enable_debug, "Ate Food")


if (
    legit_mode
):  # randomize completely if you're using legit mode. helps with legit delays
    random.seed(str(time.time()) + str(random.random()) + str(os.urandom(16)))

# main loop here <3
while not key.is_pressed("q"):
    if hold:
        while key.is_pressed(hold_key):
            loop()
    else:
        loop()
