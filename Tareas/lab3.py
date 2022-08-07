# -*- coding: utf-8 -*-

def isYearLeap(anio):
    if (anio %400 == 0) and (anio %100 ==0):
        Bisiesto = True
    elif (anio % 4 ==0) and (anio % 100 != 0):
        Bisiesto = True
    else:
        Bisiesto = False
    return Bisiesto


def dayOfYear(anio, mes, dia):
    if isinstance(anio, str)== True or isinstance(mes, str)== True or isinstance(dia, str)== True:
        numdia = "None"
       
    elif mes < 0 or mes >12:
        numdia = "Mes no valido"
    else:
        if isYearLeap(anio) == True and mes >1:
            b =1
        else:
            b=0
        
        dmes = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334,0]
        acc = dmes[mes-2]
        numdia = acc+dia+b
    return numdia
    

print(dayOfYear(1900, "julio", 31))
print(dayOfYear("dos mil", "julio", 31))
print(dayOfYear(2000, 15, 31))
print(dayOfYear(2000, 1, 1))
print(dayOfYear(2000, 12, 31))
print(dayOfYear(1900, 1, 1))
print(dayOfYear(1900, 12, 31))