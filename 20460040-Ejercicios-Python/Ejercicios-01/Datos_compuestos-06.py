#20460040 Lilia Soto Llamas

print()
print("Día siguiente")
dia = input("Ingrese el día: ")
mes = input("Ingrese el mes 1 - 12: ")
año = input("Ingrese el año: ")
print()

def dia_siguiente_e():
    if ((mes == "1") or (mes == "3") or (mes == "5") or (mes == "7") or (mes =="8") or (mes == "10")): 
        nue_año = int(año)
        if dia == "31":
            nue_mes = int(mes) + 1
            nue_dia = 1
        else: 
            nue_mes = int(mes)
            nue_dia = int(dia) + 1
    elif mes == "2":
        nue_año = int(año)
        if dia == "28":
            if int(año) % 4 == 0:
                if int(año) % 100 == 0:
                    if int(año) % 400 == 0:
                        nue_mes = int(mes)
                        nue_dia = int(dia) + 1
                    else:
                        nue_mes = int(mes) + 1
                        nue_dia = 1
                else: 
                    nue_mes = int(mes)
                    nue_dia = int(dia) + 1
            else:
                nue_mes = int(mes) + 1
                nue_dia = 1
        elif dia == "29":
            nue_mes = int(mes) + 1
            nue_dia = 1
        else:
            nue_mes = int(mes)
            nue_dia = int(dia) + 1
    elif ((mes == "4") or (mes == "6") or (mes == "9") or (mes == "11")):
        nue_año = int(año)
        if dia == "30":
            nue_mes = int(mes) + 1
            nue_dia = 1
        else: 
            nue_mes = int(mes)
            nue_dia = int(dia) + 1
    elif mes == "12":
        if dia == "31":
            nue_año = int(año) + 1
            nue_mes = 1
            nue_dia = 1
        else:
            nue_año = int(año)
            nue_mes = int(mes)
            nue_dia = int(dia) + 1
    print(f"El día siguiente es: {nue_dia}/{nue_mes}/{nue_año}")    

dia_siguiente_e()    



