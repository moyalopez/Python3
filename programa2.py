##jair
##solicitar  al usuario que elija una de las siguientes opciones
##sumar dos numero ,
##restar 3 numeros
##,multiplicar 4 numeros
##,dividir 2 numeros 

print ("BIENVENIDOS A MI PROGRAMA".center(50,"*"))
print ("1 = sumar dos numeros")
print ("2 = restar 3 numeros")
print ("3 = multiplicar 3 numeros")
print ("4 = dividir 2 numeros")

opcion =  float(input("ingresa una opcion:."))
if opcion == 1:
  print ("elegiste SUMA")
  num1 = float(input("ingresa un numero:."))
  num2 = float(input("ingresa un numero:."))
  suma = float (num1 + num2)
  print (suma)
elif opcion == 2:
  print ("elegiste RESTA")
  num3 = float(input("ingresa un numero:."))
  num4 = float(input("ingresa un numero:."))
  num5 = float(input("ingresa un numero:."))
  resta = float(num3 - num4 - num5)
  print (resta)
elif opcion == 3:
  print ("elegiste MULTIPLICACION")
  num6 = float(input("ingresa un numero:."))
  num7 = float(input("ingresa un numero:."))
  num8 = float(input("ingresa un numero:."))
  num9 = float(input("ingresa un numero:."))
  mult = float(num6 * num7 * num8 * num9)
  print (mult)
elif opcion == 4:
  print ("elegiste DIVISION")
  num10 = float(input("ingresa un numero:."))
  num11 = float(input("ingresa un numero:."))
  div = float(num10 / num11)
  print (div)
else:
  print ("no hay opcion")

