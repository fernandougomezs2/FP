Algoritmo Calculadora
	Definir n Como Entero
	Definir num1 Como Real
	Definir num2 Como Real
	escribir "Fernando Ulises Gomez Sanchez "
	escribir "Calculadora que sume, reste, multiplique y divida "
	
	Escribir "Seleccione una opcion: 1. Suma  2. Resta  3. Multiplicacion 4. Division "
	Escribir "Opcion: "
	Leer n
	
	Segun n Hacer
		1:
			Escribir "Usted eligio suma"
			Escribir "Dame un numero: "
			Leer num1
			Escribir "Dame otro numero: "
			Leer num2
			S = num1 + num2
			Escribir "El resultado es: " S
		2:
			Escribir "Usted eligio resta"
			Escribir "Dame un numero: "
			Leer num1
			Escribir "Dame otro numero: "
			Leer num2
			R = num1 - num2
			Escribir "El resultado es: " R
		3:
			Escribir "Usted eligio multiplicacion"
			Escribir "Dame un numero: "
			Leer num1
			Escribir "Dame otro numero: "
			Leer num2
			M = num1 * num2
			Escribir "El resultado es: " M
		4:
			Escribir "Usted eligio Division"
			Escribir "Dame un numero: "
			Leer num1
			Escribir "Dame otro numero: "
			Leer num2
			D = num1 / num2
			Escribir "El resultado es: " D
			
		De Otro Modo:
			Escribir "Opcion incorrecta"
	Fin Segun
	
FinAlgoritmo
