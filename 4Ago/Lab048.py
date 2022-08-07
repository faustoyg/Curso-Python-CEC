lmin = -10
lmax = 20

def readint( prompt, lmin, lmax):
    if prompt <= lmin or prompt >= lmax:
        msj = "El valor no esta en el rango permitido"
    elif prompt >= lmin and prompt <= lmax :
        msj = ("El numero es: {}").format(prompt)
    print(msj)

ex = ("Ingresa un numero de {} a {} ").format(lmin, lmax)
n= input(ex)
try:
    prompt = int(n)
except ValueError:
    print("Error en el ingreso")
    n= input("Ingresa un numero ")
    prompt = int(n)
    #exit()

readint(prompt,  lmin, lmax)