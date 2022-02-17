print("Algoritmo Maquina_Refrescos")
print("Maquina exprendedora de refrescos")
print("Costo: 1$")
D = int(input("Meter dinero: "))
print("""Seleccionar producto

1.- Coca Cola
2.- Pepsi
3.- Sprite

""")

SP = int(input("¿Cual? "))

if SP == 1 or SP == 2:
    if D >= 2:
        Sobra = D - 1
        print("Te sobra", Sobra ,"$")
        print("Entregar producto")
        print("Fin")
    else:
        print("Entregar producto")
        print("Fin")
else:
    P_Ago= str(input("Producto agotado ¿Quiere otro producto?"))
    if P_Ago == "Si":
        input("""Seleccionar producto

        1.- Coca Cola
        2.- Pepsi

        """)
        if D >= 2:
            Sobra = D - 1
            print("Te sobra", Sobra ,"$")
            print("Entregar producto")
            print("Fin")
        else:
            print("Entregar producto")
            print("Fin")
    else:
        print("Devolver dinero: ", D ,"$")
        print("Fin")

           





    
