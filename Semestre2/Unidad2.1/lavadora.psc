Algoritmo Lavadora
	Definir RS Como Caracter
	Definir A Como Caracter
	Definir Tie Como Entero
	Definir AAA Como Caracter
	Escribir "Lavadora"
	Escribir "Conectar lavadora"
	Escribir "¿hay ropa sucia?"
	Leer RS
	Si RS = "Si" Entonces
		Escribir "Agregar Ropa"
		Escribir "Agregar detergente"
		Escribir "¿Hay agua?"
		Leer A
		Si A = "Si" Entonces
			Escribir "Agregar agua"
			Escribir "¿Cuantos minutos de lavado quiere?"
			Leer Tie
			Escribir "Tiempo de lavado: " Tie "min"
			Escribir "Encender lavadora"
			Escribir "Activar enjuague"
			Escribir "Sacar ropa"
			Escribir "Fin"
		SiNo
			Escribir "¿Quieres ir a apagar el agua?"
			Leer AAA
			Si AAA = "Si" Entonces
				Escribir "Ir a pagar el agua"
				Escribir "Agregar agua"
				Escribir "¿Cuantos minutos de lavado quiere?"
				Leer Tie
				Escribir "Tiempo de lavado: " Tie "min"
				Escribir "Encender lavadora"
				Escribir "Activar enjuague"
				Escribir "Sacar ropa"
				Escribir "Fin"
			SiNo
				Escribir "Fin"
			Fin Si
		Fin Si
	SiNo
		Escribir "Fin"
	Fin Si
	
	
FinAlgoritmo
