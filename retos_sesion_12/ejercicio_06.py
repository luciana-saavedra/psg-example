entrada = input("Ingrese los datos en este formato: número1, número2, operación(+, -, *, /): ")

#Separamos los valores y eliminamos espacios
partes = entrada.split(",")
#Verificamos que el usuario haya ingresado exactamente 3 valores
if len(partes) == 3:
    numero1_str, numero2_str, operacion = partes
    numero1 = float(numero1_str.strip())
    numero2 = float(numero2_str.strip())
    operacion = operacion.strip()

    #Realizamos la operación según el operador
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2 if numero2 != 0 else "Error: División entre cero"
    else:
        resultado = "Operación no válida"
else:
    resultado = "Formato de entrada incorrecto, debe ser: número1, número2, operación"

#Mostramos el resultado
print("-------------")
print("Resultado:", resultado)