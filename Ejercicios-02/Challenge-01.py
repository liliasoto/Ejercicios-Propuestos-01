#20460040 Lilia Soto Llamas

print("\n¿Qué día de la semana es?")
dia = int(input("Ingrese un día: "))
mes = int(input("Ingrese un mes 1-12: "))
año = int(input("Ingrese un año: "))
print()

if año <= 1582:
    print("La fecha debe ser posterior al año 1582.")
else:
    A = (14 - mes) // 12
    B = año - A
    C = mes + (12 * A) - 2 
    D = B // 4
    E = B // 100
    F = B // 400
    G = ( 31 * C ) // 12
    H = dia + B + D - E + F + G
    I = H % 7
    if I == 0:
        print(f"{dia}/{mes}/{año} cae en Domingo.")
    if I == 1:
        print(f"{dia}/{mes}/{año} cae en Lunes.")
    if I == 2:
        print(f"{dia}/{mes}/{año} cae en Martes.")
    if I == 3:
        print(f"{dia}/{mes}/{año} cae en Miércoles.")
    if I == 4:
        print(f"{dia}/{mes}/{año} cae en Jueves.")
    if I == 5:
        print(f"{dia}/{mes}/{año} cae en Viernes.")
    if I == 6:
        print(f"{dia}/{mes}/{año} cae en Sábado.")

