def separar_pares_impares(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

#Pedimos al usuario que ingrese números separados por coma
entrada = input("Ingresa números separados por comas (ej: 1,3,5,4): ")

#Convertimos la cadena a lista de enteros
numeros = []
for n in entrada.split(","):
    n = n.strip()   #quitamos espacios por si hay
    if n.isdigit(): #verificamos que sea un número válido y positivo
        numeros.append(int(n))
    else:
        print(f"'{n}' no es un número válido y será ignorado.")

pares, impares = separar_pares_impares(numeros)

print("Números pares:", pares)
print("Números impares:", impares)