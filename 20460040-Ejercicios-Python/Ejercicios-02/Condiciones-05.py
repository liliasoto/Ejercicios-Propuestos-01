#20460040 Lilia Soto Llamas

num_1 = int(input("\nIngrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))
print()
if (num_1 == num_2) and (num_2 == num_3):
    print("Los tres números son iguales")
elif ((num_1 == num_2) and (num_1 != num_3)) or ((num_1 == num_3) and (num_1 != num_2)) or ((num_2 == num_3) and (num_2 != num_1)):
    print("Hay dos números iguales")
else: 
    print("Los tres números son distintos")