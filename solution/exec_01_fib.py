import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from config import lib as lib
import importlib


t = lib.Timer()

t.start()
print(lib.math.fibonacci_i(5))
#print(lib.math.fibonacci_i(35))
print(t.stop())

t.start()
print(lib.math.fibonacci_r(5))
#print(lib.math.fibonacci_r(35))
print(t.stop())