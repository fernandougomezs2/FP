# Fernando Ulises Gomez Sanchez TICs
# Insertar la calificacion utilizando un ciclo hasta que apruebes
print("Cargando.......")
print("Cargando.................")
running = True
while running:
    Calificacion1 = float(input('Ingresa tu calificacion: '))
    Cal = float(Calificacion1)
    if Cal >= 7 :
        print('Felicitaciones, has aprobado.')
# Esto hace que el ciclo while se detenga      
        running = False
    elif Cal < 7:
        print('Lo siento, has reprobado')
else:
    print('El ciclo while ha terminado.')
# El ciclo termina cuando apruebas la materia 

print('---Fin---')