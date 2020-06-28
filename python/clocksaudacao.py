while True:
    hora = int(input("Que horas são no momento? "))
    if hora < 0 or hora > 23:
        print("Digite uma hora válida!")
        continue
    break
while True:
    minuto = int(input("Quantos minutos são? "))
    if minuto < 0 or minuto > 59:
        print("Digite um minuto válido!")
        continue
    break

def timer(hora, minuto):
    if hora >= 6 and minuto >= 0 and hora <= 11 and minuto <= 59:
        return "Está de Manhã"
    elif hora >= 12 and minuto >=0 and hora <=17 and minuto <= 59:
        return "Está de Tarde"
    elif hora >= 18 and minuto >=0 and hora <=23 and minuto <= 59:
        return "Está de Noite"
    else:
        return "Está de Madrugada, vá dormir!"


print(timer(hora, minuto))