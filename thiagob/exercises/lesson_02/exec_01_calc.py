def validate_number(n):
    if n.isdigit():
        return int(n)
    else:
        print(n + " is not a valid number")
        exit()

def validate_operations(op):
    if op in ["+", "-", "/", "*"]:
        return op
    else:
        print(op + " is not a valid operation")
        exit()

def calc(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "/":
        return n1 / n2
    else:
        return n1 * n2

n1 = validate_number(input("Enter a number: "))
op = validate_operations(input("Enter an operation [+, -, /, *]: "))
n2 = validate_number(input("Enter a number: "))

result = calc(n1, op, n2)
print("%d %s %d = %d" % (n1, op, n2, result))