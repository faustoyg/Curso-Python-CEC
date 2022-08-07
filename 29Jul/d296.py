while True:
    print("\n")
    x = input("Ingrese un numero para contar: ")
    if x == "s" or x == 'salir':
        break
    x = int(x)
    y = 1
    while True:
        print(y, end=" ")
        y = y+1
        if y>x:
            break