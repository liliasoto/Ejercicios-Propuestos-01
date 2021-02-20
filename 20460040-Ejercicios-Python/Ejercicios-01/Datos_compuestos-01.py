#20460040 Lilia Soto Llamas

def separar(lista):
    lista_par = []
    lista_impar = []
    for var in range(len(lista)):
        if int(lista[var])%2 == 0:
            lista_par.append(lista[var])
        if int(lista[var])%2 != 0:
            lista_impar.append(lista[var])
    return lista_par, lista_impar

lista_prueba = [12, 13, 2, 3 ,1 , 41, 29]
print(f"Lista para hacer una prueba del programa: {lista_prueba}")
tupla = separar(lista_prueba)
print(f"Lista con números pares: {tupla[0]}")
print(f"Lasta con números impares: {tupla[1]}")

op = ""
while op != "2":
    op = input("Menú\n1. Separar una lista\n2. Salir\nElija una opción del menú: ")
    if op == "1":
        nueva_lista = []
        len_lista = input("¿Cuántos números va a ingresar en la lista? ")
        for i in range(int(len_lista)):
            nueva_lista.append(input(f"Ingrese el número para la posición {i}: "))   
        nueva_tupla = separar(nueva_lista)
        print(f"Lista con números pares: {nueva_tupla[0]}")
        print(f"Lasta con números impares: {nueva_tupla[1]}")           
    if op == "2":
        print("Ha decidido salir, gracias por usar este programa :)")  


            