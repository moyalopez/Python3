##moya
##crear un programa que permita solucionar en una o de dos opciones
##convertir dolares a quetzales o quetzales a dolares

print ("bienvenidos a mi programa".center(50,"*"))
print ("valor del dolar:.  Q.7.45")
print ("opcion 1= Q a $ , opcion 2= $ a Q")
dolares =7.45
quet =float(input("ingrese cantidad:."))
opcion = float(input("ingrese opcion:."))
multiplicacion = (quet / dolares)
div = (quet * dolares)
if opcion == 1:
 print (multiplicacion)
if opcion == 2:
 print (div)
if opcion < 1:
    print ("no esta la opcion")
if opcion > 2:
    print ("no esta la opcion")

