# METODOS PRINCIPALES EN LISTAS
# PROCESOS
# Agregar un elemento al final de la lista
print("============================================================================")
nombresMasculinos = ["Marcos", "Juan", "Smitherens", "Carlos", "Mercedo"]
nombresMasculinos.append("Joseps")
# SALIDAS
print(nombresMasculinos)

# Agregar varios elemento al final de la lista
nombresFemeninos = ["Lina", "Lauren", "Sandy", "Camil", "Valentin"]
nombresFemeninos.extend(["Luisa", "Carmen"])
print(nombresFemeninos)

# Agregar un elemento en una posición determinada
nombresMasculinos.insert(0, "Ricky")
print(nombresMasculinos)

# Eliminar el ultimo elemento de una lista
nombresFemeninos.pop()
print(nombresFemeninos)

# Eliminar un elemento por su indice
nombresMasculinos.pop(3)
print(nombresMasculinos)

# Eliminar un elemento por su valor
nombresFemeninos.remove("Camil")
print(nombresFemeninos)

# Invertir orden de lista
nombresMasculinos.reverse()
print(nombresMasculinos)

# Ordena una lista en forma ascendente A - Z
nombresFemeninos.sort()
print(nombresFemeninos)

# Ordenar una lista en forma descendente Z - A
nombresMasculinos.sort(reverse=True)
print(nombresMasculinos)

# Contar cantidad de apariciones de los elementos
nombresFemeninos2 = ["Pepa", "Grilla", "Pepa", "Pepa"]
count = nombresFemeninos2.count("Pepa")
print(count)

# Obtener número de índice
index = nombresMasculinos.index("Carlos", 1, 6)
print(index)

# Eliminar elemento de la lista
del nombresFemeninos2[1]
print(nombresFemeninos2)
print("============================================================================")
