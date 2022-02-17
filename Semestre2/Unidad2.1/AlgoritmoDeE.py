def euclides(num1,num2,iteracciones=1):
 
     # Si el num1 es inferior al num2, los invertimos
    if num1<num2:
        num1,num2=num2,num1
 
    # obtenemos el resto de la division
    resto=num1%num2
 
    if resto==0:
        return (num2,iteracciones)
    
    # llamamos nuevamente a la función pasando como primer parametro el
    # segundo numero y el resto de la division
    return euclides(num2,resto,iteracciones+1)
 
num1=int(input("Numero 1: "))
num2=int(input("Numero 2: "))
 
comunDivisor,iteracciones=euclides(num1,num2)
 
print("El Maximo comun divisor de",num1,"y",num2,"es ",comunDivisor)
print("Se ha encontrado en",iteracciones, "iteracciones")



