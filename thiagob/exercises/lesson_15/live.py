# já inicializando

matrix = [
    [7, 2, 1],
    [3, 4, 9],
    [21, 25, 26],
    [32, 34, 37]
]

# inicializando vazia

matrix = []
matrix.append([7, 2, 1])
matrix.append([3, 4, 9])
matrix.append([21, 25, 26])
matrix.append([32, 34, 37])

print(matrix)



# inicializando vazia

matrix_s = []
matrix_s.append(['a', 'b', 'c'])
# convert string em um array de caracteres
matrix_s.append(list('def'))

print(matrix_s)


row = 1
col = 2
print(matrix[row][col])


# quantidade de linhas
rows_count = len(matrix)

for row in range(rows_count):
    col_count = len(matrix[row])
    for col in range(col_count):
        print(matrix[row][col])


for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col])
