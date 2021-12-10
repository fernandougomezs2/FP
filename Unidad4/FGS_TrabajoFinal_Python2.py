# Fernando Ulises Gomez Sanchez
# Programa que ingreses el nombre completo de dos personas y te cuente el número de letras de cada nombre. Después que imprima cual es mayor.

print ("Algoritmo NombreMayorCaracteres")
n11 = int
n22 = int

n1= input("Dame el primer nombre: ")
n11 = len(n1)
print("El numero de letras del primer nombre es: ", n11)
n2= input("Dame el segindo nombre: ")
n22 = len(n2)
print("El numero de letras del segundo nombre es: ", n22)

if n11 > n22 :
	print("El nombre mas largo es: ", n1)
else:
	print("El nombre mas largo es: ", n2)

print("Fin")
