class Carro:

    estado = "desligado"

    def ligar(self):
        self.estado = "ligado"

class Onix(Carro):

    def ligar_central_multimedia(self):
        self.central = "ligado"

    def ligar(self):
        self.ligar_central_multimedia()


fusca = Carro()
fusca.ligar()
print(fusca.estado)

class Cachorro:

    nome = None
    dono = None
    adocao = False

    def correr(self):
        pass

    def __init__(self, nome, dono=None):
        self.nome = nome
        self.dono = dono
        # 
        if dono == None:
            self.adocao = True
        
        self.correr()

toto = Cachorro("Totó", "Thiago")
fifi = Cachorro("Fifi")
print(fifi.adocao)


# [ ] É possível redefinir os getters e setters em Python?
# [ ] Ajustar setas dos diagramas de classes (herança)