from interface import KeyListener
import cProfile
listener = KeyListener()
cProfile.run(listener.listen())


