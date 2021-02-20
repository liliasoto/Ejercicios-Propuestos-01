#20460040 Lilia Soto Llamas


op = ""
while op != "2":
    op = input("Menú\n1. Crear una lista de materias\n2. Salir\nElija una opción del menú: ")
    if op == "1":
        lista = []
        len_lista = input("¿Cuántos materias va a ingresar en la lista? ")
        for i in range(int(len_lista)):
            lista.append(input(f"Ingrese la materia para la posición {i}: ")) 
        print(f"La lista es: {lista}")
    if op == "2":
        print("Ha decidido salir, gracias por usar este programa :)")