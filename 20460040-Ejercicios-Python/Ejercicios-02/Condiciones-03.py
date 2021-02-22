#20460040 Lilia Soto Llamas

num_1 = int(input("\nIngrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
print()
if num_1 < num_2:
    print(f"Menor: {num_1}\nMayor: {num_2}")
elif num_1 > num_2:
    print(f"Menor: {num_2}\nMayor: {num_1}")
else:
    print("Son iguales")