import keyboard
import time
import mouse

def hold(key):
    keyboard.press(key)


def release(key):
    keyboard.release(key)


def openChat():
    keyboard.press_and_release("enter")


def Type(key):
    keyboard.press_and_release(key)


def write(Text,x=False):
    if not x:
        for char in Text:
            Type(char)
            time.sleep(0.15)
    else:
        for char in Text:
            Type(char)
            time.sleep(0.05)


def click(key):
    keyboard.press_and_release(key)


def WaitUntilPressed(key):
    return keyboard.is_pressed(key)
