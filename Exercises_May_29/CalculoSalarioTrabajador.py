# ENCUENTRO SALRIA SEMANAL DE UN TRBAJADOR
# ENTRADAS
print("====================================================================")
hourValue = int(input("Digite el valor por hora del trabajador: "))
hoursMonday = int(input("Digite las horas laboradas el día Lunes: "))
hoursTuesday = int(input("Digite las horas laboradas el día Martes: "))
hoursWednesday = int(input("Digite las horas laboradas el día Miércoles: "))
hoursThursday = int(input("Digite las horas laboradas el día Jueves: "))
hoursFriday = int(input("Digite las horas laboradas el día Viernes: "))
hoursSaturday = int(input("Digite las horas laboradas el día Sabado: "))
print("====================================================================")

# PROCESOS
totalhours = hoursMonday + hoursTuesday + hoursWednesday + \
    hoursThursday + hoursFriday + hoursSaturday
weeklySalary = totalhours * hourValue

# SALIDAS
print("===============================================")
print("Valor de la Hora: ", hourValue)
print("Horas laboradas Lunes: ", hoursMonday)
print("Horas laboradas Martes: ", hoursTuesday)
print("Horas laboradas Miércoles: ", hoursWednesday)
print("Horas laboradas Jueves: ", hoursThursday)
print("Horas laboradas Viernes: ", hoursFriday)
print("Horas laboradas Sabado: ", hoursSaturday)
print("Horas totales laboradas en la semana: ", totalhours)
print("Salario semanal: ", weeklySalary)
print("===============================================")
