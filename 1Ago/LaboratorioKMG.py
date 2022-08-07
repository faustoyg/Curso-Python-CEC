def l100kmtompg(litros):
    k1 = 1.609344
    k2 = 1 / 3.785411784
    return(100/(litros*k1*k2))

def mpgtol100km(litros):
    k1 = 1.609344
    k2 = 1 / 3.785411784
    return(100/(litros*k1*k2))

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))

print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

