# Fernando Ulises Gomez Sanchez TICs
# Examen
# Programa que guarde a todos los integrantes del grupo como objetos con sus atributos. Y que imprima lo siguiente:
# 5 alumnos con mayor edad
# Promedio de todos en la preparatoria
# Alumnos que viven mas cerca y mas lejos
# Materia con mejor rendimiento

class Alumno():
    def __init__ (self, Edad, CD, FP, FdI, Itics, TallerE, Ign, Mdd, CalP, lugarR, DT):
        self.Edad = Edad
        self.CD = CD
        self.FP = FP
        self.FdI = FdI
        self.Itics = Itics
        self.TallerE = TallerE
        self.Ign = Ign
        self.Mdd = Mdd
        self.CalP = CalP
        self.lugarR = lugarR
        self.DT = DT

Reyna = Alumno(17.8, 9, 9, 10, 10, 8, 9, 9, 9, "Emiliano", 15)
Mirozlava = Alumno(18.2, 8, 8, 10, 9, 8, 9, 9, 8, "Cosio", 30)
Melany = Alumno(18.4, 7, 10, 10, 10, 10, 9, 8, 9, "Pabellos", 7)
Diego = Alumno(19.2, 9, 7, 10, 9, 10, 9, 8, 8, "Rincon", 20)
Britsy = Alumno(19.9, 7, 10, 9, 9, 10, 10, 10, 8, "Rincon", 22)
Fernando = Alumno(17.9, 10, 10, 10, 10, 10, 10, 9, 10, "Pabellon", 6)
Johana = Alumno(18.5, 9, 7, 10, 10, 10, 7, 8, 8, "Jesus Maria", 25)
Alejandro = Alumno(19.3, 9, 9, 9, 8, 7, 10, 8, 9, "Rincon", 20)
Donaldo = Alumno(18.7, 9, 8, 10, 8, 10, 10, 9, 9, "Pabellon", 6)
Austin = Alumno(19.7, 7, 7, 10, 8, 10, 10, 7, 8, "Pabellos", 7)
Paola = Alumno(18.3, 10, 10, 10, 9, 9, 9, 8, 9, "Pabellos", 8)
Isaac = Alumno(19.2, 9, 10, 9, 10, 10, 10, 10, 9, "Rincon", 21)
Areli = Alumno(19.4, 8, 7, 10, 10, 9, 9, 10, 8, "Rincon", 20)
Alexis = Alumno(19.5, 10, 10, 9, 10, 10, 10, 9, 10, "Rincon", 20)

print ("Ingenieria TICs primer semestre grupo A")
opcion = 0
while True:
    print("""
    ¿Qué quieres ver?
    
    1) Los 5 alumnos con mayor edad  
    2) Promedio de todos en la preparatoria 
    3) Alumnos que viven mas lejos y mas cerca
    4) Materia con mejor rendimiento
    5) Salir
    """)

    opcion = int(input("Elige una opción: ") )     
    if opcion == 1:
        print(" ")
        print("Britsy con ",Britsy.Edad, "Años de edad")
        print("Austin con ",Austin.Edad, "Años de edad")
        print("Alexis con ",Alexis.Edad, "Años de edad")
        print("Areli con ",Areli.Edad, "Años de edad")
        print("Alejandro ",Alejandro.Edad, "Años de edad")
    elif opcion == 2:
        print(" ")
        print("Calificaciones del grupo en preparatoria: ")
        print(Reyna.CalP, Mirozlava.CalP, Melany.CalP, Diego.CalP, Britsy.CalP, Fernando.CalP, Johana.CalP, Alejandro.CalP, Donaldo.CalP)
        print(Austin.CalP, Paola.CalP, Isaac.CalP, Areli.CalP, Alexis.CalP)
        print ("El promedio es de: 8.7 ")
    elif opcion == 3:
        print(" ")
        print("El alumno mas que vive mas lejos es Mirozlava en",Mirozlava.lugarR,"Distancia: ",Mirozlava.DT)
        print ("El alumno mas cercano son Fernando en",Fernando.lugarR,"y Donaldo",Donaldo.lugarR,"Con:",Fernando.DT)
    elif opcion == 4:
         print(" ")
         print("La materia con mayor promedio es Fundamentos de investigacion: ")
         print(Reyna.FdI, Mirozlava.FdI, Melany.FdI, Diego.FdI, Britsy.FdI, Fernando.FdI, Johana.FdI, Alejandro.FdI, Donaldo.FdI, Austin.FdI, Paola.FdI, Isaac.FdI, Areli.FdI, Alexis.FdI)
         print("Que suma un promedio de: 9.7")
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")