cadena = input("Ingresa una frase: ")

#Quitamos espacios y convertimos todo a minúsculas
procesado = cadena.replace(" ", "").lower()

#Evaluamos si es palíndromo
es_palindromo = procesado == procesado[::-1]

print("¿Es palíndromo?", es_palindromo)