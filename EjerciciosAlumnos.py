class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Alumno: ",self.nombre)
        print("Nota: ",self.nota)
        print("")
    
    def resultado(self):
        if self.nota<5:
            print("El alumno ha reprobado")
        else:
            print("El alumno ha aprobado")

alumno1=Alumno()

alumno1.imprimir()
alumno1.resultado()