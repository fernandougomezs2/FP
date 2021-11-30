# Fernando Ulises Gomez Sanchez
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión

print("Algoritmo CantidadInvertir")
cantidad= float(input("Cantidad a invertir: "))
interes = float(input("Interés porcentual anual: "))
años = int(input("Años: "))
print("...........Cargando...........")
print("...............Cargando....................")
print("....................Cargando............................")
print("Su Capital final es de: " + str(round(cantidad * (interes / 100) * años)))