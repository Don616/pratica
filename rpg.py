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
