# MUESTREO DE PERSONAS
# ENTRADAS
print("========================================")
count = 0
habit = 0
pushAge = ""
totalPersons = 0
whileCondition = True
category = ""
pushCategory = ""
sumViejos = sumAdultos = sumJovenes = sumNinos = 0
promedioViejos = promedioAdultos = promedioJovenes = promedioNinos = 0
aAge = bAge = cAge = dAge = 0
while whileCondition:
    habit += 1
    print("Curso #", habit)
    count = 0
    totalRepetitions = int(
        input("Digite la cantidad de personas a muestrear: "))
    totalPersons += totalRepetitions
    for count in range(totalRepetitions):
        print("Digite la edad de la persona", count + 1)
        age = int(input())

# PROCESOS
        pushAge = pushAge + str(age) + " "

        if age >= 61:
            aAge += 1
            category = "Viejos"
            sumViejos += age
        elif age >= 31 and age <= 60:
            bAge += 1
            category = "Adultos"
            sumAdultos += age
        elif age >= 14 and age <= 30:
            cAge += 1
            category = "Jovenes"
            sumJovenes += age
        elif age >= 0 and age <= 14:
            dAge += 1
            category = "Niños"
            sumNinos += age

        pushCategory = pushCategory + category + " "

    whileCondition2 = True
    while whileCondition2:
        restart = input("Desea ingresar otra Zona Habitacional Si/No: ")
        if restart == "Si":
            whileCondition = True
        elif restart == "No":
            whileCondition = False
        whileCondition2 = restart != "Si" and restart != "No"
        if whileCondition2:
            print("Por favor digite una opción valida")

if sumViejos != 0:
    promedioViejos = sumViejos / aAge
if sumAdultos != 0:
    promedioAdultos = sumAdultos / bAge
if sumJovenes != 0:
    promedioJovenes = sumJovenes / cAge
if sumNinos != 0:
    promedioNinos = sumNinos / dAge

print("========================================")

# SALIDAS
print("========================================")
print("RESULTADOS FINALES")
print("Zonas Habitacionales muestreadas: ", habit)
print("Total de personas muestreadas: ", totalPersons)
print("Edades ingresadas: ", pushAge)
print("Edades: ", pushCategory)
print("Promedio edad Viejos: ", sumViejos)
print("Total Viejos: ", sumViejos)
print("Promedio edad Aultos: ", sumAdultos)
print("Total Adultos: ", sumAdultos)
print("Promedio edad Jóvenes: ", sumJovenes)
print("Total Jóvenes: ", sumJovenes)
print("Promedio edad niños: ", sumNinos)
print("Total Niños: ", sumNinos)
print("========================================")
