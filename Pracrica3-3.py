print("------------------------------------------------------------------------------------")
print("Ejercicio 3")
print("Hacer una función que reciba un año como argumento y retorne verdadero si es bisiesto.")

año = int(input("Ingrse un año: "))


def años():
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
             print('El año es bisiesto')
            
            else:
                print('El año no es bisiesto')
        else:
            print('El año es bisiesto.')
    else:
        print('El año no es bisiesto.')
    



años()

 