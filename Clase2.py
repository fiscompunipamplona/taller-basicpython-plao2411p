import math as mt
from numpy.random import rand
print ("Conversion de polares a cartesianas")
r = input ("Ingrese el valor de r --> ")
z = input ("Ingrese el valor del angulo en grados --> ")
rt = float(r)
zt = float(z)
zt = (zt*mt.pi)/180
x= rt* mt.cos(zt)
y= rt* mt.sin(zt)
print("En coordenadas cartesianas")
print ("x=",x)
print ("y=",y)
