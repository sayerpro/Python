# CALCULO NOTAS SEGÚN EL PUNTAJE
# ENTRADAS
print("========================================")
count = 0
curso = 0
pushScore = ""
totalStudents = 0
whileCondition = True
calificationWord = ""
pushCalificacions = ""
sumA = sumB = sumC = sumD = sumF = 0
promedioA = promedioB = promedioC = promedioD = promedioF = 0
aCalification = bCalification = cCalification = dCalification = fCalification = 0
while whileCondition:
    curso += 1
    print("Curso #", curso)
    count = 0
    totalRepetitions = int(
        input("Digite la cantidad de alumnos a calificar: "))
    totalStudents += totalRepetitions
    for count in range(totalRepetitions):
        calificationCondition = False
        while not calificationCondition:
            print("Digite el puntaje del estudiante", count + 1)
            calification = int(input())
            calificationCondition = calification >= 0 and calification <= 100
            if not calificationCondition:
                print("Por favor digite un puntaje entre 0 y 100")

# PROCESOS
        pushScore = pushScore + str(calification) + " "

        if calification >= 90:
            aCalification += 1
            calificationWord = "A"
            sumA += calification
        elif calification >= 80 and calification < 90:
            bCalification += 1
            calificationWord = "B"
            sumB += calification
        elif calification >= 70 and calification < 80:
            cCalification += 1
            calificationWord = "C"
            sumC += calification
        elif calification >= 60 and calification < 70:
            dCalification += 1
            calificationWord = "D"
            sumD += calification
        elif calification < 60:
            fCalification += 1
            calificationWord = "F"
            sumF += calification

        pushCalificacions = pushCalificacions + calificationWord + " "

    whileCondition2 = True
    while whileCondition2:
        restart = input("Desea ingresar otro curso Si/No: ")
        if restart == "Si":
            whileCondition = True
        elif restart == "No":
            whileCondition = False
        whileCondition2 = restart != "Si" and restart != "No"
        if whileCondition2:
            print("Por favor digite una opción valida")

if sumA != 0:
    promedioA = sumA / aCalification
if sumB != 0:
    promedioB = sumB / bCalification
if sumC != 0:
    promedioC = sumC / cCalification
if sumD != 0:
    promedioD = sumD / dCalification
if sumF != 0:
    promedioF = sumF / fCalification

print("========================================")

# SALIDAS
print("========================================")
print("RESULTADOS FINALES")
print("Cursos calificados: ", curso)
print("Total de estudiantes calificados: ", totalStudents)
print("Puntajes ingresados: ", pushScore)
print("Notas finales: ", pushCalificacions)
print("Promedio notas A: ", promedioA)
print("Total estudiantes con nota A: ", aCalification)
print("Promedio notas B: ", promedioB)
print("Total estudiantes con nota B: ", bCalification)
print("Promedio notas C: ", promedioC)
print("Total estudiantes con nota C: ", cCalification)
print("Promedio notas D: ", promedioD)
print("Total estudiantes con nota D: ", dCalification)
print("Promedio notas F: ", promedioF)
print("Total estudiantes con nota F: ", fCalification)
print("========================================")
