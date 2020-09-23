print()
print("Responda as perguntas de acordo com as opções. Se marcar alguma certa, ganha um ponto; se marcar uma errada, ou digitar qualquer outra coisa, perde um ponto.")
print()

questoes = {
    "Questão 01"      : {
        "pergunta"    : "Quanto é 5 * 8?",
        "opcão"       : {
            "a"       : "35",
            "b"       : "45",
            "c"       : "55",
            "d"       : "40",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "d",
    },
    "Questão 02"      : {
        "pergunta"    : "Quantos jogadores máximos é possível ter em uma partida de Fall Guys?",
        "opcão"       : {
            "a"       : "50",
            "b"       : "60",
            "c"       : "70",
            "d"       : "100",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "b",
    },
    "Questão 03"      : {
        "pergunta"    : "Qual destes ossos está localizado na região da cabeça?",
        "opcão"       : {
            "a"       : "Rádio",
            "b"       : "Úmero",
            "c"       : "Esfenóide",
            "d"       : "Trapézio",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "c",
    },
    "Questão 04"      : {
        "pergunta"    : "Qual destes países se isentou durante a Segunda Grande Guerra?",
        "opcão"       : {
            "a"       : "Suécia",
            "b"       : "Portugal",
            "c"       : "Israel",
            "d"       : "Somália",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "a",
    },
    "Questão 05"      : {
        "pergunta"    : "Qual destas cores não pertece ao conjunto de cores RGB?",
        "opcão"       : {
            "a"       : "Ciano",
            "b"       : "Magenta",
            "c"       : "Preto",
            "d"       : "Amarelo",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "e",
    },
    "Questão 06"      : {
        "pergunta"    : "Na última prova do Exame Hunter do Anime HunterxHunter, qual candidato foi reprovado?",
        "opcão"       : {
            "a"       : "Razon",
            "b"       : "Killua",
            "c"       : "Hisoka",
            "d"       : "Neji",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "b",
    },
    "Questão 07"      : {
        "pergunta"    : "Qual a velocidade média do som no ar?",
        "opcão"       : {
            "a"       : "268m/s",
            "b"       : "400m/s",
            "c"       : "355m/s",
            "d"       : "343m/s",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "d",
    },
    "Questão 08"      : {
        "pergunta"    : "Baseado em evidências científicas, qual grupo estariam classificados os dinossauros?",
        "opcão"       : {
            "a"       : "Anfíbios",
            "b"       : "Aves",
            "c"       : "Répteis",
            "d"       : "Mamíferos",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "b",
    },
    "Questão 09"      : {
        "pergunta"    : "Em que estado brasileiro nasceu o cantor e compositor Raul Seixas?",
        "opcão"       : {
            "a"       : "Rio de Janeiro",
            "b"       : "Pernambuco",
            "c"       : "São Paulo",
            "d"       : "Bahia",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "d",
    },
    "Questão 10"      : {
        "pergunta"    : "Qual elemento químico está logo acima do Crômio (Cr) na tabela periódica?",
        "opcão"       : {
            "a"       : "Nióbio(Nb)",
            "b"       : "Paládio(Pd)",
            "c"       : "Irídio(Ir)",
            "d"       : "Alumínio(Al)",
            "e"       : "Nenhuma das respostas",
        },
        "resposta"    : "e",
    },
}

res_certo = 0

for pk, pv in questoes.items():
    print(f"{pk}: {pv['pergunta']}")

    print()
    for qk, qv in pv["opcão"].items():
        print(f"[{qk}]: {qv}")
    print()
    res_user = input("Digite sua resposta: ")
    print()
    while res_user not in pv["opcão"].keys():
        res_user = input("Digite a letra da opção: ")

    if res_user == pv["resposta"]:
        res_certo += 1
    else:
        if res_certo > 0:
            res_certo -= 1

    print()

qt_perguntas = len(questoes)
porc_acerto = int(res_certo / qt_perguntas * 100)
print(f"Você teve uma média de {porc_acerto}%")
print()
