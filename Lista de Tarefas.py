tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    numero = int(input("Digite o número da tarefa que deseja remover: "))
    if 1 <= numero <= len(tarefas):
        tarefa_removida = tarefas.pop(numero - 1)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        adicionar_tarefa()
    elif escolha == '2':
        listar_tarefas()
    elif escolha == '3':
        remover_tarefa()
    elif escolha == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
