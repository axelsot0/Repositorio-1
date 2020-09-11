print("--------------------------------------")
print("Ejercicio 4")
print("Una pregunta entre nosotros...")
sueldo = input("Cual es su sueldo? ")
sueldo = float(sueldo)
sueldo_anual = sueldo * 12

des1 = 416220.00 

des2 = 624329.00 

des3 = 867123.00 

ars = 0.0304

afp = 0.028

def descuento ():
  ARS = sueldo_anual * ars
  AFP = sueldo_anual * afp
  print ("Descuento", ARS, " de ARS anualmente")
  print ("descuento ", AFP, " de AFP anualmente")



if sueldo_anual <= des1:
   print("Exento del ISR")
   descuento()

elif sueldo_anual <= des2:
     calculo_des = sueldo_anual * 0.15
     print("Total a pagar: ", calculo_des, "para IRS")

elif sueldo_anual <= des3:
  calculo_des2 = (sueldo_anual * 0.20) + 31216.00
  print ("Total a pagar: ", calculo_des2, " de IRS")
  descuento()

else:
  calculo_des4= (sueldo_anual * 0.25) + 79776.00
  print ("Total a pagar: ", calculo_des4, " de IRS")
  descuento()
  