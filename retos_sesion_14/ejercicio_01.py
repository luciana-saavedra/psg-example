def calcular_promedio(calificaciones):
    #Sumamos todas las calificaciones y dividimos entre la cantidad de elementos
    return sum(calificaciones) / len(calificaciones)

#Lista de calificaciones
notas = [50, 75, 80, 91, 70]
print("Promedio:", calcular_promedio(notas))