#Solicitamos al usuario un número entero
num = int(input("Ingrese un número: "))

#Creamos una función anónima que calcula el valor absoluto
#si el número es mayor o igual a 0, se devuelve tal cual; 
#si es negativo, se multiplica por -1
absoluto = lambda num: num if num >= 0 else -num

#Mostramos el resultado
print("Valor absoluto del número:", absoluto(num))
