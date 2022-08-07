
file = open("devices.txt", mode = 'a')
while True:
    newItem = input("Ingrese nuevo device: ")
    if newItem == "exit":
        print("All done")
        exit()
    file.write(newItem + "\n")
file.close()
