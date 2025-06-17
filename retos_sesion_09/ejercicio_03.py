personas = ["Ana", "Luciana", "Kathleen", "Lucy", "Steph", "Elisa", "Alejandra", "José", "Brisa", "Dylan"]

#sublista del índice 5 al 9 (sin incluir 9), saltos de 2
sublista = personas[5:9:2]
print("Sublista (índices 5 a 9 con saltos de 2):", sublista)

#verificar si "José" está en la lista original
existe_jose = "José" in personas
print("¿'José' está en la lista original?:", existe_jose)

#ordenar sublista alfabéticamente de A a Z
sublista_ordenada = []
copia_sublista = sublista.copy()
while copia_sublista:
    menor = min(copia_sublista)
    sublista_ordenada.append(menor)
    copia_sublista.remove(menor)

print("Sublista ordenada (A-Z):", sublista_ordenada)

#ordenar lista original de Z a A
personas_ordenada_desc = []
copia_personas = personas.copy()
while copia_personas:
    mayor = max(copia_personas)
    personas_ordenada_desc.append(mayor)
    copia_personas.remove(mayor)

print("Lista original ordenada (Z-A):", personas_ordenada_desc)