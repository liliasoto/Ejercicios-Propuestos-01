#20460040 Lilia Soto Llamas

def area_rectangulo (base, altura):
    area = base*altura
    return area

print(f"Área de un rectángulo de 15 de base y 10 de altura: {area_rectangulo(15,10)}", end="\n")

op = ""
while op != "2":
    op = input("Menú\n1. Obtener el área de un rectángulo\n2. Salir\nElija una opción del menú: ")
    if op == "1":
        nueva_base = input ("Ingrese la medida de la base: ")
        nueva_altura = input ("Ingrese la medida de la altura: ")
        print(f"El área es {area_rectangulo(int(nueva_base), int(nueva_altura))}")
    if op == "2":
        print("Ha decidido salir, gracias por usar este programa :)")    
