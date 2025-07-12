# partition(): divide la cadena en tres partes usando un separador
linea = "clave:valor extra"
antes, separador, despues = linea.partition(":")
print(f"Original: '{linea}' → Antes: '{antes}', Separador: '{separador}', Después: '{despues}'")

# isnumeric(): verifica si todos los caracteres son números
dato = "12345"
print(f"¿'{dato}' es numérico?: {dato.isnumeric()}")

# center(): centra el texto en un ancho dado rellenando con un carácter
titulo = "Bienvenida"
print(f"'{titulo}' centrado en 20 caracteres: '{titulo.center(20, '*')}'")

# isidentifier(): verifica si la cadena es un identificador válido en Python
palabra = "variable_1"
palabra2 = "123abc"
print(f"¿'{palabra}' es un identificador válido?: {palabra.isidentifier()}")
print(f"¿'{palabra2}' es un identificador válido?: {palabra2.isidentifier()}")

# rjust(): justifica a la derecha la cadena rellenando con un carácter
precio = "50"
print(f"'{precio}' justificado a la derecha en 6 espacios con ceros: '{precio.rjust(6, '0')}'")