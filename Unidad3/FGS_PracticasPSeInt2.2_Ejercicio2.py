# Fernando Ulises Gomez Sanchez
# Programa que que ponga 5 opciones de peliculas y escojas 1

print ("Algoritmo Peliculas")
print("""
    1) Dragon ball       3) Rapidos y furiosos
    2) Sonic       4) El conjuro
    5) Guerra de mundos
    """)

eligio=input("Selecciona una opcion: ")

if eligio=="1":
    print("Seleccionaste Dragon ball")
elif eligio=="2":
    print("Seleccionaste Sonic")
elif eligio=="3":
    print("Seleccionaste Rapidos y furiosos")
elif eligio=="4":
    print("Seleccionaste El conjuro")
elif eligio=="5":
    print("Seleccionaste Guerra de mundos")
else:
    print("Opción no válida")
