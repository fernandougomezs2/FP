Algoritmo Venta
	Definir C, CA Como Caracter
	Escribir "Venta"
	Escribir "Que venta vas hacer"
	Leer V
	Escribir "¿Hay cliente?"
	Leer C
	Si C = "Si" Entonces
		Escribir "Recopilacion de datos del cliente"
		Escribir "Nombre: "
		Leer nom
		Escribir "Edad: "
		Leer ed
		Escribir "Ocupacion: "
		Leer oc
		Escribir "Genero: "
		Leer gen
		Escribir "Productos o Servicios"
		Leer PS
		Escribir "Necesidades: "
		Leer N
		Escribir "Forma de pago: "
		Leer FdP
		Escribir "¿El cliente acepto la venta?"
		Leer CA
		Si CA = "Si" Entonces
			Escribir "Producto vendido: " V
			Escribir "Datos de cliente: "
			Escribir "Nombre: " nom "Edad: " ed "Ocupacion: " oc "Genero: " gen "Productos o Servicios: " PS "Forma de pago: " FdP
			Escribir "Fin"
		SiNo
			Escribir "Resolver sus necesidades: " N
			Leer RN
			Escribir "¿Acepto?"
			Leer A
			Si A = "Si" Entonces
				Escribir "Producto vendido: " V
				Escribir "Datos de cliente: "
				Escribir "Nombre: " nom "Edad: " ed "Ocupacion: " oc "Genero: " gen "Productos o Servicios: " PS "Forma de pago: " FdP
				Escribir "Fin"
			SiNo
				Escribir "Fin"
			Fin Si
		Fin Si
	SiNo
		Escribir "Fin"
	Fin Si
	
FinAlgoritmo
