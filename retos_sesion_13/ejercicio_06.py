while True:
    num = int(input("Ingresa un número (0 para salir): "))

    #Si el número es 0, salimos del ciclo y terminamos el programa
    if num == 0:
        print("El programa ha finalizado")
        break

    #Verificamos si el número es múltiplo de 7
    if num % 7 == 0:
        print("Es múltiplo de 7")
    else:
        print("No es múltiplo de 7")
