from random import randint

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def lotofacil():
    while True:
        p = 0 #p = quantidade de numeros par na minha lista game1
        i = 0
        game1 = []
        soma = 0
        while len(game1) < 15:
            r = randint(1,25) #r = numero gerado aleatoriamente
            if r not in game1:
                game1.append(r)
                soma += r
                if par(r):
                    p += 1
                    if p >= 9:
                        game1.pop()
                        p -= 1
                    else:
                        pass
                else:
                    i += 1
                    if i >= 10:
                        game1.pop()
                        i -= 1
            if len(game1) == 15:
                break
        if soma >= 181 and soma <= 210:
            game1.sort()
            return game1
        else:
            continue


    


loto = lotofacil()

print("Segue abaixo os números para você jogar:")
print("---"*10)
print()
print(loto)
print()
print("---"*10)
