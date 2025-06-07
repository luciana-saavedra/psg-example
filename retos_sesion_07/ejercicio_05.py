cadena = input("Ingresa una frase: ")
cadena_limpia = cadena.replace(" ", "").lower()
if cadena_limpia == cadena_limpia[::-1]:
    print("True")
else:
    print("False")