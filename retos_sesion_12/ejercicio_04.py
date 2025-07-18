edad = int(input("Ingrese la edad del cliente: "))
compra = float(input("Monto de la compra: "))

#Aplicamos condiciones según edad y monto de compra
if edad > 60 and compra > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and compra > 500:
    descuento = 0.10
else:
    descuento = 0.02

#Calculamos el precio final después del descuento
monto_final = compra * (1 - descuento)

#Mostramos el descuento aplicado y el monto final
print(f"Se aplicó el descuento de {descuento * 100}% y el monto final es {monto_final}")