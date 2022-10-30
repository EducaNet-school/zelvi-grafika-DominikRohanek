print("zadej liche cislo")
x = int(input("zde:"))
if x % 2 == 0:
    x += 1
sez = [x]
for i in range(9):
    x += 2
    sez.append(x)
print(sez)

#jeste chybi vypocet prumeru 

