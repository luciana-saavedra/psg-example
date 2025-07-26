estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

for nombre, nota in estudiantes:
    if nota >= 51:
        #Imprimimos el mensaje de felicitación
        print(f"¡Felicidades {nombre}! Aprobaste con {nota} puntos.")
