##moya
##Elabore un programa que permita ingresar el precio y la cantidad de un articulo
##a comprar. calcular el total a pagar(el iva es del 9%)

IVA = 0.09
print("Un programa que permita ingresar el precio y la cantidad de un articulo con el iva")

prod = float(input("ingresa el precio del producto:. "))
cant = int(input("Ingresa la cantidad del producto:. "))
tot = prod * cant
iva = tot * IVA
print("EL iva a pagar es de:. {}".format(iva))
print("EL total a pagar es de :. {}".format(tot))
