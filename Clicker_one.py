import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0,  0)

counter = 0

try:
    while counter < 25000:  # change this to ' while true: ' for infinite clicks
        click(230, 475)  # click(x, y) edit this to change position of click.

        if win32api.GetAsyncKeyState(ord('X')):   # press the x key to stop the script
            break
        counter += 1  # you can comment/ remove this if you set the while loop to true.
        print(counter)  # remove if you don't want to see the amount of loops
except KeyboardInterrupt:
    pass
