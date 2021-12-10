Algoritmo VelocidadD
	Definir Ca, KD, Tiempo Como Real
	Definir C Como Entero
	Escribir "Fernando Ulises Gomez Sanchez"
	Escribir "Programa que te estime el tiempo de llegada a un destino con base en la velocidad y distancia"
	
	Escribir "Cual es tu destino: "
	Leer D
	Escribir "A que distancia se encuentra tu destino con base a kilometros: "
	Leer KD
	Escribir "Como vas a ir: "
	Escribir "1.- Caminando"
	Escribir "2.- En un vehículo"
	Escribir "3.- En bicicleta"
	Leer C
	Segun C Hacer
		1:
			Escribir "Selecciono caminar"
			Escribir "Escoge tu velocidad"
			Escribir "Tu velocidad puede ser desde 1 hasta 20 km/h: "
			Leer Ca
			Tiempo = KD/Ca
			Escribir "Tu tiempo estimado de llegada al " D " es de: " Tiempo " Horas "
		2:
			Escribir "Selecciono vehiculo"
			Escribir "Escoge tu velocidad"
			Escribir "Tu velocidad puede ser desde 10 hasta 200 km/h: "
			Leer Ca
			Tiempo = KD/Ca
			Escribir "Tu tiempo estimado de llegada al " D " es de: " Tiempo " Horas "
		3:
			Escribir "Selecciono bicicleta"
			Escribir "Escoge tu velocidad"
			Escribir "Tu velocidad puede ser desde 5 hasta 70 km/h: "
			Leer Ca
			Tiempo = KD/Ca
			Escribir "Tu tiempo estimado de llegada al " D " es de: " Tiempo " Horas "
			
		De Otro Modo:
			Escribir "No existe la opcion"
	Fin Segun
	
FinAlgoritmo
