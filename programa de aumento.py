#Jairmoya
#solicitar nombre de empleado años de antiguedad para encontrar aumento

print("Bienvenidos a mi programa".center(70,"*"))
print(" de 3 a 4 años de antiguedad se le aumentara el 5%")
print("de 5 a 6 años de antiguedad se le aumentara el 15%")


nom = input("ingrese su nombre completo:.")
pue = input("ingrese su puesto de trabajo:.")
dic = input("ingrese su direccion:.")
tel = input("ingrese su telefono:.")
ani = input("ingrese sus años de antiguedad:.")
sul = input("ingrese su sueldo:.")

sum1 = float(sul) * float(0.05)
num1 = float(sul) + float(sum1)
sum2 = float(sul) * float(0.15)
num2 = float(sul) + float(sum2)
if ani == "1":
    print("su sueldo es el mismo no tiene aumento {}".format(sul))
elif ani == "2":
    print("su sueldo es el mismo no tiene aumento {}".format(sul))
elif ani == "3":
    print("su sueldo anterior era {}".format(sul))
    print("se le aumento {}".format(sum1))
    print("su sueldo actual es {}".format(num1))
elif ani == "4":
    print("su sueldo anterior era {}".format(sul))
    print("se le aumento {}".format(sum1))
    print("su sueldo actual es {}".format(num1))
elif ani == "5":
    print("su sueldo anterior era {}".format(sul))
    print("se le aumento {}".format(sum2))
    print("su sueldo actual es {}".format(num2))
elif ani == "6":
    print("su sueldo anterior era {}".format(sul))
    print("se le aumento {}".format(sum2))
    print("su sueldo actual es {}".format(num2))
else:
    print("no se puede")
