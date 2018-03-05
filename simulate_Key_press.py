# to simulate you have to install the (  pip install pynput )
from pynput.keyboard import Key, Controller
import time

keyboad=Controller()
time.sleep(2)

keyboad.press('a')

keyboad.release('a')

