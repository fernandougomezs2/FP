import time

print("Algoritmo Usuario_Contraseña")

u = str("Fernando")
c = str("Fous")

Usuario = str(input("Cual es tu usuario: "))
Contraseña = str(input("Cual es tu contraseña: "))
if Usuario == u and Contraseña == c:
    print("Bienvenido")
else:
    Opcion = int(3)
    while Opcion <= 3 and Opcion > 0:
        print("Tienes", Opcion ,"intentos")
        Usuario = str(input("Cual es tu usuario: "))
        Contraseña = str(input("Cual es tu contraseña: "))
        if Usuario == u and Contraseña == c:
            print("Bienvenido")
            break
        else:
            Opcion = Opcion - 1
    if Opcion == 0:
        print("Espera 120 segundos")
        time.sleep(10) 

        print("Puedes intentar otros 3 intentos")
        Opcion = int(3)
        while Opcion <= 3 and Opcion > 0:
            print("Tienes", Opcion ,"intentos")
            Usuario = str(input("Cual es tu usuario: "))
            Contraseña = str(input("Cual es tu contraseña: "))
            if Usuario == u and Contraseña == c:
               print("Bienvenido")
               break
            else:
                Opcion = Opcion - 1
        if Opcion == 0:
            print("Saliendo del sistema")
            
print("Fin")
    
        
            