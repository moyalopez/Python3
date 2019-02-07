#MOYA
#solicitar al usuario que selecione una opcion 
#opcion 1 solicitar dos numeros elevar el primer numero por el segundo 
#opcion 2 solicitar solicitar 3 numeros y elevar el primero al segundo y el resultado elevarlo al tercero

print("BIENVENIDOS A MI PROGRAMA".center(50,"-"))
print("opcion 1 solicitar 2 numeros para elevacion")
print("opcion 2 solicitar 3 numeros para elevacion")

opcion = input("ingrese opcion:.")
if opcion == "1":
 print("elegiste la opcion 1")
 num1 = input("ingrese valor:.")
 num2 = input("ingrese valor:.")
 elv = float(num1) ** float(num2)
 print("su resultado es {}".format(elv)) 
if opcion == "2":
 print("elegiste la opcion 2")
 num3 = input("ingrese valor:.")
 num4 = input("ingrese valor:.")
 num5 = input("ingrese valor:.")
 uno = float(num3) ** float(num4)
 dos = float(num5) ** (uno)
 print("su resultado es {}".format(dos))
else:
 print("esta opcion no esta, hasta la proxima actualizacion gracias")   
