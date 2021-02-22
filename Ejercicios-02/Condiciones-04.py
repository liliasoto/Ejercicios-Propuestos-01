#20460040 Lilia Soto Llamas

num_1 = int(input("\nIngrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
if num_1 < num_2:
    if num_2 % num_1 == 0:
        print(f"{num_2} sí es múltiplo de {num_1}")
    else: 
        print(f"{num_2} no es múltiplo de {num_1}")
elif num_1 > num_2:
    if num_1 % num_2 == 0:
        print(f"{num_1} sí es múltiplo de {num_2}")
    else: 
        print(f"{num_1} no es múltiplo de {num_2}")
else:
    print(f"{num_1} sí es múltiplo de {num_2}")