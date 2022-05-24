class Animal:
    def __init__(self,Nombre,Edad,Salud,Tamaño,Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Salud = Salud
        self.Tamaño = Tamaño
        self.Peso = Peso

    def Moverse(self):
        print("Caminar....")
        print("Correr....")
    def Comer(self):
        print("mmmmm que rico")
        print("Peso: ",self.Peso)
    def Descripcion(self):
        print("Nombre: ",self.Nombre," Edad: ",self.Edad," Tamaño: ",self.Tamaño," Salud: ",self.Salud)

Animal1 = Animal("Fernandito JR",10,"Sani",0.70,50)

Animal1.Moverse()
Animal1.Comer()
Animal1.Descripcion()
