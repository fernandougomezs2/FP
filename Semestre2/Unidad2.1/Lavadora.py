print("Algoritmo Lavadora")
print("Lavadora")
print("Conectar lavadora")

RS = str(input("¿Hay ropa sucia? "))
if RS == "Si":
    print("Agregar ropa")
    print("Agregar detergente")
    A = str(input("¿Hay agua? "))
    if A == "Si":
        print("Agregar agua")
        Tie = float(input("¿Cuantos minutos de lavado quiere? "))
        print("Minutos de lavado:", Tie, "min")
        print("Encender lavadora")
        print("Encender enjuague")
        print("Sacar ropa")
        print("Fin")
    else:
        AAA= str(input("¿Quieres ir a pagar el agua? "))
        if AAA == "Si":
            print("Ir a pagar el agua")
            print("Agregar agua")
            Tie = float(input("¿Cuantos minutos de lavado quiere? "))
            print("Minutos de lavado:", Tie, "min")
            print("Encender lavadora")
            print("Encender enjuague")
            print("Sacar ropa")
            print("Fin")
        else:
            print("Fin")
else:
    print("Fin")

