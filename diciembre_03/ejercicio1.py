# BY GLORIA
# Listas originales
catalogo_a = ["rojo", "azul", "verde", "amarillo", "azul", "negro"]
catalogo_b = ["violeta", "rojo", "blanco", "verde", "negro", "negro"]

# Convertir a sets
set_a = set(catalogo_a)
set_b = set(catalogo_b)

print("\n🎨 CATÁLOGOS ORIGINALES:")
print("A:", set_a)
print("B:", set_b)

# Operaciones entre sets
union = set_a.union(set_b)
interseccion = set_a.intersection(set_b)
solo_a = set_a.difference(set_b)
solo_b = set_b.difference(set_a)

print("\n🟣 Unión (todos sin duplicados):", union)
print("🟠 Intersección (colores en ambos):", interseccion)
print("🟡 Sólo en A:", solo_a)
print("🔵 Sólo en B:", solo_b)

# Agregar color a A
nuevo_color = input("\nIngrese un nuevo color para agregar a catálogo A: ")
set_a.add(nuevo_color)

# liminar color de B
color_borrar = input("Ingrese un color para eliminar de catálogo B: ")
set_b.discard(color_borrar)

print("\n📦 RESULTADOS ACTUALIZADOS:")
print("Catálogo A:", set_a)
print("Catálogo B:", set_b)

print("\n✔ Operación completada con éxito\n")