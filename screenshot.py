import numpy as np
import cv2
from PIL import ImageGrab
import time

# image = pyautogui.screenshot()
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# cv2.imwrite("images/test_image.png", image)


start_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(3, 150, 435, 277)))
    print("Loop took {} seconds".format(time.time() - start_time))
    start_time = time.time()
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
