#MOYA
#realizar el promedio de 5 notas utilizando el ciclo for
print("BIENVENIDOS A MI PROGRAMA".center(50,"-"))
suma = 0
for i in range (5):
    valor = int(input("ingresa un valor:."))
    suma = suma + valor
promedio = int(suma)/5



print ("el promedio es {}".format(promedio))    

