class Auto:
    def __init__(self,Marca,Tipo,Modelo,Año,Color,Numero_De_Ruedas):
        self.Marca = Marca
        self.Tipo = Tipo
        self.Modelo = Modelo
        self.Año = Año
        self.Color = Color
        self.Numero_De_Ruedas = Numero_De_Ruedas
    def Acelerar(self):
        print("Ruun Ruun")
    def Reversa(self):
        print("run run run")
    def Girar(self):
        print("........")
    def Frenar(self):
        print("fffffffffffffff")
    def Descripcion(self):
        print("Marca: ",self.Marca," Tipo: ",self.Tipo," Modelo: ",self.Modelo," Año: ",self.Año," Color: ",self.Color)
        print("Numero de ruedas: ",self.Numero_De_Ruedas)

Auto1 = Auto("Ferrari","Troca","Sedan",2003,"Azul",4)

Auto1.Acelerar()
Auto1.Reversa()
Auto1.Girar()
Auto1.Frenar()
Auto1.Descripcion()
