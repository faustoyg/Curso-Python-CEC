
#lambda
a = lambda x,y: x+y
print(a(1,5))

revertir = lambda cadena: cadena[::-1]
print(revertir("prueba"))

impar = lambda num:num%2 !=0
print(impar(33))

seq= ['palabra','gato','perro','raton','pato']
print(list(filter(lambda word: word[1]=='a',seq)))