notas = (10, 61, 0, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

#Calculamos el promedio
promedio = sum(notas) / len(notas)

#Evaluamos si aprobó (promedio >= 51)
aprobado = promedio >= 51

#Imprimimos resultados
print("Promedio:", promedio)
print("¿Aprobó el semestre?:", aprobado)