#201460040 Lilia Soto Llamas

cartas = []
#Cartas de corazones
for i in range(1,14):
    nue_tu = (i, "Co")
    cartas.append(nue_tu)

for i in range(1,14):
    nue_tu = (i, "Di")
    cartas.append(nue_tu)

for i in range(1,14):
    nue_tu = (i, "Tr")
    cartas.append(nue_tu)

for i in range(1,14):
    nue_tu = (i, "Pi")
    cartas.append(nue_tu)
    

def poker(carta_1,carta_2,carta_3,carta_4):
    pass

print()
print("Elija 4 números del 0 al 51. Estas serán sus cartas.")
pri = input("Primer número: ")
seg = input("Segundo número: ")
ter = input("Tercer número: ")
cua = input("Cuarto número: ")
cin = input("Quinto número: ")

n1 = cartas[int(pri)][0]
n2 = cartas[int(seg)][0]
n3 = cartas[int(ter)][0]
n4 = cartas[int(cua)][0]
n5 = cartas[int(cin)][0]

print()

if (n1 == n2 == n3 == n4) and (n1 != n5):
    print("¡Tienes un póker! :)")
elif (n1 == n2 == n3 == n5) and (n1 != n4):
    print("¡Tienes un póker! :)")
elif (n1 == n2 == n5 == n4) and (n1 != n3):
    print("¡Tienes un póker! :)")
elif (n1 == n5 == n3 == n4) and (n1 != n2):
    print("¡Tienes un póker! :)")
elif (n5 == n2 == n3 == n4) and (n5 != n1):
    print("¡Tienes un póker! :)")
else:
    print("No tienes un póker :(")

print()
print("Estas son sus cartas: ")
print(f"{cartas[int(pri)]}, {cartas[int(seg)]}, {cartas[int(ter)]}, {cartas[int(cua)]}, {cartas[int(cin)]}")
