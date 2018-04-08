from pynput.keyboard import Key, Listener

# defining function to print when key is pressed
# I dont know why its not working on mac


def on_press(key):
    print('{0} pressed'.format(key))
# defining function to print when key is released


def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press, on_release=on_release) as listener:
    listener.join()
