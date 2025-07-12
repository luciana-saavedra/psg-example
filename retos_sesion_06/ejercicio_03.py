print("Tabla de verdad - Sistema de seguridad")
print("Tarjeta | Huella  | Puerta")

#La puerta solo se abre si se usa la tarjeta o la huella, pero no ambas al mismo tiempo

tarjeta = True
huella = True
print(tarjeta, " |", huella, "  |", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = True
huella = False
print(tarjeta, " |", huella, " |", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = False
huella = True
print(tarjeta, "|", huella, "  |", (tarjeta or huella) and not (tarjeta and huella))

tarjeta = False
huella = False
print(tarjeta, "|", huella, " |", (tarjeta or huella) and not (tarjeta and huella))

print("Utilizaríamos el operador XOR")