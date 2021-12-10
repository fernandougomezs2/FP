# Fernando Ulises Gomez Sanchez
# Programa que te estime el tiempo de llegada a un destino con base en la velocidad y distancia.

print ("Algoritmo TiempoVelocidadDistancia")

Des = input("Dime tu destino ")
D = float(input("A que distancia se encuentra tu destino con base a kilometros: "))

print("Selecciona una opcion")
print(""" 
1. Caminando
2. En vehiculo
3. En bicicleta
	""")
C = int(input("Opcion: "))
if C == 1 :
	print("Caminando")
	Ca = float(input("Tu velocidad es de 1 a 20 km/h selecciona una velocidad:"))
	Tiempo = D/Ca
	print("Tu tiempo estimado a tu destino ",Des, "Es de: ",Tiempo, "Horas")
elif C == 2 :
	print("En vehiculo")
	Ca = float(input("Tu velocidad es de 10 a 200 km/h selecciona una velocidad:"))
	Tiempo = D/Ca
	print("Tu tiempo estimado a tu destino ",Des, "Es de: ",Tiempo, "Horas")
elif C == 3 :
	print("En bicicleta")
	Ca = float(input("Tu velocidad es de 5 a 75 km/h selecciona una velocidad:"))
	Tiempo = D/Ca
	print("Tu tiempo estimado a tu destino ",Des, "Es de: ",Tiempo, "Horas")
else :
	print("Error")

print("Fin")



