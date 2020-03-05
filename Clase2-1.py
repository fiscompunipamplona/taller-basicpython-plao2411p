import math as mt
#Pedro Luis Artunduaga Ortiz
print ("Ejercicio clase 2 transformada de Lorentz")
di = input ("Ingrese la distancia en ly --> ")
vi = input ("Ingrese la velocidad como fracion de C --> ")
d = float(di)
v = float (vi)
C = 3e8 #m/s
ly= 9.46e15 #m
v1 = v*C #m/si #velocidad de la nave(no fraccion)
d=d*ly #distancia en metros
roh= 1/mt.sqrt(1-v**2)
t= d/v1 #m/s
tnav = roh*(t-((v1*d)/C**2))
print ("Distancia de la tierra al planeta --> ",d,"m") #en metros
print ("El tiempo desde la tierra es --> ", t,"s")
print ("El tiempo desde la nave es --> ",tnav,"s")

