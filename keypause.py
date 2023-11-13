#! python3
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

keycon = Controller()
playing = True
lastKeyPress = time.time()
ignoreList = [Key.media_play_pause, Key.media_volume_up, Key.media_volume_down]

def on_press(key):
    global playing, lastKeyPress, keycon, Key
    if key in ignoreList:
        return
    lastKeyPress = time.time()
    if playing:
        playing = False
        keycon.press(Key.media_play_pause)
        keycon.release(Key.media_play_pause)

def on_release(key):
    pass

def createAndStartListener():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    return listener

listener = createAndStartListener()

DELAY = 1
while True:
    time.sleep(0.1)
    if time.time() - lastKeyPress > DELAY and not playing:
        listener.stop()
        keycon.press(Key.media_play_pause)
        keycon.release(Key.media_play_pause)
        playing = True
        listener = createAndStartListener()