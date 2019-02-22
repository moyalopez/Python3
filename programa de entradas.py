#JAIR MOYA
#determine el el valor de cuatro entradas con descuento

print("bienvenidos a mi programa".center(50,"*"))
print("valor de entrada Q200.00")
print("si compra dos entradas se le aplica descuento del 10%")
print("si compra tres entradas se le aplica descuento del 15%")
print("si compra cuatro entradas se le aplica descuento del 20%")

ent = input("cuantas entradas desea comprar:.")
por1 = 400 * 0.1
num1 = 400 - por1
por2 = 600 * 0.15
num2 = 600 - por2
por3 = 800 * 0.2
num3 = 800 - por3

if ent == "1":
    print("no aplica el descuento")
elif ent == "2":
    print("su precio a pagar es {}".format(num1))
    print("se ahorro {}".format(por1))
elif ent == "3":
    print("su precio a pagar es {}".format(num2))
    print("se ahorro {}".format(por2))
elif ent == "4":
    print("su precio a pagar es {}".format(num3))
    print("se ahorro {}".format(por3))
else:
    print("no es permitido")
    



