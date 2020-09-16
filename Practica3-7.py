print("------------------------------------------------------------------------------------------------")
print("Ejercicio 7")
print("Ingrese sus numeros luego presione 0 para finalizar.")



def duplicar(a,b,c):

    return [a*2, b*2, c*2]

z = int(input("Ingrese numeros a la lista 0 para terminar:  "))

while z != None:
    z = int(input("Ingrese numeros a la lista:  "))

w = int(input("Ingrese numeros a la lista:  "))
x = int(input("Ingrese numeros a la lista:  "))

res = duplicar(z,w,x)
print(res)



