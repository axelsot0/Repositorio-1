print("--------------------------------------")
print("Ejercicio 1.")
print("Hacer una función que potencie un número x a la y")


def potenciar():
        total = numerox ** numeroy
        print(f"Numero a potenciar: {numerox} potenciado por: {numeroy} Total = {total}")
        print("Gracias por usar nuestros servicios.")
        
        
po = int(input("Ingrese 0 para empezar: "))
while po != 0:
    print("Error")
    po = int(input("Ingrese 0 para empezar: "))
    

else:
    numerox = int(input("Ingrese un numero a potenciar: "))
    numeroy = int(input("Ingrse numero por el que se va a potenciar: "))
    potenciar()

 
    



