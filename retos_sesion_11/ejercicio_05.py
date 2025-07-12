#Diccionario que representa el arca de Noé
arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}

#Añadimos 3 especies más
arca.update({
    "🐲": 1,
    "🐍": 2,
    "🐰": 4
})

#Lista de animales (claves)
animales = list(arca.keys())

#Imprimir cada animal con su cantidad, manualmente
print(f"Animales en el arca:")
print(f"{animales[0]}: {arca[animales[0]]}")
print(f"{animales[1]}: {arca[animales[1]]}")
print(f"{animales[2]}: {arca[animales[2]]}")
print(f"{animales[3]}: {arca[animales[3]]}")
print(f"{animales[4]}: {arca[animales[4]]}")
print(f"{animales[5]}: {arca[animales[5]]}")
print(f"{animales[6]}: {arca[animales[6]]}")
print(f"{animales[7]}: {arca[animales[7]]}")
print(f"{animales[8]}: {arca[animales[8]]}")

#Verificamos si 'dragon' 🐲 está en el arca
print(f"\n¿Está el dragón? {'🐲' in arca}")

#Eliminamos la especie unicornio
arca.pop("🦄", None)

#Modificamos cantidad de jirafa a 2
arca["🦒"] = 2

#Actualizamos la lista porque cambió el diccionario
animales = list(arca.keys())

print("\nDespués de modificar la cantidad de jirafa y eliminar unicornio:")
print(f"{animales[0]}: {arca[animales[0]]}")
print(f"{animales[1]}: {arca[animales[1]]}")
print(f"{animales[2]}: {arca[animales[2]]}")
print(f"{animales[3]}: {arca[animales[3]]}")
print(f"{animales[4]}: {arca[animales[4]]}")
print(f"{animales[5]}: {arca[animales[5]]}")
print(f"{animales[6]}: {arca[animales[6]]}")
print(f"{animales[7]}: {arca[animales[7]]}")

#Vaciamos el arca después del diluvio
arca.clear()

#Estado final del arca
print(f"\nEstado final del arca después del diluvio: {arca}")