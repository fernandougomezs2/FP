Algoritmo NumAleatorio
	Definir n, a Como Entero
	Escribir "Fernando Ulises Gomez Sanchez"
	Escribir "Programa en el que pidas un número del 1 al 10 y que haga un sorteo de un número ganador entre ese rango de forma aleatoria"
	Escribir "Dame un numero del 1 al 10: "
	Leer a
	Repetir
		Escribir "Dame un numero del 1 al 10: "
		Leer a
	Hasta Que a >= 1 y a <= 10
	n = azar(a) + 1
	Escribir "El numero ganador es " n
FinAlgoritmo
