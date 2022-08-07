lista =[]
file = open("devices.txt")
for item in file:
    item = item.strip("Cisco").strip()
    print(item)
    lista.append(item)
file.close()
print(lista)