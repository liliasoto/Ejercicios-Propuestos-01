#20460040 Lilia Soto Llamas
print()
print("Suma de tiempos")
print()

hora_1 = 0
min_1 = 0
seg_1 = 0
hora_2 = 0
min_2 = 0
seg_2 = 0
min_3 = 0
hora_3 = 0

print("Primer tiempo")
seg_1 = input("Ingrese los segundos (00 - 59): ")
min_1 = input("Ingrese los minutos (00 - 59): ")
hora_1 = input("Ingrese las horas: ")
print()
print("Segundo tiempo")
seg_2 = input("Ingrese los segundos (00 - 59): ")
min_2 = input("Ingrese los minutos (00 - 59): ")
hora_2 = input("Ingrese las horas: ")

suma_seg = int(seg_1) + int(seg_2)
min_3 = suma_seg//60
nue_s = suma_seg%60

suma_min = int(min_1) + int(min_2) + int(min_3)
hora_3 = suma_min//60
nue_m = suma_min%60

nue_h = int(hora_1) + int(hora_2) + int(hora_3)

tiempo_1 = (int(hora_1), int(min_1), int(seg_1))
tiempo_2 = (int(hora_2), int(min_2), int(seg_2))
suma = (nue_h, nue_m, nue_s)

print()
print(f"Tiempos ingresados:\nhrs, min, seg {tiempo_1}\nhrs, min, seg {tiempo_2}\n\nSuma formato hrs, min, seg: {suma}")
print()
print("Gracias por utilizar este programa")


