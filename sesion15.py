print ("Inicio Ejemplo 1")
x = 1 / 0
print (x)
print ("Fin Ejemplo 1")

print ("Inicio Ejemplo 1")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")

#Ejercicio 1, Crear un programa que solicite 
# dos números y realice la división de ambos 
# números Si hay un error mostrar un mensaje 
# de error El programa se detiene si se ingresa "salir"
print ("Ejercicio en clase 1")
while True:
    try:
        num_1 = input("Ingrese el primer número: ")
        if num_1 == "salir":
            print("el programa finalizó")
            break
        num_2 = input("Ingrese el segundo número: ")
        if num_2 == "salir":
            print("el programa finalizó")
            break
        num_1 = float(num_1)
        num_2 = float(num_2)
        print("El resultado es:", num_1 / num_2)
    except Exception as error:
        print("Error:", error)

print ("Solución 1")
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        print("Resultado:", num1 / num2)
    except Exception as e:
        print("💀 Error:", e)

print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")

#De la lista de calificaciones, obtener el promedio
print ("Ejemplo 3")
calificaciones = [20,40,80,"A"]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i] 
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))

print ("Inicio Ejemplo 4")
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except Exception as e:
    print("💀 Error:", e, type(e))
else:
    print ("🎉 Sin errores")
print ("Fin Ejemplo 4")

#Ejercicio 2, Crear un programa que solicite dos números 
# y mediante una función devuelva la división de ambos
#Si hay un error mostrar un mensaje de error. El programa 
# se detiene si se ingresa "salir"
#Añadir un bloque else que muestre el resultado de la función
print ("Ejercicio en clase 2")
def division(num_1, num_2):
    return num_1 / num_2
while True:
    try:
        num_1 = input("Ingrese el primer número: ")
        if num_1 == "salir":
            print("el programa finalizó")
            break
        num_2 = input("Ingrese el segundo número: ")
        if num_2 == "salir":
            print("el programa finalizó")
            break
        num_1 = float(num_1)
        num_2 = float(num_2)
        resultado = division(num_1, num_2)
    except Exception as error:
        print("Error!:", error)
    else:
        print("El resultado es: ", resultado)

print ("Solución 2")
def division(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        resultado = division(num1, num2)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Resultado: ",resultado)

print ("Inicio Ejemplo 5")
try:
    print("🔗 Ping...")
except Exception as e:
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")

print ("Inicio Ejemplo 6")
try:
    print("🔗 Ping...")
    raise Exception("Error de conexión") #Excepción genérica
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")

#Ejercicio 3, Escriba un programa que solicite un número por 
#teclado y se almacene en una lista
#Si es 0 se genera una excepción
#Si la ejecución es correcta muestra "🎉Agregado"
#Termina la ejecución sólo con la palabra "salir" utilizar 
#la excepción KeyboardInterrupt
#Finalmente imprima siempre la suma de los números y la lista
print ("Ejercicio en clase 3")
numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            print("el programa finalizó")
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)
    except KeyboardInterrupt as error:
        print("Escriba 'salir' para detener la ejecución del programa:")
    except Exception as error:
        print("Error:", error)
    else:
        print("🎉Agregado")
    finally:
        print("Suma:", sum(numeros))
        print(numeros)

print ("Solución 3")
numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)
    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Número agregado")
    finally:
        print("Suma:", sum(numeros))

print("Inicio Ejemplo 7")
def funcion():
    pass

funcion()
print("Fin Ejemplo 7")

print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass
 
frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")

#Ejercicio 4, Crear un programa que solicite palabras por teclado 
#y almacene en una lista
#Si se inserta caracteres no alfabéticos se genera una excepción personalizada y no se almacena
#Si se ingresa "salir" se termina la ejecución
#Mostrar el mensaje "🎉 Palabra agregada" si no hay errores
#Finalmente imprimir la lista de palabras
print ("Ejercicio en clase 4")
class ErrorNoAlfabetico(Exception):
    pass
palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise ErrorNoAlfabetico("Solo se permiten letras")
        palabras.append(palabra)
    except ErrorNoAlfabetico as error:
        print("Error!:", error)
    except Exception as error:
        print("Error!:", error)
    else:
        print("Palabra agregada a la lista")
    finally:
        print("Lista:", palabras)

print ("Solución 4")
class NoAlfabeticoError(Exception):
    pass

palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise NoAlfabeticoError("Solo se permiten letras")
        palabras.append(palabra)
    except NoAlfabeticoError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Palabra agregada")
    finally:
        print("Lista:", palabras)