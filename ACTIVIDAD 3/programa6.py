#MOYA
#realizar el promedio n notas utilizando el for
print("BIENVENIDOS A MI PROGRAMA".center(50,"-"))
suma = 0
valor1 = int(input("ingresa el numero de notas:.")) 
for i in range (valor1):
    valor = float(input("ingresa un valor:."))
    suma = suma + valor
promedio = int(suma) / valor1


print ("el promedio es {}".format(promedio))    
