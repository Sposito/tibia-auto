import autopy
#9fjhmy5e
from datetime import datetime
from autopy import key
from autopy import mouse
import time
import random

print(datetime.now().hour)
def login():
    # key.tap(key.Code.SPACE, [key.Modifier.META])
    # print('star sleep')
    # time.sleep(1)
    # print('end sleep')
    # key.tap('t', delay=1)
    # time.sleep(2)
    # key.tap(key.Code.RETURN)
    #
    time.sleep(5)
    key.type_string('3y7z6qmc')
    key.tap(key.Code.RETURN)

    time.sleep(5)
    key.tap(key.Code.RETURN)

def make_avalanche():
    ct = 0
    relogin = False
    while True:
        # if not relogin and datetime.now().hour == 5 and datetime.now().minute > 25:
        #     print('\n\n--------------\nRELOGIN\n\n\n')
        #     login()
        #     relogin = True

        ct += 1
        print(f'Round {ct}:')
        for i in range(4):
            print('Eating mushroom')
            key.tap(key.Code.F2)
            time.sleep(random.random()/2)

        for i in range(7):
            if ct == 1:
                continue

            print('Making avalanche')
            key.tap(key.Code.F1)
            time.sleep(3 + random.random())
        print('...')
        key.tap(key.Code.F3)

        time.sleep(5)
        print('Using Dummy...')
        key.tap(key.Code.F4)
        time.sleep(1)
        mouse.smooth_move(870.0, 61.0)
        mouse.click()
        time.sleep(1)
        mouse.smooth_move(random.random() * 1000, random.random() * 1000)
        wait_time = 10 * 60 / 2
        # wait_time = wait_time
        print(f'Waiting {wait_time} seconds')
        time.sleep(wait_time)


key.tap(key.Code.TAB, [key.Modifier.META])
make_avalanche()
key.tap(key.Code.TAB, [key.Modifier.META])

