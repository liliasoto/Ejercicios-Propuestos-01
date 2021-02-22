#20460040 Lilia Soto Llamas

lista = []
op = 0
while op != 2:
    print("\n----------------Menú----------------\n1.- Generar nuevo número de control\n2.- Salir")
    op = int(input("Elija una opción del menú: "))
    print()
    if op == 1:
        print("Generar nuevo número de control")
        año = int(input("Ingrese el año en el que el alumno ingresó: "))
        campus = int(input("Ingrese el campus al que pertenece el alumno: "))
        pri = (año % 100) * 1000000
        seg = (campus % 100) * 10000
        nocontrol = pri + seg + 1
        esta = True
        while esta == True:
            if nocontrol in lista:
                nocontrol += 1
                esta = True
            else:
                control = nocontrol + 1
                esta = False
        else:
            control = nocontrol
        lista.append(control)
        print(f"Número de control: {control}")
    elif op == 2:
        print("Ha decidido salir, gracias por utilizar este programa.")
    else:
        print("Elija una opción del menú.")
