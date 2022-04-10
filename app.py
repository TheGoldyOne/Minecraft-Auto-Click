import win32gui, win32api, win32con
from time import sleep
import keyboard

WINDOW_NAME = "Minecraft* 1.18.2 - Multiplayer (3rd-party Server)"
START_KEY = 'f10'
STOP_KEY = 'f12'
CLICK_DELAY = 1.2


def main():
    hWnd = win32gui.FindWindow(None, WINDOW_NAME)
    lParam = win32api.MAKELONG(100, 100)
    while True:
        if keyboard.is_pressed(STOP_KEY):
            break
        sleep(CLICK_DELAY)
        win32api.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

print(f"Press {START_KEY} to start. Hold {STOP_KEY} to stop.")
keyboard.wait(START_KEY)
main()

