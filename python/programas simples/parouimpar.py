# Um simples identificador que retorna se o número digitado é par ou impar.
sair = 'y'
print()
print("Esse programa verifica se o número digitado é inteiro, par ou impar")
print('='*65)
while True:

    if sair == "y":
        pass
    elif sair == "n":
        break
    else:
        sair = input("Digite 'y' se deseja sair ou 'n' se deseja continuar: ")
        continue    


    num = input("Digite um número inteiro: ")
    print()

    if num.isnumeric():
        num = int(num)
        print(f"O número {num} é um número inteiro.")
    else:
        print("Você não digitou um número inteiro!")
        print()
        continue
    print()

    if (num % 2) == 0:
        print("O número que você digitou é par!")
        print()
        sair = input("Digite 'y' se deseja sair ou 'n' se deseja continuar: ")
        continue
        
    else:
        print("O número que você digitou é impar!")
        print()
        print('='*65)
        sair = input("Digite 'y' se deseja sair ou 'n' se deseja continuar: ")
        continue

    print()

