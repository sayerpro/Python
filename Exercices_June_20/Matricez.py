# MATRICEZ
# ENTRADAS
print("================================================================================================================")
cantidadMaterias = int(input("Digite la cantidad de materias: "))
cantidadEstuiantes = int(input("Digite la cantidad de estudiantes: "))

# PROCESOS
cantidadMaterias += 1
cantidadEstuiantes += 1

sumaNotasMaterias = 0
sumaNotasEstudiantes = 0

matriz = []

for i in range(cantidadMaterias):
    matriz.append([i]*cantidadEstuiantes)

for i in range(cantidadMaterias - 1):
    i += 1
    matriz[i][0] = input(f"Digite el nombre de la materia #{i}: ")

for i in range(cantidadEstuiantes - 1):
    i += 1
    matriz[0][i] = input(f"Digite el nombre del estudiante #{i}: ")

for a in range(cantidadMaterias - 1):
    a += 1
    for b in range(cantidadEstuiantes - 1):
        b += 1
        matriz[a][b] = float(input(
            f"Digite la nota de la materia {matriz[a][0]} del estudiante {matriz[0][b]}: "))

for line in matriz:
    print('  '.join(map(str, line)))

for a in range(cantidadMaterias - 1):
    a += 1
    for b in range(cantidadEstuiantes - 1):
        b += 1
        sumaNotasMaterias += float(matriz[a][b])

    # SALIDAS
    print(
        f"El promedio de la materia {matriz[a][0]} es: {sumaNotasMaterias / (cantidadMaterias - 1)}")
    sumaNotasMaterias = 0

for a in range(cantidadEstuiantes - 1):
    a += 1
    for b in range(cantidadMaterias - 1):
        b += 1
        sumaNotasEstudiantes += float(matriz[a][b])
    print(
        f"El promedio del estudiante {matriz[0][a]} es: {sumaNotasEstudiantes / (cantidadEstuiantes - 1)}")
    sumaNotasEstudiantes = 0
print("================================================================================================================")
