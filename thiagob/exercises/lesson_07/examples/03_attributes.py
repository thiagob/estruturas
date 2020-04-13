class Animal:
    patas = 0

class Cachorro:
    patas = 4
    raca = "Vira Lata"
    truques = ["Sentar", "Rolar", "Dar a pata"]

class Cavalo:
    patas = 4
    pelo = "Tobiano"
    andamentos = ["Marcha", "Trote", "..."]

toto = Cachorro()
print(toto.patas)
print(toto.truques)

pingo = Cavalo()
print(pingo.patas)

rex = Cachorro()
rex.truques = []
print("Rex: " + rex.truques)
print("Toto: " + toto.truques)

