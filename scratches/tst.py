from datetime import datetime
from autopy import mouse
from pynput import mouse
# print(datetime.now().hour == 23)
import os
import time

beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
rec = []
def click(x, y,a,b):
    if b and str(a) == 'Button.middle':
        rec.append((x,y))
        beep(1)
        if len(rec) % 2 == 0:
            pass
            print(rec)
            beep(1)





with mouse.Listener(on_click=click) as listener:
    # listener.daemon = True
    listener.join()





# while(True):
#     print (mouse.location())
#     mouse.click()
#     time.sleep(.2)

import time

import cv2
import mss
import numpy


# def screen_record():
#     try:
#         from PIL import ImageGrab
#     except ImportError:
#         return 0
#
#     # 800x600 windowed mode
#     mon = (0, 40, 800, 640)
#
#     title = "[PIL.ImageGrab] FPS benchmark"
#     fps = 0
#     last_time = time.time()
#
#     while time.time() - last_time < 10:
#         img = numpy.asarray(ImageGrab.grab(bbox=mon))
#         fps += 1
#
#         cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         if cv2.waitKey(25) & 0xFF == ord("q"):
#             cv2.destroyAllWindows()
#             break
#
#     return fps
#
#
# def screen_record_efficient():
#     # 800x600 windowed mode
#     mon = {"top": 40, "left": 0, "width": 800, "height": 640}
#
#     title = "[MSS] FPS benchmark"
#     fps = 0
#     sct = mss.mss()
#     last_time = time.time()
#
#     while time.time() - last_time < 10:
#         img = numpy.asarray(sct.grab(mon))
#         fps += 1
#
#         cv2.imshow(title, img)
#         if cv2.waitKey(25) & 0xFF == ord("q"):
#             cv2.destroyAllWindows()
#             break
#
#     return fps
#
#
# print("PIL:", screen_record())
# print("MSS:", screen_record_efficient())