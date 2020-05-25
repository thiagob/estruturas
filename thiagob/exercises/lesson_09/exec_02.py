from app import lib

pilha = lib.Stack(False)

# adicionar números de 1 a 10
for i in range(1, 11):
    pilha.push(i)

# remover 3 números
for i in range(3):
    pilha.pop()

# adicionar números de 1 a 5
for i in range(1, 6):
    pilha.push(i)

# remover 8 números
for i in range(7):
    pilha.pop()

# retirar elemento desejado
print(pilha.pop())