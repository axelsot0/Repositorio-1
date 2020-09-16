print("---------------------------------------------------------------------------------------------------")
print("Ejercicio 8")
print("Hacer una función que reciba un valor iniciar y uno final, y muestre en pantalla las tablas de multiplicar de los números múltiplos de 6 que hay entre el valor inicial y el valor final.")



def error():
    numero = int(input("Ingrese 6 para seguir: "))
    while numero != 6:
     print("Error usted no ingresó 6")
     numero = int(input("Ingrese 6 para seguir: "))
    else:
        numero1 = int(input("Ingrese el valor inicial: "))
        numero2 = int(input("Ingrese el valor final: "))
    for i in range (numero1,numero2):
        print(numero,"X",i,"=",numero * i)



error()
