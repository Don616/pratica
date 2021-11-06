import random as rd
def get_nome(raça=None):
    vogais = ("a","e","i","o","u")
    abc = "abcdefghijklmnopqrstuvwxyz"
    raciais = {
        "elfo"  :{"el","il","in","as"},
        "orc"   :{"nag","ok","ur","uk"},
        "humano":{"ir","ob","son","an"},
    }
    num_letras = rd.randint(4,7)
    lista = []
    nome = ""
    for x in range(num_letras):
        lista += [(rd.choice(abc))]
        if vogais not in lista:
            lista.append(rd.choice(vogais))
        while len(lista) > num_letras:
            lista.pop()
    if raça in raciais:
        lista.pop()
        r = list(raciais[raça])
        lista.append(rd.choice(r))
        
    for y in lista:
        nome += y

    return print(nome.title())


get_nome("humano")
