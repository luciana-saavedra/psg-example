nombre = input("Nombre: ")
telefono = input("Teléfono: ")

# Verificamos que: el nombre no esté vacío, el número tenga 13 caracteres 
# y comience con '+' y los demás sean números

es_valido = nombre and len(telefono) == 12 and telefono[0] == '+' and telefono[1:].isdigit()

print("-------------")
print("Contacto guardado" if es_valido else "Datos incorrectos")