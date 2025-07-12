alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}

#Añadimos 4 alimentos
alimentos.update({
    "leche": ["gato", "perro"],
    "pasto": ["conejo", "vaca"],
    "pescado": ["pez", "gato"],
    "maiz": ["vaca", "pollo"]
})

#Verificamos si 'trigo' está en el diccionario
print(f"¿Existe 'trigo' en el diccionario? {'trigo' in alimentos}")

#Eliminamos 'zanahoria' del diccionario
alimentos.pop("zanahoria", None)

#Diccionario actualizado
print(f"Diccionario actualizado de alimentos:\n{alimentos}")