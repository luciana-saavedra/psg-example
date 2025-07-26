while True:
    frase = input("Ingresa una frase (escribe 'salir' para terminar): ").lower()

    #Si la frase contiene la palabra 'salir', terminamos el programa
    if "salir" in frase:
        print("Programa finalizado.")
        break

    #Quitamos espacios para evaluar el palíndromo correctamente
    frase_junta = frase.replace(" ", "")

    #Comparamos la frase para saber si es palíndromo
    if frase_junta == frase_junta[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")