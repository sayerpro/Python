# Arreglo
# ENTRADAS
print("===============================================")
whilevalidation = False
while not whilevalidation:
    cantidadIteraciones = input(
        "Digite la cantidad total de datos que desea ingresar: ")
    whilevalidation = cantidadIteraciones.isdigit()
    if not whilevalidation:
        print("Por favor digite un número entero")

# PROCESOS
lista = []

for item in range(int(cantidadIteraciones)):
    whilevalidation2 = False
    while not whilevalidation2:
        dato = input(f"Digite el dato de la posición #{item + 1}: ")
        whilevalidation2 = dato.isdigit()
        if not whilevalidation2:
            print("Por favor digite un número entero")
        else:
            lista.append(dato)
lista.reverse()
# SALIDAS

print(f"Se imprime de manera invertida según el orden de ingreso: ", lista)
print("===============================================")
