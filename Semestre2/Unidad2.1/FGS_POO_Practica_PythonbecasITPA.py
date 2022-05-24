print("BecasITPA")
ciclo= 1
while ciclo == 1:
    print("Datos del alumno")
    nom = str(input("Nombre del alumno: "))
    print("¿De donde es?")
    print("1.- Pabellon de Artega")
    print("2.- Otro lugar")
    don = int(input(": "))
    if don == 1:
        print("El alumno", nom, "no puede tener la beca")
    else:
        print("Promedio: ")
        print("1.- Igual a 8")
        print("2.- Mayor a 9")
        pro = int(input(": "))
        print("¿Tiene materias reprobadas? ")
        print("1.- Si ")
        print("2.- No ")
        mr = int(input(": "))
        if mr == 1:
            print("El alumno ",  nom ," No puede tener la beca")
        else:
            print("¿Tiene beca?")
            print("1.- Si")
            print("2.- Beca federal")
            print("3.- No")
            beca = int(input(": "))
            if beca == 1:
                print("El alumno ", nom ," No puede tener la beca")
            else:
                Suma = pro + beca
                if Suma == 5:
                    print("El alumno ", nom ," Cumple con todos los requisitos, sus posibilidades de que le toque la beca es del 100%")
                else:
                    print ("El alumno ", nom ," Cumple con la mayoria de los requisitos, sus posibilidades de que le toque la beca es del 50%")
    

    ciclo = int(input("""

    ¿Quieres agregar otro alumno?
    1.- Si
    2.- No
    
    """))

print("Fin")



        

        