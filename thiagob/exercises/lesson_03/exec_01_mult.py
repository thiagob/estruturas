def multiplication(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

tests = [[2, 2], [2, 3], [4, 0], [9,9]]

for t in tests:
    print(t)
    print(multiplication(t[0], t[1]))
