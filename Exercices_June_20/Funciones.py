# FUNCIONES
# PROCESOS
import winsound


def lastName(name):
    lastName = "Smith"
    name = f"{name} {lastName}"
    return name


print("===================================")
# ENTRADAS
name = input("Digite su nombre: ")

# SALIDAS
print(name)
name = lastName(name)
print(name)
print("===================================")

frequency = 4500  # Set Frequency To 2500 Hertz
duration = 3000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
