from pynput import keyboard
from autopy import key
from autopy import mouse

import asyncio
import threading

# The key combination to check

class Listener:
    COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl}
    #408
    # The currently active modifiers
    current=set()
    wave_seq = [('4', 2.1),('LMC',0.01), ('0',2.1),('4',2.1),('LMC',0.01), ('8',2.1)]

    async def wave_combo_sequence(self):
        try:
            i = 0
            l = len(self.wave_seq)
            while True:
                if self.wave_cor:
                    await asyncio.sleep(self.wave_seq[i][1])
                    cmd = self.wave_seq[i][0]
                    if cmd == 'LMC':
                        mouse.click()
                    else:
                        key.tap(cmd)

                    i = (i + 1) % l

        except asyncio.CancelledError:
            raise

    heal_seq = [('1', 2.1), ('1', 2.1)]

    async def heal_combo_sequence(self):
        try:
            i = 0
            l = len(self.heal_seq)
            while True:
                if self.heal_cor:
                    await asyncio.sleep(self.heal_seq[i][1])
                    cmd = self.heal_seq[i][0]
                    if cmd == 'LMC':
                        mouse.click()
                    else:
                        key.tap(cmd)

                i = (i + 1) % l

        except asyncio.CancelledError:
            raise

    wave_cor = False
    heal_cor = False

    def loop_in_thread(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.wave_combo_sequence())

    def loop_in_thread_heal(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.heal_combo_sequence())

    t1 = None
    t2 = None
    def on_press(self, key):
        print(key)
        if key == keyboard.Key.f1:
            if not self.wave_cor:
                if not self.t1:
                    self.t1 = threading.Thread(target=self.loop_in_thread, args=(self.loop,), name='f1')
                    self.t1.start()
                self.wave_cor = True
                return
            else:

                self.wave_cor = False

        if key == keyboard.Key.f2:
            if not self.heal_cor:
                if not self.t2:
                    self.t2 = threading.Thread(target=self.loop_in_thread_heal, args=(self.loop,), name="f2")
                    self.t2.start()
                self.heal_cor = True
                return
            else:
                self.heal_cor = False




        if key in self.COMBINATION:
            self.current.add(key)
            if all(k in self.current for k in self.COMBINATION):
                print('All modifiers active!')
        if key == keyboard.Key.esc:
            self.listener.stop()


    def on_release(self, key):
        try:
            self.current.remove(key)
        except KeyError:
            pass
    executor = None

    loop = None
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

# Listener()

while True:
    key.tap(1)
    key.tap(2)