# LECTURA DE MATRIZ
# ENTRADAS
print("===============================================")
whilevalidation = False
while not whilevalidation:
    filas = input(
        "Digite la cantidad total de filas que desea ingresar: ")
    whilevalidation = filas.isdigit()
    if not whilevalidation:
        print("Por favor digite un número entero")

whilevalidation2 = False
while not whilevalidation2:
    columnas = input(
        "Digite la cantidad total de columnas que desea ingresar: ")
    whilevalidation2 = columnas.isdigit()
    if not whilevalidation2:
        print("Por favor digite un número entero")

matriz = []

# PROCESOS
for i in range(int(filas)):
    matriz.append([i]*int(columnas))

for item in range(len(matriz)):
    for element in range(len(matriz[item])):
        whilevalidation3 = False
        while not whilevalidation3:
            dato = input(f"Digite el dato de la posicion {item} {element}: ")
            whilevalidation3 = dato.isdigit()
            if not whilevalidation3:
                print("Por favor digite un número entero")
            else:
                matriz[item][element] = dato

print("La matriz quedo de las siguiente forma: ")
for line in matriz:
    print('|  '.join(map(str, line)), "|")
print("===============================================")
