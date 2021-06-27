# CÁLCULO ÁREA DE UN TRIÁNGULO
# ENTRADAS
print("==========================================================")
a = int(input("Digite el valor del primer lado del Triángulo: "))
b = int(input("Digite el valor del segundo lado del Triángulo: "))
c = int(input("Digite el valor del tercer lado del Triángulo: "))

print("==========================================================")

# PROCESOS
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# SALIDAS
print("===================================================")
print("RESULTADO CÁLCULO DEL ÁREA DE UN TRIÁNGULO")
print("El área calculada del Triángulo es: ", area)
print("===================================================")
