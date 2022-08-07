# try:
#     print("1")
#     x=1/0
#     print("2")
# except:
#     print("Error")
#     print("3")
try:
    x=int(input("Ingrese numero: "))
    y = 1/x
    print(y)
except ArithmeticError:
    print("Division para cero")
except ZeroDivisionError:
    print("No se puede dividir para cero")

except ValueError:
    print("Ingresar un numero entero")
except:
    print("Algo salio mal")
print("Fin")