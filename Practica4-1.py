print("---------------------------------------------------------------")
print("Ejecicio 1")
print("Modele tres entidades del mundo real, colocar por lo menos 3 características distintivas.")


class Abanico:
#abanico
    def __init__(self):
        
        self.marca = "Lasko"
        self.base = 1
        self.cantidad_aspas = 3
        self.motor = 1
        self.flujo_elecricidad = "desconectado"

    def enciende(self):
        print("Abanico")
        if self.flujo_elecricidad == "desconectado":
            self.flujo_elecricidad = str(input("Desea encender si o no? "))
        if self.flujo_elecricidad == "si":
            print("Encendido")
    
    def apagar(self):
        if self.flujo_elecricidad == "si":
            flujo_elecricidad = str(input("Ingrese no para desconectar: "))
            if flujo_elecricidad == "no":
                print("Apagado")
    
    def girar(self):
        if self.flujo_elecricidad == "si":
            print("Girando")

abanico_axel = Abanico()
abanico_axel.enciende()
abanico_axel.girar()
abanico_axel.apagar()

class TV:
    def __init__(self):
       
       self.marca = "Samsung"
       self.base = 1
       self.conexion_cable = "no"
       self.flujo_elecricidad = "desconectado"
       self.canales = 1
       self.cambio = 1
#Television
    def enciende(self):
        print("Televison")
        if self.flujo_elecricidad == "desconectado":
            self.flujo_elecricidad = str(input("Si, para encender? "))
        if self.flujo_elecricidad == "si":
            print("Encendido")
    
    def   apagar(self):
        if self.flujo_elecricidad == "si":
            flujo_elecricidad = str(input("Ingrese si para desconectar: "))
            if flujo_elecricidad == "si":
                print("Apagado")
    

    def mostrar_canales(self):
        if self.flujo_elecricidad == "si":
            if self.conexion_cable == "no":
                self.conexion_cable = str(input("Desea establacer una conexion por cable? (si) para conectar: "))
                if self.conexion_cable == "si":
                    print("Conexion realizada con exito.")

    def cambiar_canales(self):
        if self.flujo_elecricidad == "si":
            if self.conexion_cable == "si":
                if self.conexion_cable == "si":
                    self.cambio = int(input("Cambiar de canal, en el num pad 5 para avanzar: "))
                    if self.cambio == 5:
                        self.canales = self.canales + 1
                        if self.canales == 2:
                            print("Canal 2.")
                        
    def cambiar_canales0(self):
        if self.flujo_elecricidad == "si":
            if self.conexion_cable == "si":
                if self.conexion_cable == "si":
                    self.cambio = int(input("Cambiar de canal, en el num pad 4 para retroceder: "))
                    if self.cambio == 4:
                        self.canales = self.canales - 1
                        if self.canales == 1:
                            print("Canal 1.")                       

television = TV()
television.enciende()
television.mostrar_canales()
television.cambiar_canales()
television.cambiar_canales0()
television.apagar()



class Puerta:
    def __init__(self):

        self.tipo_madera = "Caoba"
        self.manubrio = "Funcional"
        self.visagrasA = "si"
        
        
    def abrir_puerta(self):
        if self.manubrio == "Funcional":
            self.visagrasA = str(input("Desea Abrir  la puerta(si o no)? "))
            if self.visagrasA == "si":
                print("Puerta abieta")

    
    def cerrar_puerta(self):
        if self.manubrio == "Funcional":
            self.visagrasA = str(input("Desea cerrar la puerta(si o no)? "))
            if self.visagrasA == "si":
                print("La puerta está cerrada")

puerta_cuarto = Puerta()
puerta_cuarto.abrir_puerta()
puerta_cuarto.cerrar_puerta()