def print_with_repace(s, pos):
    if pos >= len(s):
        return
        
    a = list(s)
    a[pos] = "*"
    print("".join(a))
    print_with_repace(s, pos + 1)


print_with_repace("Thiago Bohn", 0)