# CÁLCULO CALIFICACIÓN NOTAS
# ENTRADAS
print("==========================================================")
name = input("Digite el nombre del estudiante: ")
document = input("Digite la cédula del estudiante: ")
calification = float(input("Digite la nota del estudiante: "))
print("==========================================================")

# PROCESOS
if(calification >= 4.5 and calification <= 5.0):
    result = "A"
elif(calification >= 4.0 and calification <= 4.4):
    result = "B"
elif(calification >= 3.5 and calification <= 3.9):
    result = "C"
elif(calification >= 3.0 and calification <= 3.4):
    result = "D"
elif(calification >= 2.5 and calification <= 2.9):
    result = "E1"
elif(calification >= 2.0 and calification <= 2.4):
    result = "E2"
elif(calification >= 1.5 and calification <= 1.9):
    result = "E3"
elif(calification >= 1.0 and calification <= 1.4):
    result = "E4"
else:
    result = "La nota ingresada esta fuera del rango entre 1.0 y 5.0"

# SALIDAS
print("==========================================================")
print("El nombre del estudiante es: ", name)
print("El número de documento del estudiante es: ", document)
print("La calificación númerica del estudiante es: ", calification)
print("La calificación de la nota final es: ", result)
print("==========================================================")
