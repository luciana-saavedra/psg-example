#Excepción para fondos insuficientes
class FondosInsuficientesError(Exception):
    pass

#Saldo inicial disponible
saldo_disponible = 5000

while True:
    try:
        #Solicitar monto a retirar o salir
        monto = input("Ingrese el monto a retirar (o 'salir' para terminar): ")
        if monto.lower() == "salir":
            print("programa finalizado")
            break

        #Convertir monto a float
        monto = float(monto)

        #Verificar que el monto sea positivo
        if monto <= 0:
            raise Exception("⚠️ El monto debe ser mayor que 0.")

        #Verificar si hay fondos suficientes
        if monto > saldo_disponible:
            raise FondosInsuficientesError("❌ No hay fondos suficientes.")

        #Verificar límite de retiro
        if monto > 1000:
            raise Exception("⚠️ El monto excede el límite de 1000 por transacción.")

        #Realizar el retiro y mostrar saldo
        saldo_disponible -= monto
        print(f"✅ Retiro exitoso. Saldo restante: {saldo_disponible}")

    #Manejo de fondos insuficientes
    except FondosInsuficientesError as error:
        print(error)
    #Manejo de valor inválido
    except ValueError:
        print("Debes ingresar un número válido!11")
    #Manejo de otros errores
    except Exception as error:
        print(error)
