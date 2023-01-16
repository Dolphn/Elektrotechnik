from math import sqrt
from math import pi
from math import sin


def capacity(um, f, ug):
    return (um/(2*pi*(f*1000)*sqrt(ug*ug-um*um)*50))*1000*1000


print(capacity(0.68, 1, 4))
print(capacity(1.25, 2, 4))
print(capacity(1.7, 3, 4))
print(capacity(2.5, 5, 4))

def reactance(um, i):
    return (4 - um)/(i/1000)

#print(reactance(0.68, 13.6))
#print(reactance(1.25, 25))
#print(reactance(1.7, 34))
#print(reactance(2.5, 50))


def impedance(um, i, phi):
    return reactance(um, i) / sin(phi)


print(impedance(0.68, 13.6, 1.3823))
print(impedance(1.25, 25, 1.256637))
print(impedance(1.7, 34, 1.1309734))
print(impedance(2.5, 50, 0.879646))