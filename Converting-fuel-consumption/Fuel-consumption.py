def l100kmtompg(liters):
    gallons = liters / 3.785411784
    hundredkilometers = 62.137119223733
    answer = hundredkilometers / gallons
    return answer

def mpgtol100km(miles):
    hundredkilometers = 62.137119223733
    km = hundredkilometers / miles
    answerkm = km * 3.785411784
    return answerkm


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))