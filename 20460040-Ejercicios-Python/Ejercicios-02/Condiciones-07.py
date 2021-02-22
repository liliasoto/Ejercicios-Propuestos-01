#20460040 Lilia Soto Llamas
import math
def fun(a, b, c):
    valor_re = b * b - 4 * a * c
    if a == b == c:
        print("Todos los números son solución.")
    elif a == b == 0:
        print("Sin solución.")
    elif a == 0:
        print(f"Única solución: {-c/b}")
    elif valor_re <0:
        print("Sin solución real.")
    elif valor_re == 0:
        print(f"Única solución: {- b / (2 * a)}")
    else:
        print(f"Dos soluciones: {(-b + math.sqrt((b**2) - (4*a*c)))/(2*a)} y {(-b - math.sqrt((b**2) - (4*a*c)))/(2*a)}")

print("\nA continuación ingrese los coeficientes de la ecuación de segundo grado ax2 + bx + c = 0")
v_a = int(input("Ingrese el valor de a: "))
v_b = int(input("Ingrese el valor de b: "))
v_c = int(input("Ingrese el valor de c: "))
print()

fun(v_a, v_b, v_c)