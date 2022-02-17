print("Algoritmo Venta")
V = str(input("Que venta vas hacer "))
C = str(input("¿Hay cliente? "))
if C == "Si":
    print("Recopilacion de datos del cliente")
    nom = str(input("Nombre: "))
    E = int(input("Edad: "))
    oc = str(input("Ocupacion: "))
    gen = str(input("Genero: "))
    PS = str(input("Productos o Servicios: "))
    ne = str(input("Necesidades: "))
    FdP = str(input("Forma de pago: "))

    CA = str(input("¿El cliente acepto la venta? "))
    if CA == "Si":
        print("Producto vendido: ", V)
        print("Datos del cliente:")
        print("Nombre: ", nom)
        print("Edad: ", E)
        print("Ocupacion: ", oc)
        print("Genero: ", gen)
        print("Productos o Servicios: ", PS)
        print("Forma de pago: ", FdP)
        print("Fin")
    else:
        print("Resolver sus necesidades: ", ne)
        Res= str(input("Responder: "))
        Acp = str(input("¿Acepto? "))
        if Acp == "Si":
            print("Producto vendido: ", V)
            print("Datos del cliente:")
            print("Nombre: ", nom)
            print("Edad: ", E)
            print("Ocupacion: ", oc)
            print("Genero: ", gen)
            print("Productos o Servicios: ", PS)
            print("Forma de pago: ", FdP)
            print("Fin")
        else:
            print("Fin")
else:
    print("Fin")



