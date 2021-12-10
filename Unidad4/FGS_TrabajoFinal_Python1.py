# Fernando Ulises Gomez Sanchez
# Calculadora que sume, reste, multiplique y divida

print ("Algoritmo Calculadora")

print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")

n = int(input("Selecciona una opcion: "))
num1 = float(input("Selecciona un numero "))
num2 = float(input("Selecciona otro numero "))


if n == 1 :
	print ("Usted selecciono Suma ")
	R = num1 + num2
	print("El resultado es ", R)

elif n == 2 :
	print ("Usted selecciono Resta ")
	R = num1 - num2
	print("El resultado es ", R)

elif n == 3 :
	print ("Usted selecciono Multiplicacion ")
	R = num1 * num2
	print("El resultado es ", R)

elif n == 4 :
	print ("Usted selecciono Division ")
	R = num1 / num2
	print("El resultado es ", R)

else :
	print ("Error")


