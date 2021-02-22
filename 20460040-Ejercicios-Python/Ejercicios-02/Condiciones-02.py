#20460040 Lilia Soto Llamas

dividendo = int(input("\nIngrese el dividendo: "))
divisor = 0
while divisor == 0:
    divisor = int(input("Ingrese el divisor, no puede ser igual a cero: "))

if dividendo%divisor == 0:
    print (f"\nLa división es exacta. El resultado es {dividendo//divisor}")
else: 
    print (f"\nLa división no es exacta. El resultado es {dividendo/divisor}")