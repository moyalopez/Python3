##jair
##calcular la edad actual de una persona
##previamente
##el año actual y el nacimiento
print ("bienvenidos al programa".center(50,"*"))
FEC_ACT = 2019
fec_nac = int(input("ingrese tu año de nacimiento:."))

edad = FEC_ACT - fec_nac

print ("tu edad es {}".format(edad))
if edad >= 18:
    print ("eres mayor de edad")
else:
    print ("eres menor de edad")
