# MANEJO DE LISTAS
# PROCESOS
listaDeElementos = []
listaPares = []
listaImpares = []
listaPositivos = []
listaNegativos = []
producto = 1
productoPositivos = 1
productoNegativos = 1
productoPares = 1
productoImpares = 1

# ENTRADAS
cantidadInputValidacion = False
while not cantidadInputValidacion:
    cantidadElementos = int(input(
        "Digite la cantidad de elementos a ingresar en la lista: "))
    cantidadInputValidacion = str(cantidadElementos).isdigit()
    if not cantidadInputValidacion:
        print("Por favor digite un número entero")

for item in range(cantidadElementos):
    numeroValido = False
    while not numeroValido:
        elemento = input(f"Digite el elemento # {item}: ")
        numeroValido = elemento.isdigit() or elemento <= "0"
        if not numeroValido:
            print("Por favor digite un número entero")
        else:
            listaDeElementos.append(int(elemento))

for x in range(cantidadElementos):
    producto = producto * listaDeElementos[x]
    if listaDeElementos[x] >= 0:
        listaPositivos.append(listaDeElementos[x])
        productoPositivos = productoPositivos * listaDeElementos[x]
    else:
        listaNegativos.append(listaDeElementos[x])
        productoNegativos = productoNegativos * listaDeElementos[x]
    if listaDeElementos[x] % 2 == 0:
        listaPares.append(listaDeElementos[x])
        productoPares = productoPares * listaDeElementos[x]
    else:
        listaImpares.append(listaDeElementos[x])
        productoImpares = productoImpares * listaDeElementos[x]

# SALIDAS
if len(listaDeElementos) > 0:
    print("=======================================================================")
    print("Lista: ", listaDeElementos)
    print("Tamaño de la lista: ", len(listaDeElementos))
    print("Elementos de la lista: ", len(listaDeElementos))
    print("Suma de los elementos de la lista: ", sum(listaDeElementos))
    print("Elemento mas Grande la lista: ", max(listaDeElementos))
    print("Elemento menor la lista: ", min(listaDeElementos))
    print("Promedio de la lista: ", sum(
        listaDeElementos) / len(listaDeElementos))
    print("Producto de los elementos de la lista: ", producto)
else:
    print("Lista de números vacia, no se pudo realizar operaciones")

if len(listaPositivos) > 0:
    print("=======================================================================")
    print("Lista números positivos: ", listaPositivos)
    print("Tamaño de la lista: ", len(listaPositivos))
    print("Elementos de la lista: ", len(listaPositivos))
    print("Suma de los elementos de la lista: ", sum(listaPositivos))
    print("Elemento mas grande la lista: ", max(listaPositivos))
    print("Elemento menor la lista: ", min(listaPositivos))
    print("Promedio de la lista: ", sum(listaPositivos) / len(listaPositivos))
    print("Producto de los elementos de la lista: ", productoPositivos)
else:
    print("Lista de números positivos vacia, no se pudo realizar operaciones")

if len(listaNegativos) > 0:
    print("=======================================================================")
    print("Lista números negativos: ", listaNegativos)
    print("Tamaño de la lista: ", len(listaNegativos))
    print("Elementos de la lista: ", len(listaNegativos))
    print("Suma de los elementos de la lista: ", sum(listaNegativos))
    print("Elemento mas Grande la lista: ", max(listaNegativos))
    print("Elemento menor la lista: ", min(listaNegativos))
    print("Promedio de la lista: ", sum(listaNegativos) / len(listaNegativos))
    print("Producto de los elementos de la lista: ", productoNegativos)
else:
    print("Lista de números negativos vacia, no se pudo realizar operaciones")

if len(listaPares) > 0:
    print("=======================================================================")
    print("Lista números pares: ", listaPares)
    print("Tamaño de la lista: ", len(listaPares))
    print("Elementos de la lista: ", len(listaPares))
    print("Suma de los elementos de la lista: ", sum(listaPares))
    print("Elemento mas grande la lista: ", max(listaPares))
    print("Elemento menor la lista: ", min(listaPares))
    print("Promedio de la lista: ", sum(listaPares) / len(listaPares))
    print("Producto de los elementos de la lista: ", productoPares)
else:
    print("Lista de números pares vacia, no se pudo realizar operaciones")

if len(listaImpares) > 0:
    print("=======================================================================")
    print("Lista números imPares", listaImpares)
    print("Tamaño de la lista: ", len(listaImpares))
    print("Elementos de la lista: ", len(listaImpares))
    print("Suma de los elementos de la lista: ", sum(listaImpares))
    print("Elemento mas Grande la lista: ", max(listaImpares))
    print("Elemento menor la lista: ", min(listaImpares))
    print("Promedio de la lista: ", sum(listaImpares) / len(listaImpares))
    print("Producto de los elementos de la lista: ", productoImpares)
else:
    print("Lista de números impares vacia, no se pudo realizar operaciones")
print("=======================================================================")
