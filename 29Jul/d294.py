for A in range(10,1,-2):
    print(A)


devices = ["R1","R2","R3","S1","S2"]
for a in devices:
    print(a)

switch=[]
router=[]
lista = ["R1", "R2", "R3", "R4", "S1", "S2", "S3"]

for item in lista:
    if "R" in item:
        switch.append(item)
#    elif "S" in item:
    else:
        router.append(item)
print(switch)
print(router)

for j in "amigos":
    print("dame una", [j])
print("AMIGO!")
#
print("Comienzo")
for i in range(0,10,2):
    print("hola ", end="")
print()
print("final")
#
veces = int(input("cuantos saludos? "))
for i in range(1, veces+1, 1):
    print("hola ", end="")
print()
print("adios")