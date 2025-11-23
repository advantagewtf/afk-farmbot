import keyboard
import time
import mouse
import extra.lib as keylib

# vk keycode map -> very necessary if you want to not get aids while reading code <3

VK_CODES = {
    "A": 0x41, "B": 0x42, "C": 0x43, "D": 0x44, "E": 0x45,
    "F": 0x46, "G": 0x47, "H": 0x48, "I": 0x49, "J": 0x4A,
    "K": 0x4B, "L": 0x4C, "M": 0x4D, "N": 0x4E, "O": 0x4F,
    "P": 0x50, "Q": 0x51, "R": 0x52, "S": 0x53, "T": 0x54,
    "U": 0x55, "V": 0x56, "W": 0x57, "X": 0x58, "Y": 0x59,
    "Z": 0x5A,
    "0": 0x30, "1": 0x31, "2": 0x32, "3": 0x33, "4": 0x34,
    "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39,
    "F1": 0x70, "F2": 0x71, "F3": 0x72, "F4": 0x73, "F5": 0x74,
    "F6": 0x75, "F7": 0x76, "F8": 0x77, "F9": 0x78, "F10": 0x79,
    "F11": 0x7A, "F12": 0x7B,
    "ESC": 0x1B, "TAB": 0x09, "CAPSLOCK": 0x14, "SHIFT": 0x10,
    "CTRL": 0x11, "ALT": 0x12, "SPACE": 0x20, " ": 0x20, "ENTER": 0x0D,
    "BACKSPACE": 0x08, "DELETE": 0x2E, "INSERT": 0x2D, "HOME": 0x24,
    "END": 0x23, "PAGEUP": 0x21, "PAGEDOWN": 0x22,
    "UP": 0x26, "DOWN": 0x28, "LEFT": 0x25, "RIGHT": 0x27,
    "NUM0": 0x60, "NUM1": 0x61, "NUM2": 0x62, "NUM3": 0x63,
    "NUM4": 0x64, "NUM5": 0x65, "NUM6": 0x66, "NUM7": 0x67,
    "NUM8": 0x68, "NUM9": 0x69, "NUMLOCK": 0x90, "NUMENTER": 0x0D,
    "NUMPLUS": 0x6B, "NUMMINUS": 0x6D, "NUMMULT": 0x6A, "NUMDIV": 0x6F,
    "PRINTSCREEN": 0x2C, "SCROLLLOCK": 0x91, "PAUSE": 0x13,
    "WIN": 0x5B, "ALT": 0x5D,
    "-": 0xBD, "=": 0xBB, "[": 0xDB, "]": 0xDD,
    "\\": 0xDC, ";": 0xBA, "'": 0xDE,
    ",": 0xBC, ".": 0xBE, "/": 0xBF, "`": 0xC0
}

def key_to_code(key: str):
    return VK_CODES[key.upper()]

def press_key(key):
    if type(key) == int:
        keylib.key_press(key)
    elif type(key) == str:
        keylib.key_press(key_to_code(key))
        
def openChat():
    keylib.key_press(key_to_code("t"))
    # keyboard.press_and_release("/")


def write(Text,x=False):
    if not x:
        for char in Text:
            keylib.key_press(key_to_code(char))
            time.sleep(0.15)
    else:
        for char in Text:
            keylib.key_press(key_to_code(char))
            time.sleep(0.05)


def is_pressed(key):
    if type(key) == int:
        keylib.is_key_down(key)
    elif type(key) == str:
        keylib.is_key_down(key_to_code(key))
        
    # return keybord.is_pressed(key)
