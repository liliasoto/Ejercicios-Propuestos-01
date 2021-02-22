#20460040 Lilia Soto Llamas

num = int(input("\n¿Cuántos números se van a introducir?: "))
lista = []
suma = 0
for i in range(num):
    nu = int(input(f"Ingrese el número {i+1}: "))
    lista.append(nu)
    if nu < 0:
        suma += 1
print(f"\nNúmeros ingresados: {lista}\nNúmero impares ingresados: {suma}")
    