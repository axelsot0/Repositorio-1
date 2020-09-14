print("--------------------------------------------------------------------------------------")
print("Ejercicio 4.")
print("Crear una función que evalúe dos números y retorne verdadero si ambos números son iguales.")

regresar =int(input("Si quiere  usar el programa ingresa 0: "))

while regresar != 0:
    print("Error")
    regresar =int(input("Si quiere  usar el programa ingresa 0: "))
else:
    num1 = int(input("Ingrese su primer número: "))
    num2 = int(input("Ingrese su segundo número: "))

def igual():
    while  num1 != num2:
      print("Falso")
      print("Sus números no coinciden: ")
      regresar =int(input("Si quiere  usar el programa ingresa 0: "))
      


    else:
        
        print("Verdadero")
        print("Gracias por usar nuestros servicios. ")
        
     
igual()





