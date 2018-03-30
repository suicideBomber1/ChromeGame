import numpy as np
import cv2
from PIL import ImageGrab, Image
from mss import mss
import time
import os

# Below function taken from Sentedex YouTube Channel


def process_image(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=100, threshold2=300)
    return processed_image

#################################################


for i in reversed(range(4)):
    print(i + 1)
    time.sleep(1)

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
    cv2.imshow('test', new_screen)
    # cv2.imwrite('images/frame%d.jpg' % count, new_screen)
    cv2.imwrite(os.path.join(path, 'frame%d.jpg' % count), new_screen)
    time.sleep(0.3)
    count += 1
    start_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
