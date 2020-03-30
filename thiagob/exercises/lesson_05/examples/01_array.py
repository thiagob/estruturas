a = ['a', 'b', 'c', 'd', 'f']

def item_exists(a, element):
    for i in range(len(a)):
        if a[i] == element:
            return True
    return False

print(item_exists(a, 'a')) # True
print(item_exists(a, 'x')) # False
