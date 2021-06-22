# NÓMINA EMPLEADOS
# ENTRADAS
print("==========================================================")
print("Datos del Empleado")
print("__________________")
cedula = (input("Digite el número de cédula: "))
nombre = (input("Digite el nombre: "))
salario = int(input("Digite el valor del salario total: "))
dias = int(input("Digite el total de días trabajados: "))
recargoNocturnoPregunta = "Esperando"
while recargoNocturnoPregunta != "Si" and recargoNocturnoPregunta != "No":
    recargoNocturnoPregunta = input(
        ("El trabajador tiene recargo nocturno Si / No: "))
    if recargoNocturnoPregunta != "Si" and recargoNocturnoPregunta != "No":
        print("Por favor ingrese una opción valida")
horasExtraDiurnas = int(input("Digite el total de horas extra diurnas: "))
horasExtraNocturnas = int(input("Digite el total de horas extra nocturnas: "))
horasExtraFestivas = int(
    input("Digite el total de horas extra en días festivos: "))
horasExtraFestivasNocturnas = int(
    input("Digite el total de horas extra en días festivos: "))
prestamo = int(input("Digite el valor prestado: "))
print("==========================================================")

# PROCESOS
minimunSalary = 908526
transportSubsidy = 106454
if salario <= (minimunSalary * 2):
    subsidio = transportSubsidy / 30 * dias
else:
    subsidio = 0

sueldo = salario / 30 * dias
valueOvertimeHours = salario / 240 * horasExtraDiurnas * 1.25
valueOvertimeHoursNight = salario / 240 * horasExtraNocturnas * 1.35
valueOvertimeHoursHolidays = salario / 240 * horasExtraFestivas * 1.75
valueOvertimeHoursHolidaysNight = salario / \
    240 * horasExtraFestivasNocturnas * 2.1

if recargoNocturnoPregunta == "Si":
    recargoNocturno = salario * 0.35
else:
    recargoNocturno = 0

totalDevengado = sueldo + subsidio + valueOvertimeHours + valueOvertimeHoursNight + \
    valueOvertimeHoursHolidays + valueOvertimeHoursHolidaysNight + recargoNocturno

salud = (totalDevengado - subsidio) * 4 / 100
pension = (totalDevengado - subsidio) * 4 / 100

if salario >= (minimunSalary * 4):
    fondoSolidario = salario * 0.01
else:
    fondoSolidario = 0

totalDeducido = salud + pension + prestamo + fondoSolidario
netoPagado = totalDevengado - totalDeducido

# SALIDAS
print("==========================================================")
print("TOTAL NÓMINA")
print("Nombre del empleado: ", nombre)
print("Número de cédula del empleado: ", cedula)
print("Días trabajados por el empleado: ", dias)
print("Recargo nocturno: ", recargoNocturnoPregunta, " / ", recargoNocturno)
print("Horas extras diurnas del empleado: ",
      horasExtraDiurnas, " / ", valueOvertimeHours)
print("Horas extras nocturnas del empleado: ",
      horasExtraNocturnas, " / ", valueOvertimeHoursNight)
print("Horas extras diurnas festivas del empleado: ",
      horasExtraFestivas, " / ", valueOvertimeHoursHolidays)
print("Horas extras nocturnas festivas del empleado: ",
      horasExtraFestivasNocturnas, " / ", valueOvertimeHoursHolidaysNight)
print("Prestamo hecho por el empleado del empleado: ", prestamo)
print("Pago a la salud: ", salud)
print("Pago a la pensión: ", pension)
print("Pago al fondo solidario: ", fondoSolidario)
print("TOTAL DEVENGADO: ", totalDevengado)
print("TOTAL DEDUCIDO: ", totalDeducido)
print("TOTAL NETO PAGADO AL EMPLEADO: ", netoPagado)
print("==========================================================")
