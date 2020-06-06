import random
"""
Jogo de forca feito em Python
"""
sair = "y"
while True:
    
    # Pergunta se o usuário deseja continuar jogando ou sair
    if sair == 'y':
        pass
    elif sair == 'n':
        break
    else:
        sair = input("Digite somente 'y' ou 'n': ")
        continue

    # Palavras aleatórias que serão escolhidas para o jogo.
    palavra = "arroz feijao batata macarrao tempero queijo caldo goiaba abacate tomate papel livro sorvete casa estudante biblioteca teclado frango estupido dicionario paralelepipedo leite vaca esperto gambiarra mouse monitor computador escola internet soldado sol ovo eu ela sim nao pao cao rio palavra tempestade aluguel predio telescopio milionario fone cloro bicicleta astronauta lua doutor medico mar cortina ceu montanha carro refrigerante prato rotina sentimento amor paz uniao sal pimenta espirito copo agua solidariedade farmacia sindrome medo nos sempre convidado luz garrafa hipopotamo sociedade"

    lista = palavra.split(" ")
    secreto = random.choice(lista)
    digitadas = []
    chances = 0
    quant_letras = len(secreto)

    # Seleciona quantas chances o usuario tem de acordo com a quantidade de letras da palavra escolhida.
    if quant_letras <= 4:
        chances = 3
    elif quant_letras >= 5 and quant_letras <= 7:
        chances = 5
    else:
        chances = 7

    print("-"*30)
    print()
    print(f"Bem vindo ao jogo da Força.\nVocê tem {chances} chances para acertar uma palavra gerada aleatoriamente. \nNenhuma das letras contém pontuação, para ficar mais fácil de adivinhar.\nBoa Sorte!")
    print()
    print("-"*30)
    while True:
        
        # Bloco de código para forçar o usuário a digitar somente letras e somente uma por vez.
        letra = input("Digite uma letra para tentar adivinhar a palavra secreta: ")
        if not letra.isalpha():
            print()
            print("Digite somente letras!")
            print()
            continue
        if len(letra) > 1:
            print()
            print("Você só pode digitar uma letra!")
            print()
            continue

        #Chances que o usuário tem para acertar a palavra secreta.
        if letra not in secreto:
            chances -= 1
            if chances == 0:
                print()
                print(f"Suas chances acabaram, você perdeu. A palavra era {secreto}.")
                print()
                break

        print()
        print(f"Você ainda tem {chances} chances ao total")
        
        
        # Adiciona as letras digitadas na variável "digitadas" e exclui as erradas.
        digitadas.append(letra)

        if letra in secreto:
            print()
            print(f'Você acertou uma letra: {letra}.')
            print()
        else:
            print()
            print(f'A letra que você digitou "{letra}" está ERRADA!')
            print()
            digitadas.pop()
        
        # Ocultando e revelando a letra secreta.
        temp = ""
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                temp += letra_secreta
            else:
                temp += "-"
        # Para quando o usuário conseguir completar a frase.
        if temp == secreto:
            print()
            print(f"Você acertou a palavra! Parabéns!!! A palavra secreta era: {secreto}")
            print()
            print()
            break
        else:
            print()
            print(f"~~> {temp}")
            print()
            print()

    # Pergunta se o usuário deseja continuar jogando ou sair
    sair = input("Deseja jogar outra vez? Digite 'y' para continuar e 'n' para sair: ")
    if sair == True:
        continue

















