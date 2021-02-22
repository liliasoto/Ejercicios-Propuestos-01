# 20460040 Lilia Soto Llamas 

num = int(input("\nIngrese un número entero mayor a 0: "))
divisores = []
for i in range (1,(num+1)):
    if num % i == 0: 
        divisores.append(i)
print(f"Divisores de {num}: {divisores}")