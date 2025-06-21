#Listas iniciales
productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Doritos", "Snickers"]
precios = [5.50, 3.20, 2.00, 6.00, 7.50]
print(productos)
print(precios)
#1.Agregar 2 productos nuevos al final de las listas
productos.append("Glacitas")
precios.append(4.75)

productos.append("Takis")
precios.append(8.25)

print("Listas después de agregar productos:")
print(productos)
print(precios)

#2.Eliminar el producto "Bon Bon Bum" y su precio asociado
indice_bonbon = productos.index("Bon Bon Bum")
productos.pop(indice_bonbon)
precios.pop(indice_bonbon)

print("\nListas después de eliminar 'Bon Bon Bum':")
print(productos)
print(precios)

#3.¿Cuánto cuesta "Oreo" y "Chizitos"?
indice_oreo = productos.index("Oreo")
precio_oreo = precios[indice_oreo]
print("Oreo cuesta:", precio_oreo)

indice_chizitos = productos.index("Chizitos")
precio_chizitos = precios[indice_chizitos]
print("Chizitos cuesta:", precio_chizitos)

#4.Producto más caro y más barato
precio_max = max(precios)
indice_max = precios.index(precio_max)
producto_mas_caro = productos[indice_max]

precio_min = min(precios)
indice_min = precios.index(precio_min)
producto_mas_barato = productos[indice_min]

print(f"\nProducto más caro: {producto_mas_caro} - Bs.{precio_max}")
print(f"Producto más barato: {producto_mas_barato} - Bs.{precio_min}")

#5.¿Cuántos productos tienes en total?
total_productos = len(productos)
print(f"\nTotal de productos: {total_productos}")

#6.¿Cuánto cuestan todos los productos?
costo_total = sum(precios)
print(f"\nCosto total de todos los productos: Bs.{costo_total:.2f}")

#7.Ordenar productos y precios de más barato a más caro
productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Doritos", "Snickers", "Glacitas", "Takis"]
precios = [5.50, 3.20, 2.00, 6.00, 7.50, 4.75, 8.25]

#Copiar y ordenar precios
precios_ordenados = precios.copy()
precios_ordenados.sort()

#Creamos una lista vacía para productos ordenados
productos_ordenados = []

#Agregamos uno a uno según el precio ordenado
productos_ordenados.append(productos[precios.index(precios_ordenados[0])])
productos_ordenados.append(productos[precios.index(precios_ordenados[1])])
productos_ordenados.append(productos[precios.index(precios_ordenados[2])])
productos_ordenados.append(productos[precios.index(precios_ordenados[3])])
productos_ordenados.append(productos[precios.index(precios_ordenados[4])])
productos_ordenados.append(productos[precios.index(precios_ordenados[5])])

print("Productos ordenados de más barato a más caro:")
print(productos_ordenados)

print("Precios ordenados de más barato a más caro:")
print(precios_ordenados)

#8.Eliminar todos los productos de las listas
productos.clear()
precios.clear()

print("\nListas después de eliminar todos los productos:")
print(productos)
print(precios)