#20460040 Lilia Soto Llamas

def intermedio(a,b):
    inter = (a+b)/2
    return inter

print(f"El punto intermedio entre -12 y 24 es: {intermedio(-12,24)}")

op = ""
while op != "2":
    op = input("Menú\n1. Obtener el punto intermedio entre dos números\n2. Salir\nElija una opción del menú: ")
    if op == "1":
        nuevo_a = input ("Ingrese el primer número: ")
        nuevo_b = input ("Ingrese el segundo número: ")
        print(f"El punto intermedio entre {nuevo_a} y {nuevo_b} es {intermedio(int(nuevo_a),int(nuevo_b))}")
    if op == "2":
        print("Ha decidido salir, gracias por usar este programa :)") 