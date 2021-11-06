import random as rd
moedas = []

for i in range(10):
    num = rd.uniform(0,10)
    moedas.append(num)

money = {
    "Dollar" :moedas[0],
    "Euro"   :moedas[1],
    "Libra"  :moedas[2],
    "Iene"   :moedas[3],
    "Franco" :moedas[4],
    "Yuan"   :moedas[5],
    "Peso"   :moedas[6],
    "Rupia"  :moedas[7],
    "Rand"   :moedas[8],
    "Bitcoin":moedas[9],
}

for x, y in money.items():
    print("{} está valendo R${:.2f} neste momento".format(x, y))