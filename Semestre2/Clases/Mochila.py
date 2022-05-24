class Mochila:
    def __init__(self,Marca,Cierres,Color,Material,Espaldar,Compartimiento):
        self.Marca = Marca
        self.Cierres = Cierres
        self.Color = Color
        self.Material = Material
        self.Espaldar = Espaldar
        self.Compartimiento = Compartimiento
        pass
    def LlevarCosas(self):
        print("Compartimiento: ",self.Compartimiento)
    def Descripcion(self):
        print("Marca: ",self.Marca," Cierres: ",self.Cierres," Color: ",self.Color," Material: ",self.Material," Espaldar: ",self.Espaldar)

Moch1 = Mochila("Nike",True,"Azul","Cuero",True,True)

Moch1.LlevarCosas()
Moch1.Descripcion()
