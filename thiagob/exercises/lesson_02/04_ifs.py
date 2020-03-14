if 3 > 2:
    print('Funciona!')


n = int(input("Enter a number: "))

if n == 0:
    print("ZERO is even")
elif n % 2 == 0:
    print(str(n) + " is even")
else:
    print(str(n) + " is odd")