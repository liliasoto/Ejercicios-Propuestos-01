#20460040 Lilia Soto Llamas

def relacion(a,b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0

print(f"Relación entre 5 y 10: {relacion(5,10)}")
print(f"Relación entre 10 y 5: {relacion(10,5)}")
print(f"Relación entre 5 y 5: {relacion(5,5)}")

op = ""
while op != "2":
    op = input("Menú\n1. Obtener la relación entre dos números\n2. Salir\nElija una opción del menú: ")
    if op == "1":
        nuevo_a = input ("Ingrese el primer número: ")
        nuevo_b = input ("Ingrese el segundo número: ")
        print(f"La relación entre {nuevo_a} y {nuevo_b} es {relacion(int(nuevo_a), int(nuevo_b))}")
    if op == "2":
        print("Ha decidido salir, gracias por usar este programa :)") 