# from pynput import keyboard
# from pynput.keyboard import Key


# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))


from pynput.keyboard import Key, Listener

# defining function to print when key is pressed


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


# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False


# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# char = input("Enter a value: ")
# # print(keyboard.KeyCode().from_char(char))
# print(keyboard.Key(char))


# def on_press(key):
#     try:
#         print("{0} released".format(keyboard.KeyCode().from_char(key)))
#     except:
#         print("{0} released".format(keyboard.Key(key)))


# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

# while True:
#     char = input("Enter a value: ")
#     on_press(char)

# controller = keyboard.Controller()


# def on_press(key):
#     if key == keyboard.Key.up:
#         print("Upward arrow released")


# with keyboard.Listener(on_press=on_press) as listener:
    # listener.join()
