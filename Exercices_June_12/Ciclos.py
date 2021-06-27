# CICLOS EN PYTHON
# ENTRADAS
print("================================================")
print("Ciclo While con cantidad de Números")
cantidadNumeros1 = int(input("Cuantos numeros desea utilizar: "))

# PROCESOS
contador1 = suma1 = resta1 = 0
producto1 = 1
while contador1 < cantidadNumeros1:
    numero1 = int(input("Digite un número: "))
    suma1 += numero1
    contador1 += 1
    producto1 *= numero1
    resta1 -= numero1
print("================================================")

# SALIDAS
print("================================================")
print("Cantidad de números: ", contador1)
print("Suma de números: ", suma1)
print("Resta de números: ", resta1)
print("Producto de números: ", producto1)
print("================================================")

# ENTRADAS
print("================================================")
print("Ciclo While solicitando al usuario el repetir proceso")

# PROCESOS
reiniciar2 = "Si"
contador2 = suma2 = resta2 = 0
producto2 = 1
while reiniciar2 == "Si":
    numero2 = int(input("Digite un número: "))
    suma2 += numero2
    contador2 += 1
    producto2 *= numero2
    resta2 -= numero2
    condicionWhile2 = True
    while condicionWhile2:
        reiniciar2 = input("Desea ingresar otro número Si/No: ")
        condicionWhile2 = reiniciar2 != "Si" and reiniciar2 != "No"
        if condicionWhile2:
            print("Por favor ingrese una opción valida")
print("================================================")

# SALIDAS
print("================================================")
print("Suma de números: ", suma2)
print("Cantidad de números: ", contador2)
print("Resta de números: ", resta2)
print("Producto de números: ", producto2)
print("================================================")

# ENTRADAS
print("================================================")
print("Ciclo For con cantidad de Números")
cantidadNumeros3 = int(input("Cuantos numeros desea utilizar: "))

# PROCESOS
contador3 = suma3 = resta3 = 0
producto3 = 1
for contador3 in range(cantidadNumeros3):
    numero3 = int(input("Digite un número: "))
    suma3 += numero3
    contador3 += 1
    producto3 *= numero3
    resta3 -= numero3
print("================================================")

# SALIDAS
print("================================================")
print("Suma de números: ", suma3)
print("Cantidad de números: ", contador3)
print("Resta de números: ", resta3)
print("Producto de números: ", producto3)
print("================================================")
