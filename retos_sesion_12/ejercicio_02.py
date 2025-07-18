usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

print("Acceso Aprobado" if usuarios.get(usuario) == contraseña else "Acceso Denegado")