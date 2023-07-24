from pyautogui import *
from keyboard import *
from threading import *
a = {
    "w": lambda: moveTo(position()[0], position()[1] - 10),
    "s": lambda: moveTo(position()[0], position()[1] + 10),
    "a": lambda: moveTo(position()[0] - 10, position()[1]),
    "d": lambda: moveTo(position()[0] + 10, position()[1]),
}
for k, i in a.items():
    add_hotkey(k, i)
on_press_key("q", lambda e: mouseDown(button="left"))
on_release_key("q", lambda e: mouseUp(button="left"))
on_press_key("e", lambda e: mouseDown(button="right"))
on_release_key("e", lambda e: mouseUp(button="right"))
wait()
