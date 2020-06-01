from app import lib

stack = lib.lists.Stack()

print("Length => %i" % stack.length())
print("")
print(">>> João")

stack.push("O cortiço, de Aluísio Azevedo")
stack.push("Dom Casmurro, de Machado de Assis")

print("Length => %i" % stack.length())
print("")
print(">>> José")
print(stack.pop())

stack.push("Triste fim de Policarpo Quaresma, de Lima Barreto")
stack.push("São Bernardo, de Graciliano Ramos")
stack.push("São Bernardo, de Graciliano Ramos")

print("Length => %i" % stack.length())
print("")
print(">>> Maria")
print(stack.pop())

stack.push("Morte e vida severina, de João Cabral de Melo Net")
stack.push("Grande sertão: Veredas, de Guimarães Rosa")
stack.push("A hora da estrela, de Clarice Lispector")

print("Length => %i" % stack.length())
print("")
print(">>> Joana")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.push("O caderno rosa de Lori Lamby, de Hilda Hist")

print("Length => %i" % stack.length())
print("")
print(">>> Teresa")
print(stack.pop())
print(stack.pop())

print("Length => %i" % stack.length())