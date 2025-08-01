#Pedimos los datos al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ").strip()

def calcular(num1, num2, operacion):
    # Verificamos qué operación se solicita
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: no se puede dividir entre cero"
    else:
        return "Operación inválida"

#Mostramos el resultado
print("El resultado es:", calcular(num1, num2, operacion))