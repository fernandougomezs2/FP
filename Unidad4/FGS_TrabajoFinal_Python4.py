# Fernando Ulises Gomez Sanchez
# Programa que saque el área de un círculo, un cuadrado, rectángulo y triángulo

print ("Algoritmo Area")

R = float
R1 = float
A = float
Op = int(input("""
Selecciona una opcion
1. Circulo
2. Cuadrado
3. Rectangulo
4. Triangulo
"""))

if Op == 1 :
	print("Area del circulo")
	D = float(input("Dame el diametro: "))
	R = D/2
	R1 = R*R
	A = 3.14 * R1
	print("El area del circulo es: ", A)
elif Op == 2 :
	print("Area del Cuadrado")
	Al = float(input("Dame el ancho y el largo: "))
	A = Al * Al
	print("El area del cuadrado es: ", A)
elif Op == 3 :
	print("Area del Rectangulo")
	B = float(input("Dame la base: "))
	Alt = float(input("Dame la altura: "))
	A = B * Alt
	print("El area del rectangulo es: ", A)
elif Op == 4 :
	print("Area del Triangulo")
	B = float(input("Dame la base: "))
	Alt = float(input("Dame la altura: "))
	A = B * Alt / 2
	print("El area del triangulo es: ", A)
else :
	print ("Error")

print("Fin")

