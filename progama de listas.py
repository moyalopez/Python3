#
#generen los numeros del 0 al 20
#generen 2 listas que se llamen pares que almacene todos los numeros pares
#otra que se llamen impares que almacene todo los numeros impares

pares = []
impares = []

for i in range(21):
     if i % 2 == 0:
         pares.append(i)
     else:
         impares.append(i)
print("pares {}".format(pares))
print("impares {}".format(impares))

