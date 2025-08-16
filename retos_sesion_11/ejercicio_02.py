#Diccionario de alimentos y los animales que los consumen
alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}

#Añadimos 4 alimentos con update(clave=valor)
alimentos.update(leche=["gato", "perro"])
alimentos.update(pasto=["conejo", "vaca"])
alimentos.update(pescado=["pez", "gato"])
alimentos.update(maiz=["vaca", "pollo"])

#Verificamos si 'trigo' está en el diccionario
print("¿Existe 'trigo' en el diccionario?", "trigo" in alimentos)

#Eliminamos 'zanahoria' del diccionario
alimentos.pop("zanahoria")

#Diccionario actualizado
print("Diccionario actualizado de alimentos:", alimentos)