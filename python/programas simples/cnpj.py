"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

def remove_ponto(cnpj):
    cnpj_limpo = ''
    for x in cnpj:
        if x.isnumeric():
            cnpj_limpo += x
    return cnpj_limpo


def multiplicador(x=list,y=list):
    lista_multiplicada = []
    i = 0
    for item in x:
        resultado = item * y[i]
        lista_multiplicada.append(resultado)
        i += 1
    return lista_multiplicada


def formula(num):
    f = 11 - (num % 11)
    if f > 9:
        return 0
    else:
        return f


def verificador(valor1, valor2):
    if valor1 == valor2:
        return "verdadeiro"
    else:
        return "falso"


def gerador_formula(lista):
    if len(lista) == 12:
        lista1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    elif len(lista) == 13:
        lista1 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    lista2 = []
    for x in lista:
        lista2.append(int(x))
    lista3 = []
    i = 0
    for y in lista1:
        lista3.append(y * lista2[i])
        i += 1
    return sum(lista3)


def master(cnpj):
    novo_cnpj = ""
    for x in cnpj:
        if x == "-":
            novo_cnpj = remove_ponto(novo_cnpj)
            lista1 = []
            break
        else:
            novo_cnpj += x

    digito_1 = gerador_formula(novo_cnpj)
    a = formula(digito_1)
    cnpj_final = novo_cnpj + str(a)
    digito_2 = gerador_formula(cnpj_final)
    b = formula(digito_2)
    cnpj_final += str(b)
    z = verificador(remove_ponto(cnpj), cnpj_final)
    return print(f'Seu CNPJ:"{cnpj}" é {z}!')

# -----------------------------

cnpj = "71.506.168/0001-11"
master(cnpj)


