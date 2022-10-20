sez = [1, 2, 3, 4, 5]
print("zadej o kolik mist se seznam zrotuje kladne cislo je doleva zaporne doprava")
x = int(input("zde:"))
sez = sez[x:] + sez[:x]
print(sez)
