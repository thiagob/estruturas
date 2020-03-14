fruits = ["apple", "orange", "pineapple", "banana"]

for fruit in fruits:
    print(fruit)

fruits.append("Grapes")
print(fruits)

for i in range(0, len(fruits)):
    print(fruits[i])

for idx, val in enumerate(fruits):
    print(idx)
    print(val)

n = ""
while not n.isdigit():
    n = input("Enter a number: ")

while True:
    n = input("Enter a number: ")
    if n.isdigit():
        break