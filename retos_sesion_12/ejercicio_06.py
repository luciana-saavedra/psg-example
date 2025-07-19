entrada = input("Ingrese los datos en este formato: número1, número2, operación(+, -, *, /): ")

#Separamos los tres valores usando split y quitamos espacios con strip
num1_str, num2_str, operacion = entrada.split(",")
num1 = float(num1_str.strip())
num2 = float(num2_str.strip())
operacion = operacion.strip()

#Verificamos qué operación quiere hacer el usuario
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero" #No se puede dividir entre 0
else:
    resultado = "Operación no válida" #Porque la operación no está dentro de las que nuestra calculadora ofrece

#Mostramos el resultado
print("-------------")
print("Resultado:", resultado)