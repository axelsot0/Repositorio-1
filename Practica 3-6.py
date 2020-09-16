print("--------------------------------------------------------------------------------------------")
print("Ejercico 6.")
print("Hacer una función que reciba una cedula como argumento y diga si la cedula es válida o no.")

def verificacion_cedula():
    empezar = int(input("Ingrese 0 para comenzar: "))
    while empezar != 0:
        print("error.")
        empezar = int(input("Ingrese 0 para comenzar: "))
    else:
        numero_cedula = float(input("Ingrese el numero de cedila(Sin espacios o guiones.): "))
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))
        mes =  int(input("Ingrese su mes de nacimiento: "))
        dia = int(input("Ingrese su dia de nacimiento: "))
        sexo = int(input("Ingrese su sexo(1-para masculino 2-para femenino): "))
        

    while numero_cedula >= 99999999999:
        print("Su numero de cedula es incrrecto")
        empezar = int(input("Ingrese 0 para comenzar: "))

    while numero_cedula <= 00000000000:
        print("Su numero de cedula es incrrecto")
        empezar = int(input("Ingrese 0 para comenzar: "))


    while año_nacimiento <= 1920:
        print("Su año de nacimiento no es verdadero: ")
        empezar = int(input("Ingrese 0 para comenzar: "))
    
    while año_nacimiento > 2002:
        print("Su año de nacimiento no es verdadero: ")
        empezar = int(input("Ingrese 0 para comenzar: "))

    while mes == 0:
        print("Su mes de nacimiento no es correcto: ")
        empezar = int(input("Ingrese 0 para comenzar: "))

    while mes > 12:
        print("Su mes de nacimiento no es correcto: ")
        empezar = int(input("Ingrese 0 para comenzar: "))

    while sexo > 2:
        print("Su sexo es incorrecto")
        empezar = int(input("Ingrese 0 para comenzar: "))

    while sexo < 1:
        print("Su sexo es incorrecto")
        empezar = int(input("Ingrese 0 para comenzar: "))


    else:
        print("Su cedula es valida.")
        print("Gracias por usar nuestros servicios.")    





verificacion_cedula()

 



