print("--------------------------------------------------------------------------------------------------------------------------")
print("ejercicio 1:")
print("Imprimir cifras")

numeros = []

cantidad = int(input("Cuantos numeros va a imprimir? "))
for i in range(cantidad):
    numero = int(input("numero: "))
    
    numeros.append(numero)

if numero < 1:
    print("Error")
    print("Numero no puede ser igual a cero")

else:
    print("Usted imprimió esta cantidad de numeros")
    print(cantidad)
    sum([numero])
    
  