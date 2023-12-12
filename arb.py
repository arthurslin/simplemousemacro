import pyautogui
import random
import time
from pynput.mouse import Listener

# pyautogui.displayMousePosition()
# pyautogui.mouseInfo()

CLICKS = 8

points = []
selections = []

# Get function
while (True): 

    def is_clicked(x, y, button, pressed):

        if pressed:
            print("Click Received",x,y)
            if len(points) < 2:
                points.append((x,y))

            return False

    with Listener(on_click=is_clicked) as listener:
        listener.join()

    if len(points) == 2:
        selections.append(points)
        points = []

    if len(selections) == CLICKS:
        break


for i in range(230):
    ranpoint = (0,0)
    for i in selections:
        randx = random.randint(i[0][0],i[1][0])
        randy = random.randint(i[0][1],i[1][1])
        time.sleep(random.uniform(0.5,1))
        # print("Point:",i,"Index:",selections.index(i))
        if selections.index(i) == 6:
            time.sleep(9)
            pyautogui.click(randx, randy)
        pyautogui.click(randx, randy)

