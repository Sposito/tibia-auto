from pynput import keyboard

from macro_runner import MacroRunner


class KeyListener:
    macro = MacroRunner()

    def listen(self):
        self.macro.run()
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if key is keyboard.Key.f13:
            quit()
        self.macro.key_press(key)

    def on_release(self, key):
        pass
