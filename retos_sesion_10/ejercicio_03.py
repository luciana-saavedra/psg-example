tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

compraron_en_ambos = set(tienda_fisica).intersection(set(tienda_online))
compraron_solo_fisica = set(tienda_fisica).difference(set(tienda_online))
compraron_solo_online = set(tienda_online).difference(set(tienda_fisica))

print("Compraron en ambos canales:", compraron_en_ambos)
print("Compraron solo en la tienda física:", compraron_solo_fisica)
print("Compraron solo online:", compraron_solo_online)