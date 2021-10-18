from pynput.keyboard import Key, Listener
import time

def on_press(key):
    try:
        if key == key.f14:
            print('{0} pressed'.format(key))
            time.sleep(5)
            return False
    except AttributeError:
        pass

def on_release(key):
    print('{0} release'.format(key))
    #if key == Key.esc:
        # Stop listener
    return False

# Collect events until released
while(True):
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print('Next')