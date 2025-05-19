import os

def add_projeto():
    os.system("cls")
    print("Menu - Adicionar Projeto")
    print("0 - Cancelar e voltar ao menu principal.")
    id = input("Insira o ID do projeto: ")
    if id == 0:
        menu()
        return

def del_projeto():
    os.system("cls")

def ver_projeto():
    os.system("cls")

def filtrar_projeto():
    os.system("cls")

def menu():
    os.system("cls")
    print("Gerenciador de Projetos")
    print("\nMenu\n")
    print("1 - Adicionar Projeto")
    print("2 - Deletar Projeto")
    print("3 - Verificar Projetos")
    print("4 - Filtrar Projetos")

    menu_op = int(input("\nInsira a opção do menu desejada: "))

    while menu_op:
        if menu_op == 1:
            add_projeto()
            menu_op = 0
        elif menu_op == 2:
            del_projeto()
            menu_op = 0
        elif menu_op == 3:
            ver_projeto()
            menu_op = 0
        elif menu_op == 4:
            filtrar_projeto()
            menu_op = 0
        else:
            print("\nInsira uma opção válida.")
            menu_op = int(input("\nInsira a opção do menu desejada: "))

menu()

