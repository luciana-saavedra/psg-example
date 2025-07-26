#Inicializamos los dos primeros términos de la sucesión de Lucas
a, b = 2, 1
print("Sucesión de Lucas:")
#Usamos un ciclo for para imprimir los primeros 20 términos
for i in range(20):
    print(a, end=", ")
    a, b = b, a + b