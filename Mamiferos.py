class Mamiferos:
    def __init__(self,codigo,nombres,apellidos):
        self.codigo=codigo
        self.nombres=nombres
        self.apellidos=apellidos
    def mostrar(self):
        #print (self.codigo)
        #print (self.nombres,self.apellidos)

        print ("El codigo de:",self.nombres,self.apellidos,"es:",self.codigo)


alumno1=Mamiferos("201701","Juan","León")
alumno1.mostrar()