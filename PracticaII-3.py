print("-----------------------------------------------------")
print("Ejercicio 3")

numero = int(input("Ingrese 5 para seguir: "))

def error():
 print("Error usted no ingresó 5")

error()

if numero == 5:
 for i in range (1,1001):
    print(numero,"X",i,"=",numero * i)





if numero != 5:
    print("-----------------")
    error()



