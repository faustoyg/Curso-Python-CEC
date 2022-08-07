# -*- coding: utf-8 -*-

def isYearLeap(anio):
    if (anio %400 == 0) and (anio %100 ==0):
        Bisiesto = True
    elif (anio % 4 ==0) and (anio % 100 != 0):
        Bisiesto = True
    else:
        Bisiesto = False
    return Bisiesto

#anio = 2000
#anio = int(input("Ingresa un año: "))
#print(isYearLeap(anio))


def daysInMonth(anio, mes):
    Bisi = isYearLeap(anio)
    if mes == 2 and Bisi == True:
       dm = 29
    elif mes == 2 and Bisi == False:
       dm = 28
    elif mes== 4 or mes== 6 or mes== 9 or mes== 11:
        dm = 30
    else:
        dm = 31
    return dm



testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")




