jhon_autos = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
jess_autos = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

#Obtenemos los autos en común
autos_comunes = jhon_autos & jess_autos

#Verificamos si existen autos en común
if autos_comunes:
    print("Sí, Jhon y Jess tienen autos en común.")
    print("Autos en común:", autos_comunes)
else:
    print("No hay autos en común entre Jhon y Jess.")
