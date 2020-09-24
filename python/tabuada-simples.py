#Cria uma tabuada do número escolhido até zero.
numero1 = (input("Digite qualquer número: "))

while numero1.isnumeric() == False:
    numero1 = (input("Digite somente números: "))

numero1 = int(numero1)
numero2 = numero1

calc = 0
while numero2 >= 0:
    calc = numero1 * numero2
    print(f"{numero1}x{numero2} = {calc}")
    numero2 -= 1
