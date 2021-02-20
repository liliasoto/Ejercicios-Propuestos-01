#20460040 Lilia Soto Llamas

print()
print("Día siguiente")
dia = input("Ingrese el día: ")
mes = input("Ingrese el mes escribiendo las 3 primeras letras, siendo la primera mayúscula. Ene, Feb, etc...: ")
año = input("Ingrese el año: ")
print()

def dia_siguiente_t():
    if mes == "Ene": 
        nue_año = int(año)
        if dia == "31":
            nue_mes = "Feb"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Mar": 
        nue_año = int(año)
        if dia == "31":
            nue_mes = "Abr"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "May": 
        nue_año = int(año)
        if dia == "31":
            nue_mes = "Jun"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Jul": 
        nue_año = int(año)
        if dia == "31":
            nue_mes = "Ago"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes =="Ago": 
        nue_año = int(año)
        if dia == "31":
            nue_mes = "Sep"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Oct": 
        nue_año = int(año)
        if dia == "31":
            nue_mes = "Nov"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Feb":
        nue_año = int(año)
        if dia == "28":
            if int(año) % 4 == 0:
                if int(año) % 100 == 0:
                    if int(año) % 400 == 0:
                        nue_mes = mes
                        nue_dia = int(dia) + 1
                    else:
                        nue_mes = "Mar"
                        nue_dia = 1
                else: 
                    nue_mes = mes
                    nue_dia = int(dia) + 1
            else:
                nue_mes = "Mar"
                nue_dia = 1
        elif dia == "29":
            nue_mes = "Mar"
            nue_dia = 1
        else:
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Abr":
        nue_año = int(año)
        if dia == "30":
            nue_mes = "May"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Jun":
        nue_año = int(año)
        if dia == "30":
            nue_mes = "Jul"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Sep":
        nue_año = int(año)
        if dia == "30":
            nue_mes = "Oct"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Nov":
        nue_año = int(año)
        if dia == "30":
            nue_mes = "Dic"
            nue_dia = 1
        else: 
            nue_mes = mes
            nue_dia = int(dia) + 1
    elif mes == "Dic":
        if dia == "31":
            nue_año = int(año) + 1
            nue_mes = "Ene"
            nue_dia = 1
        else:
            nue_año = int(año)
            nue_mes = mes
            nue_dia = int(dia) + 1
    print(f"El día siguiente es: {nue_dia}/{nue_mes}/{nue_año}")

dia_siguiente_t()