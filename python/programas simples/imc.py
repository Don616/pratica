"""
Faz um cálculo simples de IMC.
"""

nome = input("Escreva seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")
ano = (int(idade) - 2020) * -1
imc = int(peso) / float(altura)


print(f"{nome} tem {idade} anos, nasceu no ano de {ano}, pesa {peso}, tem {altura} de altura e seu imc é de {imc:.1f}.")
