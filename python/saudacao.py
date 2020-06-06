"""
Faça um programa que pergunte a hora para o usuário e, se baseando no horário descrito, exiba a saudação apropriada.
"""

hora = input("Que horas são aí? ")

if hora.isnumeric():
    hora = int(hora)
else:
    print("Por favor, digite somente números.")
if hora < 0 or hora > 23:
    print("Horário inválido")
elif hora <= 5:
    print(f"Ainda é de madrugada, são {hora} horas, então podemos considerar boa noite!")
elif hora >= 6 and hora <= 11:
    print(f"Bom dia! Agora são {hora} horas.")
elif hora >= 12 and hora <= 17:
    print(f"Boa tarde! Agora são {hora} horas da tarde.")
else: 
    print(f"Boa noite! Agora são {hora} horas da noite.")
