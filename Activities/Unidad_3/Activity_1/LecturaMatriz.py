# Arreglo
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

for item in matriz:
    for element in item:
print("===============================================")
