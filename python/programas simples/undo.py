# Faça um programa que execute undo sempre que pedir
from sys import exit

def memoria(x):
    copia_tarefas = x
    

lista_tarefas = []
while True:
    tarefas = input("\nAdicione uma tarefa: ").title()
    print("="*10)
    print("Minha lista de tarefas: ")
    lista_tarefas.append(tarefas)
    print(memoria(lista_tarefas))
    print(*lista_tarefas,sep=", ")
    print()
    print("="*10)
    exe = input("Deseja adicionar mais? Digite:\n'S' para Sim;\n'N' para Não;\n'D' para Desfazer;\n'R' para Refazer.\n~: ").upper()
    if exe[0] == 'S':
        continue
    elif exe[0] == 'N':
        exit()
    elif exe[0] == 'D':
        pass



