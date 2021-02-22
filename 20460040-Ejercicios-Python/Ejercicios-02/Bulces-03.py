#20460040 Lilia Soto Llamas

num = int(input("\n¿Cuántos números se van a ingresar? "))
num_1 = int(input(f"Ingrese el número 1: "))
for i in range(2,(num+1)):
    nume = int(input(f"Ingrese el número {i}, mayor a {num_1}: "))
    if nume < num_1:
        print(f"¡{nume} no es mayor que {num_1}!")
    
