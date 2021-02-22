#20460040 Lilia Soto Llamas 

num = int(input("\n¿Cuántos números se van a introducir?: "))
suma = 0
may = 0
men = 120394**123344
for i in range(num):
    nu = int(input(f"Ingrese el número {i+1}: "))
    if nu > may:
        may = nu
    if nu < men:
        men = nu
    suma += nu
media = suma/num
print(f"El número mayor es: {may}\nEl número menor es: {men}\nLa media aritmética es: {media}") 
    
    
        