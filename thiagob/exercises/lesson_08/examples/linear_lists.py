# Como declarar um array
empty = []
numbers = [1, 2, 3, 4]
strings = ['Hello', 'World']

# Como obter o tamanho
length = len(numbers)
print(length) # 4

# Como adicionar um item no final
strings.append('!')
print(strings) # ['Hello', 'World', '!']

# Como adicionar um item no início
strings.insert(0, 'My first')
print(strings) # ['My first', 'Hello', 'World', '!']





# Com limpar um array
strings.clear()
print(strings) # []

# Como converter uma string in um array
strings = 'Amanhã é dia de Tiradentes'.split(' ')
print(strings) # ['Amanhã', 'é', 'dia', 'de', 'Tiradentes']

# Como remover um item do array
strings.remove('Tiradentes')
print(strings) # ['Amanhã', 'é', 'dia', 'de']

# Como remover um item do array através do Index
del strings[3]
print(strings) # ['Amanhã', 'é', 'dia']

item = strings.pop(1)
print (item) # é
print(strings) # ['Amanhã', 'dia']





strings = ['Amanhã', 'é', 'dia']
# Como ler o último item
last = strings[len(strings)-1]
print(last) # dia

last = strings[-1]
print(last) # dia


# Como adicionar vários items no array
strings.extend(['de', 'delete', 'sem', 'where'])
print(strings) # ['Amanhã', 'é', 'dia', 'de', 'delete', 'sem', 'where']

strings = strings + ['e', 'ficar', 'em', 'casa']
print(strings) # ['Amanhã', 'é', 'dia', 'de', 'delete', 'sem', 'where', 'e', 'ficar', 'em', 'casa']

# Como ler somente parte do array
sub = strings[0:4]
print(sub) # ['Amanhã', 'é', 'dia', 'de']

# Como ler somente parte do array

#    (0)     (1)   (2)    (3)     (4)     (5)     (6)    (7)    (8)     (9)   (10)
# ['Amanhã', 'é', 'dia', 'de', 'delete', 'sem', 'where', 'e', 'ficar', 'em', 'casa']
#   (-11)   (-10)  (-9)   (-8)   (-7)     (-6)    (-5)   (-4)   (-3)   (-2)   (-1)

sub = strings[2:-4]
print(sub) # ['dia', 'de', 'delete', 'sem', 'where']





# Como order um array
nums = [27, 35, 2, 8, 9, 26, 14, 13]
nums.sort()
print(nums) # [2, 8, 9, 13, 14, 26, 27, 35]

# Como inverter um array
nums.reverse()
print(nums) # [35, 27, 26, 14, 13, 9, 8, 2]

# Como converter um array um string
fruits = ['Maça', 'Banana', 'Laranja', 'Abacata']
print('Lista de Compras: ' + ', '.join(fruits))
# Output: Lista de Compras: Maça, Banana, Laranja, Abacata