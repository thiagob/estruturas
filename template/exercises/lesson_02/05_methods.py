def is_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even(n):
    return not is_odd(n)

print(is_odd(7))
print(is_even(7))