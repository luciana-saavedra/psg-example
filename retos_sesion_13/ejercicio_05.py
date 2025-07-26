for fila in range(8):
    linea = ""  #Variable para construir cada línea del tablero
    
    for columna in range(8):
        #Si la suma de fila y columna es par, agregamos '#', sino '*'
        if (fila + columna) % 2 == 0:
            linea += " # "
        else:
            linea += " * "
    print(linea)  # Imprimimos la línea completa