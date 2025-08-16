personas = ["Ana", "Luciana", "Kathleen", "Lucy", "Steph", "Elisa", "Alejandra", "José", "Brisa", "Dylan"]

#Sublista del índice 5 al 9 con saltos de 2
sublista = personas[5:10:2]
print("Sublista (índices 5 a 9 con saltos de 2):", sublista)

#Verificar si "José" está en la lista original
existe_jose = "José" in personas
print("¿'José' está en la lista original?:", existe_jose)

#Ordenar sublista alfabéticamente de A a Z
sublista_ordenada = sublista.copy()
sublista_ordenada.sort()
print("Sublista ordenada (A-Z):", sublista_ordenada)

#Ordenar lista original de Z a A
personas_ordenada_desc = personas.copy()
personas_ordenada_desc.sort(reverse=True)
print("Lista original ordenada (Z-A):", personas_ordenada_desc)