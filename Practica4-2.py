print("--------------------------------------")
print("Ejercicio 2")
print("Crear una clase llamada Estudiante con un campo llamado promedio, el cual solo podrá ser accedido mediante un metodo. El valor del promedio no puede estar por encima de 100 que es la nota máxima")

class Estudiante:
    def __init__(self):

        self.matematicas = 40
        self.sociales = 85
        self.naturales = 81
        self.español = 75


    def calcular_promedio(self):
        promedio = self.matematicas + self.sociales + self.naturales + self.español
        total = promedio / 4
        print(f"Su promedio es de {total}")


calcula_promedio = Estudiante()
calcula_promedio.calcular_promedio()