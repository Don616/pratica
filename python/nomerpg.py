import random as rd
def ger_nome():
    vogais = ("a","e","i","o","u")
    abc = "abcdefghijklmnopqrstuvwxyz"
    num_letras = rd.randint(4,7)
    lista = []
    nome = ""
    for x in range(num_letras):
        lista += [(rd.choice(abc))]
        if vogais not in lista:
            lista.append(rd.choice(vogais))
        while len(lista) > num_letras:
            lista.pop()
    for y in lista:
        nome += y

    return print(nome.title())


ger_nome()
