print("-----------------------------------------------------------------")
print("Ejecicio 2")

def opciones():
    print(" 1- Convertir grados a Celsius a Fahrenheit    2- Convertir dólar a pesos    3- Convertir metros a pies     4- Salir : ")

opciones ()
accion = input("Elija una opción:")
accion = int(accion)

while accion != 4:
  if accion == 1:
      print("Convertir grados Celsius a Fahrenheit")
      Cantidad_celcius = input("Ingrese Cantidad de grados celsius: ")
      Cantidad_celcius = float(Cantidad_celcius)
      print("Grados Fahrenheit:")
      print(Cantidad_celcius * 9 / 5 +32)

     
      
      opciones()
      accion = input("Ingrese una opción: ")
      accion = int(accion)

  elif accion == 2:
       print("Convertir dolar a pesos")
       cantidad_dollar = input("Ingrese cantidad de dolares")
       cantidad_dollar = float(cantidad_dollar)
       print("Pesos:")
       print(cantidad_dollar * 58.52)
      
   
       opciones()
       accion = input("Ingrese una opción: ")
       accion = int(accion)

  elif accion == 3:
       print("Convertir metros a pies")
       cantidad_metros = input("Ingrese cantidad de metros: ")
       cantidad_metros = float(cantidad_metros)
       print("Pies:")
       print(cantidad_metros * 3.28)   

      
       opciones()
       accion = input("Ingrese una opción: ")
       accion = int(accion)
  elif accion >= 4:
      print("Error")
      print("Acción no valida")

     
      opciones()
      accion = input("Ingrese una opción:  ")
      accion = int(accion)

if  accion == 4:
     print("Gracias por utilizar nuestros servicios") 




    

    


     