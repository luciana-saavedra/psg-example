#Excepción para frutas no permitidas
class FrutaNoPermitidaError(Exception):
    pass

#Lista de frutas permitidas
frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]

#Lista para almacenar frutas ingresadas
canasta = []

while True:
    #Solicitar fruta o salir
    fruta = input("Ingresa una fruta (o 'salir' para terminar): ")
    if fruta.lower() == "salir":
        print("programa finalizado")
        break

    try:
        #Verificar si la fruta está permitida
        if fruta not in frutas_permitidas:
            raise FrutaNoPermitidaError(f"'{fruta}' no es una fruta permitida.")

        #Agregar fruta a la canasta
        canasta.append(fruta)
        print(f"{fruta} añadida a la canasta.")

    #Manejo de fruta no permitida
    except FrutaNoPermitidaError as error:
        print(error)

#Mostrar canasta final
print("\n Canasta final:", canasta)
