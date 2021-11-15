# Fernando Ulises Gomez Sanchez
# Hacer un programa que te pida 3 numeros e imprima el mayor

print("Algoritmo NumeroMayor")

numeros = []
for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
        
print("Mayor:", mayor)
