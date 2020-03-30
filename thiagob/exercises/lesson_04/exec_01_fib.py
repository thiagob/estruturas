from app import lib

t = lib.Timer()

t.start()
print(lib.math.fibonacci_i(5))
#print(lib.math.fibonacci_i(35))
print(t.stop())

t.start()
print(lib.math.fibonacci_r(5))
#print(lib.math.fibonacci_r(35))
print(t.stop())