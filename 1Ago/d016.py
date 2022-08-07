def tupla(*args):
    for a in args:
        print(a)

tupla(5)

tupla(1,2,3)

def datos(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])

datos(nombre='Fausto', edad=37)
