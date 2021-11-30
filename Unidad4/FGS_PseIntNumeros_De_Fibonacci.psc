Algoritmo NumerosF
	Definir numero_, a, b, tmp como Entero
    Escribir "	Por favor ingrese la cantidad de números de la serie que se imprimirán:"
    Leer numero_
    b = 1
    Para i<-1 Hasta numero_ Hacer
        Escribir a
        total = a + b
        a = b
        b = total
    FinPara
	
FinAlgoritmo
