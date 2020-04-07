"""
Um simples programa que verifica o tamanho do nome digitado.
"""
nome = input("Olá, escreva seu nome por favor: ")
while not nome.isalpha():
    nome = input("Digite apenas letras: ")
    continue
else:
    pass
tamnome = len(nome)

if tamnome <= 4:
    print(f"Seu nome é curto em relação à maioria dos nomes, pos ele tem {tamnome} letras.")
elif tamnome >= 5 and tamnome <= 6:
    print(f"Seu nome é do tamanho mediano, pois ele tem {tamnome} letras.")
else:
    print(f"Seu nome é considerado grande, pois ele tem {tamnome} letras.")
