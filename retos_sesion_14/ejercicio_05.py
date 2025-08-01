def contar_vocales(cadena):
    #Definimos las vocales
    vocales = 'aeiouAEIOU'
    #Contador de vocales
    contador = 0
    #Recorremos cada caracter en la cadena
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

texto = input("Ingresa una cadena: ")
print("Cantidad de vocales:", contar_vocales(texto))
