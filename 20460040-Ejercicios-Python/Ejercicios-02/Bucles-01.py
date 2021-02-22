#20460040 Lilia Soto Llamas

lista_numeros = []
lista_pares = []
lista_impares = []
lista_primos = []
lista_noprimos = []

def clasifica(lista):
    suma = 0
    for i in lista_numeros:
        if i%2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
        if primo(i) == True:
            lista_primos.append(i)
        if primo(i) == False: 
            lista_noprimos.append(i)
        suma += i
    print()
    print(f"Números pares: {lista_pares}\nNúmeros impares: {lista_impares}\nNúmeros primos: {lista_primos}\nNúmeros no primos: {lista_noprimos}\nSuma: {suma}")

def primo(num):
    if num<=1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

print("\nIngresa seis números a continuación:")
for i in range (6):
    lista_numeros.append(int(input(f"Ingresa el número {i+1}: ")))

clasifica(lista_numeros)


