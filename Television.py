class Tv:
    def __init__(self,marca):
        self.marca=marca
        self.encendida=False
    
    def encenderTv(self):
        if(self.encendida==False):
            self.encendida=True
        else:
            print ("La Tv está encendida")

    def apagarTv(self):
        if(self.encendida==True):
            self.encendida=False
        else:
            print ("La Tv está apagada")

    def saberMarca(self):
        print (self.marca)

tele=Tv("Samsung")
tele.encenderTv()
tele.apagarTv()
tele.saberMarca()