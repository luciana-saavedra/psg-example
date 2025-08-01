#Pedimos al usuario cuántos números de la serie de Lucas desea ver
n = int(input("Ingrese la cantidad de números de la serie que desea obtener: "))

#Definimos una función recursiva para obtener el n-ésimo número de la serie de Lucas
def serie_lucas(n):
    if n == 0:
        return 2  #El primer número de la serie de Lucas es 2
    elif n == 1:
        return 1  #El segundo número de la serie de Lucas es 1
    else:
        #La función se llama a sí misma con los dos valores anteriores
        return serie_lucas(n - 1) + serie_lucas(n - 2)

#Imprimimos los primeros n números de la serie usando un bucle for
for i in range(n):
    print(serie_lucas(i), end=" ")