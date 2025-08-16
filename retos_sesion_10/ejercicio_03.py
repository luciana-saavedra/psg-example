tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

conjunto_fisica = set(tienda_fisica)
conjunto_online = set(tienda_online)

#Compraron en ambos canales
compraron_en_ambos = conjunto_fisica & conjunto_online

#Compraron solo en la tienda física
compraron_solo_fisica = conjunto_fisica - conjunto_online

#Compraron solo en la tienda online
compraron_solo_online = conjunto_online - conjunto_fisica

print("Compraron en ambos canales:", compraron_en_ambos)
print("Compraron solo en la tienda física:", compraron_solo_fisica)
print("Compraron solo online:", compraron_solo_online)