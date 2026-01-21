class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        #return super().emitir_som() # Super() chama implementação da classe mãe
        return "Morcegos emitem sons ultrassônicos"