class Persona:
    def __init__(self,Nombre,Edad,Sexo,Peso,Tamaño,Color_de_piel):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Sexo = Sexo
        self.Peso = Peso
        self.Tamaño = Tamaño
        self.Color_de_piel = Color_de_piel
    def Caminar(self):
        print(self.Nombre, "Deracha, Izquierda")

    def Moverse(self):
        print(self.Nombre, "Mano derecha, Mano izquierda")

    def Alimentarse(self):
        print("Comer...")
        print("Peso: ",self.Peso)
    
    def Descripcion(self):
        print("Nombre: ",self.Nombre," Edad: ",self.Edad," Sexo: ",self.Sexo," Tamaño: ",self.Tamaño," Coloe de piel: ",self.Color_de_piel)

Fer = Persona("Fernando",18,"Macho pecho peludo",56,1.77,"Blanco")

Fer.Caminar()
Fer.Moverse()
Fer.Alimentarse()
Fer.Descripcion()