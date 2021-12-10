Algoritmo Area
	Definir Op Como Entero
	Definir D Como Real
	Definir R Como Real
	Definir A Como Real
	Definir R1 Como Real
	Definir AL Como Real
	Definir B Como Real
	Definir Alt Como Real
	Escribir "Fernando Ulises Gomez Sanchez"
	Escribir "Programa que saque el área de un círculo, un cuadrado, rectángulo y triángulo"
	
	Escribir "Seleccione una opcion: "
	Escribir "1.- Circulo"
	Escribir "2.- Cuadrado"
	Escribir "3.- Rectangulo"
	Escribir "4.- Triangulo"
	Leer Op
	Segun Op Hacer
		1:
			Escribir "Usted eligio sacar el area del circulo"
			Escribir "Dame el diametro del circulo: "
			Leer D
			R = D/2
			R1 = R * R
			A = 3.14 * R1
			Escribir "El area del circulo es: " A
		2:
			Escribir "Usted eligio sacar el area del cuadrado"
			Escribir "Dame el ancho y el largo del cuadrado: "
			Leer AL
			A = AL * AL
			Escribir "El area del cuadrado es: " A
		3:
			Escribir "Usted eligio sacar el area del rectangulo"
			Escribir "Dame la base: "
			Leer B
			Escribir "Dame la altura: "
			Leer Alt
			A = B * Alt
			Escribir "El area del rectangulo es: " A
		4:
			Escribir "Usted eligio sacar el area del triangulo"
			Escribir "Dame la base: "
			Leer B
			Escribir "Dame la altura: "
			Leer Alt
			A = B * Alt / 2
			Escribir "El area del triangulo es: " A
			
		De Otro Modo:
			Escribir "Error"
	Fin Segun
	
	
FinAlgoritmo
