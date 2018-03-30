import numpy as np
import cv2
from PIL import ImageGrab, Image
from mss import mss
import time
import os

# image = pyautogui.screenshot()
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# cv2.imwrite("images/test_image.png", image)


def process_image(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=100, threshold2=300)
    return processed_image


# while(True):
#     screen = np.array(ImageGrab.grab(bbox=(3, 150, 435, 277)))
#     new_screen = process_image(screen)
#     print("Loop took {} seconds".format(time.time() - start_time))
#     start_time = time.time()
#     cv2.imshow('window', new_screen)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break

path = '/Users/Nagarjuna/Projects/ChromeGame/images'

monitor = {'top': 155, 'left': 3, 'width': 430, 'height': 120}
count = 0

sct = mss()

start_time = time.time()
while(True):
    sct.get_pixels(monitor)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    new_screen = process_image(np.array(img))
    print("Loop took {} seconds".format(time.time() - start_time))
    start_time = time.time()
    cv2.imshow('test', new_screen)
    # cv2.imwrite('images/frame%d.jpg' % count, new_screen)
    cv2.imwrite(os.path.join(path, 'frame%d.jpg' % count), new_screen)
    count += 1
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
