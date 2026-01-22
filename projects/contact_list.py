# Fazer verificação se foi colocado algum número, se o numero tem 9, se não tem

class ListaDeContatos:
    # () Cadastro de contato -> O sistema deve permitir o cadastro de um novo contato com os seguintes campos: nome, telefone, e-mail e status de favorito.
    # () Listagem de contatos -> O sistema deve permitir a visualização da lista completa de contatos cadastrados.
    # () Listagem de favoritos -> O sistema deve permitir a visualização apenas dos contatos marcados como favoritos.
    # () Exclusão de contato -> O sistema deve permitir a exclusão de um contato cadastrado.
    pass

class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._favorito = favorito
    
    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self,valor):
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio!")
        self._nome = valor.strip()
        
    
    def editar(self):
        pass

    def favoritar(self):
        pass

"""
 
    # Property: telefone
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        # Remove caracteres não numéricos
        apenas_numeros = ''.join(filter(str.isdigit, valor))
        if len(apenas_numeros) < 8:
            raise ValueError("Telefone deve ter pelo menos 8 dígitos!")
        self._telefone = valor
    
    # Property: email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            raise ValueError("Email inválido!")
        self._email = valor.strip().lower()
    
    # Property: favorito
    @property
    def favorito(self):
        return self._favorito
    
    @favorito.setter
    def favorito(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Favorito deve ser True ou False!")
        self._favorito = valor
    
    # Métodos de ação
    def alternar_favorito(self):
        """Alterna entre favorito e não-favorito"""
        self._favorito = not self._favorito
    
    def __str__(self):
        """Representação em string do contato"""
        fav = "⭐" if self._favorito else ""
        return f"{fav}{self._nome} | {self._telefone} | {self._email}""""









def exibir_menu():
    print("CONTATOS\n".center(80))
    print("1. Adicionar novo contato")
    print("2. Ver lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver favoritos")
    print("6. Apagar contato")
    print("7. Sair")

def main():


    while True:
        exibir_menu()
        try:
            escolha = input("\nDigite uma opção: ")
            match escolha:
                case "1":
                    pass

                case "2":
                    pass
                
                case "3":
                    pass

                case "4":
                    pass
                
                case "5":
                    pass
                
                case "6":
                    pass
                
                case "7":
                    print("\n👋 Até logo!")
                    break
                
                case _:
                    print("\n❌ Opção inválida! Por favor, digite uma das opções a cima.\n")
        except Exception as erro:
            print(f"Erro: {erro}")

if __name__ == "__main__":
    main()

"""@classmethod
    def criar_carro(cls, config):
        marca, modelo, ano = config.split(",")
        return cls(marca, modelo, ano)

config1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(config1)
print(f"Marca: {carro1.marca}\nModelo:{carro1.modelo}\nAno: {carro1.ano}")"""
"""
class MinhaClasse:
    valor = 10 # Atributo da classe

    def __init__(self, nome):
        self.nome = nome # Atributo da instância

    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod #metodo da classe
    def metodo_classe(cls):
        return f"Método de classe chamado para valor={cls.valor}"

    @staticmethod
    def metodo_estatico():
        return "Meodo estático chamado"


obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, config):
        marca, modelo, ano = config.split(",")
        return cls(marca, modelo, ano)

config1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(config1)
print(f"Marca: {carro1.marca}\nModelo:{carro1.modelo}\nAno: {carro1.ano}")"""