productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Doritos", "Snickers"]
precios = [5.50, 3.20, 2.00, 6.00, 7.50]

#1. Agregar 2 productos nuevos al final de las listas
productos.append("Glacitas")
precios.append(4.75)
productos.append("Takis")
precios.append(8.25)

print("Listas después de agregar productos:")
print(productos)
print(precios)

#2. Eliminar "Bon Bon Bum" y su precio
indice_bonbon = productos.index("Bon Bon Bum")
productos.pop(indice_bonbon)
precios.pop(indice_bonbon)

print("\nListas después de eliminar 'Bon Bon Bum':")
print(productos)
print(precios)

#3. Precio de "Oreo" y "Chizitos"
print("\nOreo cuesta:", precios[productos.index("Oreo")])
print("Chizitos cuesta:", precios[productos.index("Chizitos")])

#4. Producto más caro y más barato
indice_max = precios.index(max(precios))
indice_min = precios.index(min(precios))
print(f"\nProducto más caro: {productos[indice_max]} - Bs.{precios[indice_max]}")
print(f"Producto más barato: {productos[indice_min]} - Bs.{precios[indice_min]}")

#5. ¿Cuántos productos tienes en total?
print(f"\nTotal de productos: {len(productos)}")

# 6. ¿Cuánto cuestan todos los productos?
print(f"Costo total de todos los productos: Bs.{sum(precios):.2f}")

# 7. Ordenar productos y precios de más barato a más caro
precios_ordenados = precios.copy()
productos_ordenados = []

#Ordenamos precios
precios_ordenados.sort()

#Relacionamos productos según precios ordenados
productos_ordenados.append(productos[precios.index(precios_ordenados[0])])
productos_ordenados.append(productos[precios.index(precios_ordenados[1])])
productos_ordenados.append(productos[precios.index(precios_ordenados[2])])
productos_ordenados.append(productos[precios.index(precios_ordenados[3])])
productos_ordenados.append(productos[precios.index(precios_ordenados[4])])
productos_ordenados.append(productos[precios.index(precios_ordenados[5])])

print("\nProductos ordenados de más barato a más caro:", productos_ordenados)
print("Precios ordenados de más barato a más caro:", precios_ordenados)

#8. Eliminar todos los productos y precios
productos.clear()
precios.clear()
print("\nListas después de eliminar todos los productos:", productos, precios)