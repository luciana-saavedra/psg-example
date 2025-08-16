# Tres en Raya
# Crear un tablero vacío (3x3)
tablero = [[" " for columna in range(3)] for fila in range(3)]

# Iniciar el turno con el jugador "X"
turno_actual = "X"

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print(fila)
    print()

# Función para verificar ganador
def verificar_ganador():
    for i in range(3):
        # Filas y columnas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

# Función para verificar empate
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

        # Pedir jugada
        try:
            fila_jugada = int(input("Fila (0, 1 o 2): "))
            columna_jugada = int(input("Columna (0, 1 o 2): "))
        except ValueError:
            print("Solo se aceptan números. Intenta otra vez.\n")
            continue

        # Verificar coordenadas
        if not (0 <= fila_jugada <= 2 and 0 <= columna_jugada <= 2):
            print("Coordenadas fuera de rango. Intenta otra vez.\n")
            continue

        # Verificar si la casilla está ocupada
        if tablero[fila_jugada][columna_jugada] != " ":
            print("Casilla ocupada. Intenta otra vez.\n")
            continue

        # Registrar jugada
        tablero[fila_jugada][columna_jugada] = turno_actual

        # Mostrar tablero actualizado
        mostrar_tablero()

        # Verificar ganador
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