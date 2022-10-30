sez = [0, 1]
sez2 = [0, 1]
print("zadej pocet cisel kolik chces z Fibonnaciho rady. ")
p = int(input("zde:"))
for i in range(p-2):
    i = sez[sez2[0]] + sez[sez2[1]]
    sez2[0] += 1
    sez2[1] += 1
    sez.append(i)
print(sez)

#Pozor, rada nezacina od 0
