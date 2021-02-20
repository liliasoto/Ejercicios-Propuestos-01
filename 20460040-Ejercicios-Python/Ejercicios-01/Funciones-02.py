#20460040 Lilia Soto Llamas
import math

def area_circulo(radio):
    area = math.pi*(radio**2)
    return area

print(f"El área de un círculo de 5 de radio es: {area_circulo(5)}")

op = ""
while op != "2":
    op = input("Menú\n1. Obtener el área de un círculo\n2. Salir\nElija una opción del menú: ")
    if op == "1":
        nuevo_radio = input ("Ingrese la medida del radio: ")
        print(f"El área es {area_circulo(int(nuevo_radio))}")
    if op == "2":
        print("Ha decidido salir, gracias por usar este programa :)") 