#Ingresamos la pregunta como una cadena
pregunta = input("Ingresa una pregunta: ")

#Almacenamos la pregunta completa como un solo elemento en una tupla
pregunta_tupla = (pregunta,)

#Concatenamos las tuplas ('¿', ) + pregunta_tupla + ('?', )
resultado = ('¿',) + pregunta_tupla + ('?',)

#Imprimimos la tupla resultante
print("Tupla con signos:", resultado)

#Repetimos la tupla dos veces
repetido = resultado * 2

#Imprimimos la tupla repetida
print("Tupla repetida:", repetido)