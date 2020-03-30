def print_replacing(s, pos):
    if pos >= len(s):
        return
        
    a = list(s)
    a[pos] = "*"
    print("".join(a))
    print_replacing(s, pos + 1)


print_replacing("Thiago Bohn", 0)