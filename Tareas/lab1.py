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

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
