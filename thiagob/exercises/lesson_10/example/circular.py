a = ["João", "Maria", "Jóse", "Pedro"]

counts = 10
count = 0

# Forma 1
index  = 0
while count < counts:
    print(a[index])
    count += 1
    index += 1

    if index >= len(a):
        index = 0

# Forma 2
count = 0
while count < counts:
    index = count % len(a)
    print(a[index])
    count += 1


