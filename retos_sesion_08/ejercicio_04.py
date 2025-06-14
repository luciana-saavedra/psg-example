notas = (10, 61, 80, 21, 22, 0, 32, 30, 41, 51, 5, 5, 23, 100)

promedio = sum(notas) / len(notas)

if promedio >= 51:
    resultado = "Aprobó"
else:
    resultado = "No aprobó"

print(f"El promedio es: {promedio:.2f} - {resultado}")