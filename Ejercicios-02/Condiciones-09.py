#20460040 Lilia Soto Llamas

dis = int(input("\nIngrese una distancia en centímetros: "))

if dis <= 0:
    print("La distancia tiene que ser mayor a 0.")
else:
    km = dis // 100000
    m = (dis % 100000) // 100
    cm = (dis % 100000) % 100
    print(f"{dis} centímetros equivalen a: {km} km {m} m {cm} cm")