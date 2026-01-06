def Adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa,"Completada": False}
    tarefas.append(tarefa)
    print("Tarefa {} adicionada com sucesso.".format(nome_tarefa))

def Ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["Completada"] == True else " "
        print(f"{indice}. [{status}] {tarefa['tarefa']}")

def Atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["tarefa"] = novo_nome
        print("Tarefa {}. atualizada para {}".format(indice_tarefa, novo_nome))
    else:
        print("Índice inválido!")

def Completar_tarefa(tarefas, indice_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["Completada"] = True
        print("Tarefa: {} completada".format(tarefas[indice_ajustado]["tarefa"]))
    else:
        print("Índice inválido!")

def Deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["Completada"] == True:
            tarefas.remove(tarefa)
    print("As tarefas completadas foram deletadas!")

tarefas = []

while True:
    print("=" * 80)
    print("GERENCIADOR DE TAREFAS".center(80))
    print("=" * 80)

    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("\nDigite sua escolha: ")
    match escolha:
        case "1":
            nova_tarefa = input("\nQual tarefa você quer adicionar: ")
            Adicionar_tarefa(tarefas,nova_tarefa)

        case "2":
            Ver_tarefas(tarefas)

        case "3":
            Ver_tarefas(tarefas)
            indice_tarefa = input("\nDigite o número da tarefa que deseja atualizar: ")
            novo_nome = input("Digite o novo nome da tarefa: ")
            Atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

        case "4":
            Ver_tarefas(tarefas)
            indice_completada = input("\n Digite o número da tarefa completada: ")
            Completar_tarefa(tarefas, indice_completada)

        case "5":
            Deletar_tarefas_completadas(tarefas)
            Ver_tarefas(tarefas)

        case "6":
            break

        case _:
            print("\n❌ Opção inválida! Por favor, digite uma das opções a cima.\n")

print("\n\nTchau, até mais tarde (;")