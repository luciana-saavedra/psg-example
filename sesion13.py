range(5)
range(1, 10, 2)
print(list(range(5)))

print ("Inicio")
for i in range(5): # rango (0,5,1)
    print(i)
print ("Fin")

#Ejemplo 1, sumar los números del 1 al 10 de 2 en 2
print ("Ejemplo 1")
suma = 0
for i in range(1, 11, 2): # 1, 3, 5, 7, 9
    suma = suma + i #suma += i
print(suma)

#Ejemplo 2, crear un árbol de navidad de 6 niveles

print ("Ejemplo 2")
for i in range(0, 6):
    print(" "*(5-i) + "*"*i*2+"*")

#Ejemplo 3, crear una serie de números cuadrados del 1 al 10

print ("Ejemplo 3")
for i in range(1, 11):
    print(i**2, end=" ")

#Ejemplo 4, crear una lista de números pares del 1 al 10

print ("Ejemplo 4")
pares = []
for i in range(0, 11, 2):
    pares.append(i)
print(pares)

#Ejercicio en clase: Ejercicio 1, imprimir los 10 primeros de la serie números cúbicos
for i in range(1,11):
    print(i**3,end="," if i<10 else "")

for fruta in ['🍎','🍌','🍇','🍉']:
    print(fruta)

print ("Ejemplo 5")
fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
for objeto in fiesta:
    print(objeto)

print ("Ejemplo 6")
frutas =  ('🍅','🍇','🍈','🍉','🍊')
for fruta in frutas:
    print(fruta, end=", ")

print ("Ejemplo 7")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
for clave in frutas:
    print(clave, frutas[clave])

#Ejemplo 8, imprimir los elementos del ciclo de vida de un pollo con flechas
print ("Ejemplo 8")
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(etapa, end="->")

#Ejemplo 9, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
print ("Ejemplo 9")
animales = ['🐶','🐱','🐰','🐭']
for animal in animales:
    print(animal)

#Ejemplo 10, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
print ("Ejemplo 10")
animales = ['🐶','🐱','🐰','🐭']
for i in range(len(animales)):
    print(animales[i])

#Ejemplo 11, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']
print ("Ejemplo 11")
animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal, animales[i])

print ("Ejemplo 11")
#animales = ['🐶','🐱','🐰','🐭']
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
print (list(enumerate(frutas)))
for i, fruta in enumerate(frutas):
    print(i, fruta, frutas[fruta])

#Ejercicio 2, imprimir la cantidad de veces los elementos de la cadena '⚽🏀🏐🎱' de acuerdo a su posición más 1
esferas = '⚽🏀🏐🎱'
for i, elemento in enumerate(esferas):
    print(elemento*(i+1))

print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1

print ("Ejemplo 13")
suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print(suma)

print ("Ejercicio en clase")
numero = int(input("Ingrese un número: "))
while numero >= 0:
    print(numero)
    numero -= 1

frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14 con for")
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print ("Fin")

frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14 con while")
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print ("Fin")

print ("Ejemplo 15")
contador = 0
while True:
    print(contador)
    contador += 1

print ("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == 'salir':
        break
    print(texto.upper())
print ("Fin")

print ("Ejercicio en clase")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print ("Par" if numero % 2 == 0 else "Impar")

print ("Ejemplo 17")
pares = [i for i in range(2, 11, 2)]
print(pares)

print ("Ejemplo 18")
pares = [i for i in range(2, 11) if i % 2 == 0]
print(pares)

print ("Ejemplo 19")
pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
print(pares)

print ("Ejercicio en clase")
impares = tuple(i for i in range(1, 11) if i % 2 != 0)
print(impares)

print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

print ("Ejemplo 21")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print(f"Tabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
print ("Fin")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()

print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)

print ("Ejercicio en clase")
n = int(input("Ingrese un número: "))
matriz = [[(j, i) for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)