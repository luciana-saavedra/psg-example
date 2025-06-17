numeros = [3.14, 5.0, 2.718, 10, 15, 7, 21, 100, 42, 8.5]

for indice in range(len(numeros)):
    elemento = numeros[indice]
    tipo_dato = type(elemento)
    print(f"Elemento en el índice {indice}: {elemento}, tipo de dato: {tipo_dato}")