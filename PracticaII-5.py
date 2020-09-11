billete1000 = 9
billete500 = 19
billete100 =  99

def retiro(monto):
       global billete1000, billete500, billete100
       d1 = int(monto / 1000) 
       monto = monto % 1000 
       if d1 >= billete1000:
         monto = monto + (d1 - billete1000) * 1000
         d1 = billete1000
       d2 = int(monto / 500)
       monto = monto % 500
       if d2 >= billete500:
         monto = monto + (d2 - billete500) * 500
         d2 = billete500
       d3 = int(monto / 100)
       monto = monto % 100  
       if d3 >= billete100:
         monto = monto + (d3 - billete100) * 100
         d3 = billete100
       return [d1, d2, d3]


print ("Bienvenido al cajero ABC, por favor elegir el banco para su Transacción:  ")
print ("1. Banco ABC")
print ("2. Otros ")
select = input(":  ")
select = int(select)


if select == 1:
  a = int(input("Ingrese el monto para retirar: "))
  if a <= 10000:
      res = retiro(a)
      print("Billetes de 1000: " , res[0])
      print("Billetes de 500: ", res[1])
      print("Billetes de 100: ", res[2]) 
  if a == 0:
      print ("Retiro nulo")
  if a >= 10000:
      print("El monto deseado excede el limite") 
  

if select == 2:
  a = int(input("Ingrese el monto a retirar: "))
  if a <= 2000:
      res = retiro(a)
      print("Billetes de 1000: " , res[0])
      print("Billetes de 500: ", res[1])
      print("Billetes de 100: ", res[2]) 
  if a == 0:
      print ("Retiro nulo")
  if a >= 2000:
      print("El monto deseado excede el limite")