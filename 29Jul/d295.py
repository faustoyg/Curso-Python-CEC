x = input("ingrese un numero para contar: ")
x = int(x)
contador = 1

#while True:
while contador <= x:
    print(contador, end=" ")
    contador += 1
    #contador += contador
    if contador>x:
        break
