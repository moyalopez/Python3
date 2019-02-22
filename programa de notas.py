#jairmoya
opcion = int(input("1.promedio de 4 notas\n2.division\n3.Salir\nIngrese su opcion:."))
promedio = 0

while opcion != 3:
    if opcion == 1:
        
        for i in range (4):
            nota = int(input("ingrese primera nota"))
            promedio = promedio + nota
            div = int(promedio) / int(4)
        print ("el promedio es:. {}".format(div))
    elif opcion == 2:
        num1 = float(input("Ingrese numero:."))
        num2 = float(input("Ingrese numero:."))
        
        if num2 != 0:
            total = num1 / num2
            print("Total:.",total)
        else:
            print("error, valor incorrecto... intente de nuevo")
    opcion = int(input("1.promedio de 4 notas\n2.division\n3.Salir\nIngrese su opcion:."))


        

