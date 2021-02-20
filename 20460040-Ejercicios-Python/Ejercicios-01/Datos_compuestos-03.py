#20460040 Lilia Soto Llamas 

op = ""
while op != "3":
    op = input("Menú\n1. Ordenar los números de la lotería primitiva\n2. Invertir una lista con números del 1 al 10\n3. Salir\nElija una opción del menú: ")
    if op == "1":
        lista = []
        len_lista = input("¿Cuántos números de la lotería primitiva va a ingresar en la lista? ")
        for i in range(int(len_lista)):
            lista.append(input(f"Ingrese el número para la posición {i}: "))
        print(f"Lista original: {lista}")    
        lista.sort()
        print(f"Lista ordenada de menor a mayor: {lista}") 
    if op == "2":
        lista_1_10 = [1,2,3,4,5,6,7,8,9,10]
        print(f"Lista original: {lista_1_10}")
        lista_1_10.sort(reverse=True)
        print(f"Lista ordenada de mayor a menor: {lista_1_10}")
    if op == "3":
        print("Ha decidido salir, gracias por usar este programa :)")