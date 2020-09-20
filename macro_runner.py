from  enum import Enum
import time
import threading

from autopy import key

from Sequence import Sequence
# from interface import KeyListener
from vision import ScreenVision


class cd_type(Enum):
    Nil = 0
    Attack = 2
    Healing = 4
    Support = 8
    Special = 16
    Conjure = 32


class Action:
    def __init__(self, key, cooldown_time, cooldown_type=cd_type.Nil,  name='', action=None, condition=None):

        self.key = key
        self.cooldown_time = cooldown_time
        self.cooldown_type = cooldown_type
        self.name = name
        self.action = action
        self.condition = condition

class Config:
    pace = 1

    terra_wave = Action('0', 4, cd_type.Attack, 'Terra Wave')
    intense_healing = Action('1', 1, cd_type.Healing, 'Intense Healing')
    ice_strike = Action('2', 2, cd_type.Attack, 'Ice Strike')
    ice_wave = Action('8', 4, cd_type.Attack, 'Ice Wave')
    mana_heal = Action('3', 1, cd_type.Nil, 'Mana Potion')
    avalanche = Action('4', 2, cd_type.Attack, 'Avalanche')
    # mas_san = Action('F5', 2, cd_type.Attack, 'Exevo Mas San')
    # rune_area = Action('F6', 2, cd_type.Healing, '')
    # strong_mana = Action('F4', 1, cd_type.Attack, '')
    # exura_gran_san = Action('F2', 1, cd_type.Attack, '')

    seq = Sequence([ice_strike, terra_wave, ice_strike, ice_wave])
    mana_pot_seq = Sequence([mana_heal])
    intense_healing_seq = Sequence([intense_healing])
    avalanche_sequence = Sequence([avalanche])
    # sec_pally_atk = Sequence([mas_san, rune_area])
    # sec_pally_mana = Sequence([mas_san, rune_area])
    # sec_pally_heal_mana = Sequence([mas_san, rune_area])

    # Druid
    macros = {'f1': seq,
                'f2': intense_healing_seq,
              'f3' : avalanche_sequence
              }
    # # Paladin
    # macros = {'\'1\'': sec_pally_atk}
    #

class MacroRunner:
    f_dict = {'F5': key.Code.F5,
              'F6': key.Code.F6}

    pace = Config.pace
    _running = False
    _current_sequences = dict()
    _timer = 0
    loop = None

    vision = ScreenVision()

    def __init__(self):
        self.vision = ScreenVision()


        self.quick_watch_cooldowns = dict()


        self.watching_vitals = False

    def push_sequence(self, name, seq):
        if name in self._current_sequences.keys():
            return
        pass

    def pop_seq(self, name):
        if name not in self._current_sequences.keys():
            return

    def __del__(self):
        if self.loop:
            self.loop.join()

    _t = time.time()
    c = 0
    _r = 0
    _p = 0.1
    _i = 0

    def watch_vitals(self):
        data = self.vision.read_bars()
        # print('watching', data)
        if data[1] < 0 or data[0] < 0:
            return
        cycle_time = time.time()

        for k, v in list(self.quick_watch_cooldowns.items()):
            if cycle_time - v > 1:
                del([self.quick_watch_cooldowns[k]])



        if  data[0] < .9 and '1' not in self.quick_watch_cooldowns:
                key.tap('1')
                self.quick_watch_cooldowns['1'] = time.time()


        time.sleep(0.05)


        if data[1] < .7 and '3' not in self.quick_watch_cooldowns:
            key.tap('3')
            self.quick_watch_cooldowns['3'] = time.time()


    def main_loop(self):
        while self._running:
            start = time.time()
            if self.watching_vitals:
                self.watch_vitals()

            exec_list = []
            for k, v in self._current_sequences.items():
                q = v.query(self._i)
                if q:
                    exec_list.append(q)

            for e in exec_list:
                if len(e.key) > 1:
                    if e.key in self.f_dict:
                        key.tap(self.f_dict[e.key])
                else:
                    if e.condition != None and  not e.condition():
                        continue
                    key.tap(e.key)

                time.sleep(0.05)
            # print(str(len(self._current_sequences)))
            # print(self._i)



            while time.time() - self._t < self.pace:
                time.sleep(self._p)

            print(f'Time of cycle{self._i}: {time.time() - start}')
            self._t = time.time()
            self._i += 1

    def run(self):
        self.loop = threading.Thread(target=self.macro_loop)
        self.loop.daemon = True
        self.loop.start()

    def macro_loop(self):
        self._running = True
        self.main_loop()

    def key_press(self, key):
        macros = Config.macros

        k = str(key).replace('Key.', '')

        if k == 'f19':
            self.watching_vitals = not self.watching_vitals # not self.watching_vitals

        if  k not in macros:
            return
        if k in self._current_sequences:
            del(self._current_sequences[k])
        else:
            self._current_sequences[k] = macros[k]


