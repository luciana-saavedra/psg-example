while True:
    try:
        #Solicitar primer número o salir
        num1 = input("Ingresa el primer número (o 'salir' para terminar): ")
        if num1.lower() == "salir":
          print ("el programa finalizo")
          break

        #Solicitar segundo número o salir
        num2 = input("Ingresa el segundo número (o 'salir' para terminar): ")
        if num2.lower() == "salir":
          print ("el programa finalizo")
          break

        #Convertir los datos a float
        num1 = float(num1)
        num2 = float(num2)

        #Operaciones matemáticas
        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicación: {num1 * num2}")

        #División con manejo de división por cero
        try:
            print(f"División: {num1 / num2}")
        except ZeroDivisionError:
            print("Error!: No se puede dividir entre cero.")

    #Manejo de error por dato no numérico
    except ValueError:
        print("Error!: Debes ingresar valores numéricos.")
    #Manejo de errores inesperados
    except Exception as error:
        print(f"⚠️ Error inesperado: {error}")
