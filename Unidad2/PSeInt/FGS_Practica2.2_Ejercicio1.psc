Algoritmo NumeroMayor
	Definir a,b,c Como Entero
	Escribir 'Programa que pida 3 numeros e imprima el numero mayor'
	Escribir 'Dame un numero'
	Leer a
	Escribir 'Dame otro numero'
	Leer b
	Escribir 'Dame otro numero'
	Leer c
	Si a>b Entonces
		Si a>c Entonces
			Escribir 'El numero mayor de los tres es:',' ',a
		SiNo
			Escribir 'El numero mayor de los tres es:',' ',c
		FinSi
	SiNo
		Si b>c Entonces
			Escribir 'El numero mayor de los tres es:',' ', b
		SiNo
			Escribir 'El numero mayor de los tres es:',' ',c
		FinSi
		
	FinSi
FinAlgoritmo
