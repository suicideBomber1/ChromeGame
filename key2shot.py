# Take a screenshot every time we press a certain key

from pynput.keyboard import Key, Listener
import numpy as np
import cv2
from PIL import ImageGrab, Image
from mss import mss
import time
import os

path = '/Users/Nagarjuna/Projects/ChromeGame/images'
monitor = {'top': 155, 'left': 3, 'width': 430, 'height': 120}
count1 = 0
count2 = 0

sct = mss()


def screen_grab(monitor):
    sct.get_pixels(monitor)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    new_screen = process_image(np.array(img))
    cv2.imshow('test', new_screen)
    return new_screen


def save_image(new_screen, name, count):
    name = name + str(count)
    print("Saving image: ", name)
    cv2.imwrite(path + name + ".png", new_screen)
    count += 1
    return count


def process_image(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=100, threshold2=300)
    return processed_image


# while(True):
#     screen_grab(monitor)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break


def on_press(key):
    global count1, count2, monitor, path
    new_screen = screen_grab(monitor)
    if key == Key.up:
        count1 = save_image(new_screen, 'jump', count1)

    if key == Key.right:
        count2 = save_image(new_screen, 'nojump', count2)


def on_release(key):
    if key == Key.Escape:
        print("Process has been interrupted by 'Esc' key")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# def listen():
#     listener = Listener(on_press=on_press, on_release=on_release)
#     listener.start()


# while True:
#     listen()

# def main():
#     while True:
#         listen()
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break


# if __name__ == '__main__':
#     main()


# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
