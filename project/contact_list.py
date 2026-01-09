class Contato:
    def __init__(self, nome="Novo Contato", telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

contatos = []
# Fazer verificação se foi colocado algum número, se o numero tem 9, se não tem
def adicionar_contato(contatos, nome, telefone, email):
    novo_contato = Contato(nome, telefone, email)
    for contato in contatos:
        if telefone == contato.telefone:
            print("❌ Esse número já foi salvo anteriormente")
            return
    contatos.append(novo_contato)
    print("Novo contato salvo com sucesso!")
    

while True:

    print("CONTATOS\n".center(80))
    print("1. Adicionar novo contato")
    print("2. Ver lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    try:
        escolha = input("\nDigite uma opção: ")
        match escolha:
            case "1":
                novo_contato_nome = input("Digite o nome do contato: ")
                novo_contato_telefone = input("Digite o telefone: ")
                novo_contato_email = input("Digite o email: ")
                adicionar_contato(contatos, novo_contato_nome, novo_contato_telefone, novo_contato_email)

            case "2":
                a
            case "3":
                
            case "4":
                a
            case "5":
                a
            case "6":
                a
            case "7":
                a
            case _:
                print("\n❌ Opção inválida! Por favor, digite uma das opções a cima.\n")



    except Exception as erro:
        print(f"Erro: {erro}")
