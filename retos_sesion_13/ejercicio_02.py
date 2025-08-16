print("20 primeros múltiplos de 2 y 5:")

contador = 0  #Contador de múltiplos encontrados
numero = 1    #Número que vamos a evaluar

while contador < 20:
    if numero % 2 == 0 and numero % 5 == 0:
        #Imprimimos los múltiplos
        print(numero, end=", " if contador < 19 else "\n")
        contador += 1
    numero += 1  #Pasamos al siguiente número