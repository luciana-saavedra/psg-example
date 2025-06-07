#partition()
linea = "clave:valor extra"
antes, separador, despues = linea.partition(":")
print(antes, separador, despues)

#isnumeric()
dato = "12345"
print(dato.isnumeric())

#center()
titulo = "Bienvenida"
print(titulo.center(20, "*"))

#isidentifier()
palabra = "variable_1"
print(palabra.isidentifier())
palabra2 = "123abc"
print(palabra2.isidentifier())

#rjust()
precio = "50"
print(precio.rjust(6, "0"))