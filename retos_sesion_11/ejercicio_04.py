#Diccionario de hábitats y especies en peligro
habitats = {
    "polo norte": {"especies": {"oso polar", "morsa", "ballena"}},
    "amazonas": {"especies": {"tigre", "mono", "guacamayo"}}
}

#Añadimos 2 hábitats más usando update()
habitats.update({
    "sabana africana": {"especies": {"león", "elefante"}},
    "bosque boreal": {"especies": {"alce", "lobo"}}
})

#Verificamos si 'amazonas' está en el diccionario
print(f"¿Existe el hábitat 'amazonas'? {'amazonas' in habitats}")

#Añadimos 'anaconda' al hábitat 'amazonas'
habitats["amazonas"]["especies"].add("anaconda")

#Diccionario actualizado de hábitats
print(f"Diccionario de hábitats actualizado:\n{habitats}")