pregunta_texto = input("Escribe una pregunta (sin signos de interrogación): ")
pregunta_tupla = tuple(pregunta_texto)

resultado = ('¿',) + pregunta_tupla + ('?',)

print("Resultado concatenado:", resultado)

repetido = resultado * 2
print("Tupla repetida 2 veces:", repetido)