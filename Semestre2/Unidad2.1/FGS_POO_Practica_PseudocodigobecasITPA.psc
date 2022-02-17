Algoritmo becasITPA
	Definir rep como entero
	
	Escribir "Becas ITPA"
	ciclo = 1
	Mientras ciclo=1 Hacer
		Escribir "Datos del alumno"
		Escribir "Nombre del alumno: "
		Leer nom
		Escribir "�De donde es? "
		Escribir "1.- Pabellon de Arteaga"
		Escribir "2.- Otro lugar"
		Leer don
		Si don = 1 Entonces
			Escribir "El alumno " nom " " " No puede tener la beca"
		SiNo
			Escribir "Promedio: "
			Escribir "1.- Igual a 8"
			Escribir "2.- Mayor a 9"
			leer pro
			Escribir "�Materias reprobadas?"
			Escribir "1.- Si"
			Escribir "2.- No"
			Leer mr
			Si mr = 1 Entonces
				Escribir "El alumno "  nom " " " No puede tener la beca"
			SiNo
				Escribir "Tiene beca"
				Escribir "1.- Si"
				Escribir "2.- Beca federal"
				Escribir "3.- No"
				Leer beca
				Si beca = 1 Entonces
					Escribir "El alumno "  nom " " " No puede tener la beca"
				SiNo
					Suma = pro + beca
					Si Suma = 5 Entonces
						Escribir "El alumno "  nom " " " Cumple con todos los requisitos, sus posibilidades de que le toque la beca es del 100%"
					SiNo
						Escribir "El alumno "  nom " " " Cumple con la mayoria de los requisitos, sus posibilidades de que le toque la beca es del 50%"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
		
		Escribir "�Quieres agregar otro alumno?"
		Escribir "1.- Si"
		Escribir "2.- No"
		Leer ciclo
		
	Fin Mientras
	
	
FinAlgoritmo
