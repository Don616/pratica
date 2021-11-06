'''
d1 = dict(c1='valor1', c2='valor2', c3='valor3')

print(d1["c1"])

'''
'''
d2 = {
    "chave1" : "valor1",
    "chave2" : "valor2",
    "chave3" : "valor3",
}

for k in d2:
    print(k)
'''

animais = {
    "reptil"   : {
            "jacare"  : {1},
            "cobra"   : {2},
            "dragao"  : {3},
    },
    "ave"      : {
            "pinguin" : {4},
            "aguia"   : {5},
            "coruja"  : {6},
    },
    "mamifero" : {
            "humano"  : {7},
            "macaco"  : {8},
            "vaca"    : {9},
    },
    "peixe"    : {
            "salmao"  : {10},
            "atum"    : {11},
            "sardinha": {12},
    },
}

error_cont = 0
while error_cont < 4:
    tipo_dado = input("Que tipo de animal procura? Peixe, Réptil, Mamífero ou Ave? ")
    if tipo_dado not in animais:
        print("Não encontrado!")
        error_cont += 1
        if error_cont == 3:
            print("Tente novamente mais tarde")
            break
        continue
        
            
        
    
a = list(animais[tipo_dado].keys())

print(a)
print(a[-1])
