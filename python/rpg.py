# Calcula pontos e leveis no rpg.

print("LEVEL E EXPERIÊNCIA:")
print("=" *20)
lvlatual = int(input("Level: "))
xp = int(input("Exp: "))
grau = (int(input("Grau: ")))
print("=" *20)
print("RESULTADO:")
print("-" *20)
lvlfinal = lvlatual
'''
No sistema, se a experiência ganha pelo jogador for igual ao seu level, ele sobe de nível.
E para cada nível que ele sobe, ganha 1 ponto multiplicado pelo seu grau."
'''
if(lvlatual > xp):
	print("Você não tem exp pra upar. Seu burro!!!")
else:
	while(lvlatual <= xp):
		xp = xp - lvlatual
		lvlatual = lvlatual +1
	print("Level atual: ", lvlatual)
	print("Exp que sobrou: ",   xp)
	print("Pontos Ganhos:", (lvlatual - lvlfinal) * grau)
	print("-" *20)
