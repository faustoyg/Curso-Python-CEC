print("Serie de Fibonacci")

def PrintFibonacci(n):
    a = 0
    b = 1 #valores iniciales de la serie

    print(a, b, end=" ") #numeros iniciales

    n -= 2 #reduccion del tamano en 2 porque ya se imprimio 0 y 1

    # Lazo hasta llegar a cero 0.
    while n > 0:
        # Siguiente numero de Fibonacci
        print(a + b, end=" ")

        # Actualizacion de la primera y segunda variable para encontrar el proximo numero.
        temp = b
        b = a + b
        a = temp

        # Disminuir la logitud que determina los numero de Fibonacci
        n -= 1
#def fib(m)
