from pynput import keyboard

keys = [keyboard.Key.left, keyboard.Key.down, keyboard.Key.right, 'a', 's']

def on_press(key):
    mod = key % len(keys)
    keyboard.Controller().press(keys[mod])

def on_release(key):
    mod = key % len(keys)
    keyboard.Controller().release(keys[mod])