#20460040 Lilia Soto Llamas

op = input("\nSi quiere calcular el área de un triángulo escriba \"T\" o \"t\"\nSi quiere calcular el área de un círculo escriba \"C\" o \"c\"\n¿Qué desea hacer?: ")

if op == "T" or op == "t":
    base = float(input("Ingrese la medida de la base: "))
    altura = float(input("Ingrese la medida de la altura: "))
    area = (base*altura)/2
    print(f"El área del triángulo es: {area}")
if op == "C" or op == "c":
    radio = float(input("Ingrese la medida del radio: "))
    area = (radio**2)*3.141592
    print(f"El área del círculo es: {area}")
