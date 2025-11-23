import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL("user32", use_last_error=True)

# constants
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

MAPVK_VK_TO_VSC = 0

# all the mouse flags i think you'll need tbh
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040


# ctypes structs. this is really stupid. god i hate ctypes 😭
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG)),
    ]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG)),
    ]


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    ]


class _INPUTunion(ctypes.Union):
    _fields_ = [("mi", MOUSEINPUT), ("ki", KEYBDINPUT), ("hi", HARDWAREINPUT)]


class INPUT(ctypes.Structure):
    _fields_ = [("type", wintypes.DWORD), ("union", _INPUTunion)]


LPINPUT = ctypes.POINTER(INPUT)

user32.SendInput.argtypes = (wintypes.UINT, LPINPUT, ctypes.c_int)
user32.SendInput.restype = wintypes.UINT


def key_down(vk: int):
    sc = user32.MapVirtualKeyW(vk, MAPVK_VK_TO_VSC)

    inp = INPUT(  # ignore this absolute aids of a structure ;-;
        type=INPUT_KEYBOARD,
        union=_INPUTunion(
            ki=KEYBDINPUT(wVk=vk, wScan=sc, dwFlags=0, time=0, dwExtraInfo=None)
        ),
    )
    user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def key_up(vk: int):
    sc = user32.MapVirtualKeyW(vk, MAPVK_VK_TO_VSC)

    inp = INPUT(  # ignore this absolute aids of a structure ;-;
        type=INPUT_KEYBOARD,
        union=_INPUTunion(
            ki=KEYBDINPUT(
                wVk=vk, wScan=sc, dwFlags=KEYEVENTF_KEYUP, time=0, dwExtraInfo=None
            )
        ),
    )
    user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def key_press(vk: int, delay: float = 0.01):

    key_down(vk)
    time.sleep(delay)
    key_up(vk)


def send_text(text: str):
    for char in text:
        inp = INPUT(  # ignore this absolute aids of a structure ;-;
            type=INPUT_KEYBOARD,
            union=_INPUTunion(
                ki=KEYBDINPUT(
                    wVk=0,
                    wScan=ord(char),
                    dwFlags=KEYEVENTF_UNICODE,
                    time=0,
                    dwExtraInfo=None,
                )
            ),
        )

        user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

        # KeyUp
        inp2 = INPUT( # ignore this absolute aids of a structure ;-;
            type=INPUT_KEYBOARD,
            union=_INPUTunion(
                ki=KEYBDINPUT(
                    wVk=0,
                    wScan=ord(char),
                    dwFlags=KEYEVENTF_UNICODE | KEYEVENTF_KEYUP,
                    time=0,
                    dwExtraInfo=None,
                )
            ),
        )

        user32.SendInput(1, ctypes.byref(inp2), ctypes.sizeof(INPUT))


def mouse_move(dx: int, dy: int):
    inp = INPUT( # ignore this absolute aids of a structure ;-;
        type=INPUT_MOUSE,
        union=_INPUTunion( 
            mi=MOUSEINPUT(
                dx=dx,
                dy=dy,
                mouseData=0,
                dwFlags=MOUSEEVENTF_MOVE,
                time=0,
                dwExtraInfo=None,
            )
        ),
    )

    user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def mouse_click(left=True, delay=0.01):
    down_flag = MOUSEEVENTF_LEFTDOWN if left else MOUSEEVENTF_RIGHTDOWN
    up_flag = MOUSEEVENTF_LEFTUP if left else MOUSEEVENTF_RIGHTUP

    inp_down = INPUT(
        type=INPUT_MOUSE, union=_INPUTunion(mi=MOUSEINPUT(0, 0, 0, down_flag, 0, None))
    )
    inp_up = INPUT(
        type=INPUT_MOUSE, union=_INPUTunion(mi=MOUSEINPUT(0, 0, 0, up_flag, 0, None))
    )

    user32.SendInput(1, ctypes.byref(inp_down), ctypes.sizeof(INPUT))
    time.sleep(delay)
    user32.SendInput(1, ctypes.byref(inp_up), ctypes.sizeof(INPUT))
    # this is nice because its not detected by lunar since its a python window sending it 💔💔💔


def is_key_down(vk: int) -> bool:
    return bool(user32.GetAsyncKeyState(vk) & 0x8000)


# def is_key_toggled(vk: int) -> bool:
#     return bool(user32.GetKeyState(vk) & 1)
