# Slide 5
matrix = []
matrix.append([7, 2, 1])
matrix.append([3, 4, 9])
matrix.append([21, 25, 26])
matrix.append([32, 34, 37])

print(matrix)

# Slide 6

row = 1
col = 2

print(matrix[row][col]) # 9

# Slide 7

for line in matrix:
    for item in line:
        print(item)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col])


# Slide 8
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col])
