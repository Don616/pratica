"""
Programa que converte algum número digitado em hora, minuto e segundo respectivamente.
Sujeito a melhorias.
"""

segundo = 0
minuto = 0
hora = 0

time = (input("Digite algum número, que lhe direi quanto tempo dá: "))

# Conversão do número digitado, para minuto, segundo ou hora.    
if time.isnumeric():
    time = int(time)
    while time >= 60:
        time = time -60
        minuto = minuto +1
        while minuto >= 60:
            minuto = minuto -60
            hora = hora +1
    segundo = time
    print("{}:{}:{}".format(hora, minuto, segundo))
else:
    print("Você não digitou um número... Execute o programa novamente.") 

