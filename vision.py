import mss

import cv2
import numpy as np
import time
import pytesseract
import threading
from PIL import Image


class ScreenVision:

    def __init__(self):
        self. watching_bars = False
        self.img_bar = None
        self.imgs = []
        self._t = None
        self._hp = -1
        self._mana = -1
        self._time = time.time()
        self._first_grab = True

    config = '-c tessedit_char_whitelist=0123456789'

    pois = [(1621.0, 325.0), (1665.0, 350), #HP mana
           (67.0, 838.0), (188.0, 861.0), #cool downs
           (1513.0, 251.0), (1543.0, 282.0), #ring
           (1333.0, 60.0), (1485.0, 298.0), #battle
           (1332.0, 319.0), (1486.0, 537.0)] #pt
    def grab_screen(self, rect):
        with mss.mss() as sct:
            return sct.grab(rect)

    def build_rect(self, a,b):
        top = min(a[1], b[1])
        left = min(a[0], b[0])
        width = abs(a[0] - b[0])
        height = abs(a[1] - b[1])
        return {'top' : top, 'left' : left, 'width' : width, 'height' : height}

    def read_bars(self):
        lt = time.time()
        # img = np.array(self.grab_screen(self.build_rect((1527.0, 331.0), (1615.0, 334.0))))
        # img2 = np.array(self.grab_screen(self.build_rect((1528.0, 340.0), (1616.0, 347.0))))
        img = self.grab_screen(self.build_rect((1528.0, 332.0), (1619.0, 333.0)))
        img2 = self.grab_screen(self.build_rect((1528.0, 345.0), (1619.0, 346.0)))
        c = 0
        l = len(img.pixels[0])
        if l <= 0:
            return
        for p in img.pixels[0][::-1]:
            if p[0] > 245:
                break
            c += 1
        self._hp = 1 - c / l
        # print(f'Hp: {self._hp}')

        c = 0
        l = len(img2.pixels[0])
        for p in img2.pixels[0][::-1]:
            if p[2] > 245:
                break
            c += 1
        self._mana = 1 - c / l
        # print(f'Mana: {self._mana}')
        # def capture_img():
            # a = Image.fromarray(img)
            # DEBUG PURPOSES
            # a = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            # a.show()
            # b = Image.frombytes("RGB", img2.size, img2.bgra, "raw", "BGRX")
            # b.show()


            # (_, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            #
            # self.img_bar = cv2.bitwise_not(img).copy()
            #
            # print(f'capture took {time.time() -lt}')
            # print(f'Got img:  {time.time() - self._time}')


            # lt = time.time()
            # img = np.array(self.grab_screen(self.build_rect((1621.0, 325.0), (1665.0, 350))))
            # img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
            # (_, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            # self.img_bar = cv2.bitwise_not(img).copy()
            # print(f'capture took {time.time() -lt}')
            # print(f'Got img:  {time.time() - self._time}')


        # def read_img():

        #     lt = time.time()
        #     hp_mana = pytesseract.image_to_string(self.img_bar, config=self.config).split('\n')
        #
        #     if len(hp_mana) < 2:
        #         return None
        #     self._hp = int(hp_mana[0])
        #     self._mana = int(hp_mana[1])
        #     print(f'read took {time.time() -lt}')
        #     print(f'Read img: {time.time() - self._time}')
        #
        #
        # if  self._first_grab:
        #     capture_img()
        #     self._first_grab = False
        # t1 = threading.Thread(target=capture_img)
        # t2 = threading.Thread(target=read_img)
        #
        # t1.start()
        # t2.start()
        #
        # t1.join()
        # t2.join()
        return (self._hp, self._mana)


    def watch_bars(self, action):
        def loop():

            while self.watching_bars:
                self.read_bars()
                action((self._hp, self._mana))

        self._t = threading.Thread(target=loop)
        self._t.daemon = True
        self._t.start()






    def see(self):
        for i in range(len(self.pois)//2):
            p = i * 2
            a = self.pois[p]
            b = self.pois[p +1]
            self.imgs.append(np.array(self.grab_screen(self.build_rect(a, b))))
        c = 0
        for img in self.imgs:
            cv2.imwrite(f'{c}.png', img)

            if c == 0:
                print(pytesseract.image_to_string(img, config=self.config))
            c += 1


# time.sleep(0)
# a = ScreenVision()
# t = 0
# historic = []
# while True:
#     t = time.time()
#     a.read_bars()
#     historic.append(time.time() - t)
#     print(sum(historic)/len(historic))
# def act(dt):
#     if dt:
#         print(dt[0], dt[1])
# a.watching_bars = True
# a.watch_bars(act)



# 0 -> 0
# 1 -> 2
# 2 -> 4
# 3 - > 6