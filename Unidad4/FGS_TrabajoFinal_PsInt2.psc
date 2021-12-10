Algoritmo NombreMayorCaracteres
	Definir n1 Como Caracter
	Definir n2 Como Caracter
	Definir n11 Como Entero
	Definir n22 Como Entero
	Escribir "Fernando Ulises Gomez Sanchez"
	Escribir "Programa que ingreses el nombre completo de dos personas y te cuente el número de letras de cada nombre. Después que imprima cual es mayor"
	
	Escribir "Dame el primer nombre: "
	Leer n1
	n11 = Longitud(n1)
	Escribir " " n1 " Tiene: " n11 " Caracteres "
	
	Escribir "Dame el segundo nombre: "
	Leer n2
	n22 = longitud(n2)
	Escribir " " n2 " Tiene: " n22 " Caracteres "
	
	Si n11 > n22 Entonces
		Escribir "El nombre mas largo es: " n1
	SiNo 
		Escribir "El nombre mas largo es: " n2
	Fin Si
FinAlgoritmo
