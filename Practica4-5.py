print("---------------------------------------------------")
print("ejercicio 5")
print("Crear una clase llamada Estudiante con un campo llamado promedio, el cual solo podrá ser accedido mediante un metodo. El valor del promedio no puede estar por encima de 100 que es la nota máxima.")


class Carro:
    def __init__(self):

        self.cantidad_combustible = 5
        self.acelerador = 1
        self.motor = "apagado"
        


    def Encender(self):
        if self.motor == "apagado":
            self.motor = int(input("Ingrese 5 para encender el motor: "))
            if self.motor == 5:
                print("Motor encendido")
                if self.motor == 5:
                    self.acelerador = int(input("ingrese 1 para acelerar: "))
                    while self.acelerador == 1:
                        while self.cantidad_combustible > 0:
                            print("Pisando acelerador.")
                            print("Acelerando")
                            self.cantidad_combustible = self.cantidad_combustible - 1
                            print(f"El galon va por:{self.cantidad_combustible} Galones.")
                            self.acelerador = int(input("Desea dejar de acelerar?presione 0: " ))
                            while self.acelerador == 0:
                                print("Usted a dejado de acelerar.")
                                self.acelerador = int(input("ingrese 1 para acelerar: "))
                        
                                while self.cantidad_combustible < 1:

                                    print("No hay galones insuficientes para acelerar")
                                    self.cantidad_combustible = int(input("Ingrese 5 para rellenar los galones: "))
                                    self.acelerador = int(input("ingrese 1 para acelerar: "))

Carrito_rojo_de_carrera = Carro()
Carrito_rojo_de_carrera.Encender()


        