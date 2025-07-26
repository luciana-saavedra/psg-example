print("20 primeros múltiplos de 2 y 5: ")
contador = 0  #Contador de números encontrados
numero = 1    #Número que vamos a evaluar

while contador < 20:
    # Verificamos si el número es divisible por 2 y 5
    if numero % 2 == 0 and numero % 5 == 0:
        print(numero, end=", ")
        contador += 1
    numero += 1  #Pasamos al siguiente número