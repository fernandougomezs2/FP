# Fernando Ulises Gomez Sanchez
# Programa en el que pidas un número del 1 al 10 y que haga un sorteo de un número ganador entre ese rango de forma aleatoria

print("Algoritmo NumeroAleatorio")

import random
n = int(input("Dame un numero del 1 al 10: "))
Sorteo = random.randint(1,n)
print(Sorteo)

print("Fin")
          
	 
