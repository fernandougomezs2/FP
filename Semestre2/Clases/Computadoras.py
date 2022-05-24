class Computadoras:
    def __init__(self, Tipo, Marca, Color, RAM):
        self.Tipo = Tipo
        self.Marca = Marca
        self.Color = Color
        self.RAM = RAM
    def Descripcion(self):
        print("Tipo: ",self.Tipo)
        print("Marca: ",self.Marca)
        print("Color: ",self.Color)
        print("RAM: ",self.RAM)

O1 = Computadoras("Escritorio","Lenovo","Azul",12)

O1.Descripcion()