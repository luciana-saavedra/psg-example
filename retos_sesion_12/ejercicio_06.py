num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

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
        resultado = "Error: División por cero"  #No se puede dividir entre 0
else:
    resultado = "Operación no válida"  #Porque la operación no está dentro de las que nuestra calculadora ofrece

#Mostramos el resultado final
print("-------------")
print("Resultado:", resultado)