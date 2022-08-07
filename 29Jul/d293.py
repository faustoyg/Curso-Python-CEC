lista1=[]
lista2=[]
lista = ["R1", "R2", "R3", "R4", "S1", "S2", "S3"]

for item in lista:
    if "R" in item:
        lista1.append(item)
#    elif "S" in item:
    else:
        lista2.append(item)

print(lista1)
print(lista2)