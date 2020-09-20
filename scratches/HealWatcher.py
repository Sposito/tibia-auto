import numpy as np
from PIL import ImageGrab
import imutils
import cv2
import time
import mss

# with mss.mss() as sct:
#     sct.grab(0, )
# for _ in range(50):
#     t = time.time()
#     image = ImageGrab.grab(bbox=(5,5,6,6))
#     # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     t = time.time() - t
#     print(t)
# cv2.imwrite("in_memory_to_disk.png", image)

for _ in range(10000):
    with mss.mss() as sct:
    # Use the 1st monitor

        t = time.time()
        monitor = sct.monitors[1]

        # Capture a bbox using percent values
        left = monitor["left"] + monitor["width"] * 0 // 100  # 5% from the left
        top = monitor["top"] + monitor["height"] * 0 // 100  # 5% from the top
        right = left + 1000  # 400px width
        lower = top + 1000  # 400px height
        bbox = (left, top, right, lower)

        # Grab the picture
        # Using PIL would be something like:
        # im = ImageGrab(bbox=bbox)
        im = sct.grab(bbox)  # type: ignore
        t = time.time() - t
        print(t)