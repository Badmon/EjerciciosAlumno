class Gelatina:
    def __init__(self,tam,color,sabor): #
        self.tam=tam
        self.color=color
        self.sabor=sabor
    def desplegar(self):
        print (self.tam)
        print (self.color)
        print (self.sabor)
gel1=Gelatina("chico","rojo","fresa")
gel2=Gelatina("mediana","verde","manzana")
gel3=Gelatina("grande","amarillo","plátano")
gel1.desplegar()
gel2.desplegar()
gel3.desplegar()

