print("--------------------------------------------------------------------------------------------------------")
print("Ejercicio 2.")
print("Realizar una función que pida por pantalla un número del 1 al 10 y muestre  por pantalla el número escrito en letras.")

def numero_letras():
    num = int(input("Ingrese cualquier numero del 1-10: "))
    if num == 1:
        print(f"Numero:{num} Numero en letras: Uno. ")

    if num == 2:
        print(f"Numero{num} Numero en letras: Dos.")

    if num == 3:
        print(f"Numero{num} Numero en letras: Tres.")

    if num == 4:
        print(f"Numero{num} Numero en letras: Cuatro.")
   

    if num == 5:
        print(f"Numero{num} Numero en letras: Cinco.")

    if num == 6:
        print(f"Numero{num} Numero en letras: Seis.")

    if num == 7:
        print(f"Numero{num} Numero en letras: Siete.")

    if num == 8:
        print(f"Numero{num} Numero en letras: Ocho.")


    if num == 9:
        print(f"Numero{num} Numero en letras: Nueve.")

    if num == 10:
        print(f"Numero{num} Numero en letras: Diez.")

opciones = int(input("Introduzca: 1) para empezar  2) para salir.: "))

while opciones  < 1:
        print("Error introduzca una opcion valida.")
        opciones = int(input("Introduzca: 1) para empezar  2) para salir.: "))
        



while opciones >  2:
        print("Error introduzca una opcion valida.")
        opciones = int(input("Introduzca: 1) para empezar  2) para salir.: "))
        


else:
     numero_letras()

     










    




            
   

