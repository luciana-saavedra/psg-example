tupla_especies = (('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅']))

#Convertimos tupla a diccionario
diccionario_especies = dict(tupla_especies)

#Obtenemos y eliminamos el valor de la clave 'aves'
aves = diccionario_especies.pop('aves')
print(f"Especies de aves eliminadas: {aves}")

#Modificamos el valor de la clave 'felino'
diccionario_especies['felino'] = '🐈'

#Cambiamos la clave 'canino' por 'caninos' y su valor por lista
diccionario_especies['caninos'] = ['🐶', '🐕']
diccionario_especies.pop('canino')

#Diccionario modificado
print(f"Diccionario de especies modificado:\n{diccionario_especies}")