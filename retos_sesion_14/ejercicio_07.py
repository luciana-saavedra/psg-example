# Tres en Raya

# Crear un tablero vacío (3x3)
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Iniciar el turno con el jugador "X"
turno_actual = "X"

# Función para mostrar el tablero en consola
def mostrar_tablero():
    for fila in tablero:
        print(fila)
    print()

# Función para verificar si hay un ganador
def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

# Función para verificar si hay empate
def tablero_lleno():
    for fila in tablero:
        if " " in fila:
            return False
    return True

# Función principal del juego
def tres_en_raya():
    global turno_actual

    while True:
        print(f'Juega "{turno_actual}"')

        # Pedir la jugada del jugador
        try:
            fila = int(input("Fila (0, 1 o 2): "))
            columna = int(input("Columna (0, 1 o 2): "))
        except ValueError:
            print("Solo se aceptan números. Intenta otra vez.\n")
            continue

        # Verificar que la jugada esté dentro del tablero
        if not (0 <= fila <= 2 and 0 <= columna <= 2):
            print("Coordenadas fuera de rango. Intenta otra vez.\n")
            continue

        # Verificar si la casilla está ocupada
        if tablero[fila][columna] != " ":
            print("Casilla ocupada. Intenta otra vez.\n")
            continue

        # Registrar la jugada
        tablero[fila][columna] = turno_actual

        # Mostrar el tablero actualizado
        mostrar_tablero()

        # Verificar si hay un ganador
        ganador = verificar_ganador()
        if ganador:
            print(f'¡Ganó "{ganador}"!')
            break

        # Verificar empate
        if tablero_lleno():
            print("¡Empate!")
            break

        # Cambiar turno
        turno_actual = "O" if turno_actual == "X" else "X"

# Ejecutar el juego
tres_en_raya()