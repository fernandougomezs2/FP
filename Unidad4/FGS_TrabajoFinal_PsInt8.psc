Algoritmo NombreAleatorio
	Definir n Como Entero
	Definir Nom, x Como Caracter
	Escribir "Fernando Ulises Gomez Sanchez"
	Escribir "Programa que pida el nombre de una persona y lo imprima con las letras de forma aleatoria"
	Escribir "Dame el nombre de la persona: "
	Leer Nom
	n = longitud(Nom)
	x = ""
	Mientras n > 0 Hacer
		x = x + Subcadena(Nom, n, n)
		n = azar(30)
	Fin Mientras
	Escribir "El nombre de forma aleatoria " Nom " es: " x
FinAlgoritmo