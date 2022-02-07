Algoritmo Maquina_Refrescos
	Escribir 'Maquina expendedora de refrescos'
	Escribir "Meter dinero: "
	Leer D
	Escribir "Selecciona producto: "
	Escribir "1.- Coca cola"
	Escribir "2.- Pepsi"
	Escribir "3.- Sprite"
	Leer SP
	Si SP = 1 o SP = 2 Entonces
		Si D >= 2 Entonces
			Sobra = D - 1
			Escribir "Te sobra " Sobra "$"
			Escribir "Entregar Producto"
			Escribir "Fin"
		SiNo
			Escribir "Entregar Producto"
			Escribir "Fin"
		Fin Si
	SiNo
		Escribir "Producto agotado ¿Quiere otro producto? "
		Leer P_Ago
		Si P_Ago = "Si" Entonces
			Escribir "Selecciona producto: "
			Escribir "1.- Coca cola"
			Escribir "2.- Pepsi"
			Leer SP2
			Si D >= 2 Entonces
				Sobra = D - 1
				Escribir "Te sobra " Sobra "$"
				Escribir "Entregar Producto"
				Escribir "Fin"
			SiNo
				Escribir "Entregar Producto"
				Escribir "Fin"
			Fin Si
			
		SiNo
			Escribir "Devolver dinero: " D
			Escribir "Fin"
		Fin Si
	Fin Si
FinAlgoritmo
