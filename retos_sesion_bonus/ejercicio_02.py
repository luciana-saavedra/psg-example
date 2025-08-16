def obtener_aleatorio():
    secreto = 42
    return secreto

def adivina(secreto):
    intentos = 0
    print("¿Qué número estoy pensando? (1-100)")
    while True:
        try:
            #Solicitamos al usuario que ingrese un número
            intento = int(input(f"Intento N° {intentos + 1}: "))
            if intento == secreto:
                #Mensaje si acierta
                print("¡Felicidades! Has adivinado el número!")
                break
            elif intento < secreto:
                #Indicamos si el número secreto es mayor
                print("El número es mayor.")
            else:
                #Indicamos si el número secreto es menor
                print("El número es menor.")
        except ValueError:
            #Revisamos si el usuario no ingresa un número válido
            print("Por favor, ingresa un número válido.")
        finally:
            #Incrementamos el contador de intentos
            intentos += 1
    #Mostramos la cantidad de intentos realizados
    print(f"Has adivinado el número en {intentos} intentos.\n")

def jugar():
    #Mensaje de bienvenida y solicitud del nombre del jugador
    print("Bienvenido al juego de adivinanzas del Python Study Group 2025")
    print("="*63)
    nombre_jugador = input("¿Cuál es tu nombre?: ")
    print(f"Bienvenido, {nombre_jugador}!")
    print("="*63)
    
    while True:
        opcion = input("¿Quieres jugar? (s/n): ")

        if opcion.lower() != 's':
            break
        #Obtenemos el número secreto
        secreto = obtener_aleatorio()
        #Ejecutamos la función para adivinar
        adivina(secreto)
    
    #Mensaje de despedida y agradecimiento al jugador
    print("Gracias por participar!")
    print(f"🐍 Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()