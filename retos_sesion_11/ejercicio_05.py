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

#Lista de animales en el arca
iterador_arca = iter(arca.items())

print("Animales en el arca:")

print(next(iterador_arca))  # perro
print(next(iterador_arca))  # gato
print(next(iterador_arca))  # tigre
print(next(iterador_arca))  # mono
print(next(iterador_arca))  # unicornio
print(next(iterador_arca))  # jirafa
print(next(iterador_arca))  # dragón
print(next(iterador_arca))  # serpiente
print(next(iterador_arca))  # conejo

#Verificamos si el dragón 🐲 está en el arca
print("\n¿Está el dragón?", "🐲" in arca)

#Eliminamos la especie unicornio
arca.pop("🦄", None)

#Modificamos cantidad de jirafa a 2
arca["🦒"] = 2

#Lista actualizada después de los cambios
iterador_arca_actualizado = iter(arca.items())

print("\nDespués de modificar la cantidad de jirafa y eliminar unicornio:")

print(next(iterador_arca_actualizado))  # perro
print(next(iterador_arca_actualizado))  # gato
print(next(iterador_arca_actualizado))  # tigre
print(next(iterador_arca_actualizado))  # mono
print(next(iterador_arca_actualizado))  # jirafa
print(next(iterador_arca_actualizado))  # dragón
print(next(iterador_arca_actualizado))  # serpiente
print(next(iterador_arca_actualizado))  # conejo

#Vaciamos el arca después del diluvio
arca.clear()
print("\nEstado final del arca después del diluvio:", arca)