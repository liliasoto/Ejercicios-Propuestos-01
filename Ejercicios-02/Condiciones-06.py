#20460040 Lilia Soto llamas

print("\nA continuación escribe los coeficientes de la siguiente ecuación (ax + b = 0)")
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
print()
if a == b == 0:
    print("Tiene soluciones infinitas.")
elif a == 0:
    print("No tiene solución.")
else: 
    print(f"El resultado es: x = {-b/a}")
