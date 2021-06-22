# DEFINIR EL NÚMERO CENTRAL
# ENTRADAS
print("==========================================================")
numero1 = int(input("Digite el valor del número 1: "))
numero2 = int(input("Digite el valor del número 2: "))
numero3 = int(input("Digite el valor del número 3: "))
print("==========================================================")

# PROCESOS
if numero1 > numero2:
    if numero1 > numero3:
        if numero2 > numero3:
            mayor = numero1
            central = numero2
            menor = numero3
        else:
            mayor = numero1
            central = numero3
            menor = numero2
if numero2 > numero1:
    if numero2 > numero3:
        if numero1 > numero3:
            mayor = numero2
            central = numero1
            menor = numero3
        else:
            mayor = numero2
            central = numero3
            menor = numero1
if numero3 > numero1:
    if numero3 > numero2:
        if numero1 > numero2:
            mayor = numero3
            central = numero1
            menor = numero2
        else:
            mayor = numero3
            central = numero2
            menor = numero1

# SALIDAS
print("==========================================================")
print("RESULTADO DEFINIR EL NÚMERO CENTRAL")
print("El número mayor es: ", mayor)
print("El número central es: ", central)
print("El número menor es: ", menor)
print("==========================================================")

# Este Algoritmo comentado, tambien funciona correctamente, pero es una version menos compacta
# numero1 = 12
# numero2 = 10
# numero3 = 11

# if (numero1 > numero2):
#     if (numero1 > numero3):
#         if (numero2 > numero3):
#             mayor = numero1
#             central = numero2
#             menor = numero3
#         else:
#             mayor = numero1
#             central = numero3
#             menor = numero2
# if (numero1 > numero3):
#     if (numero1 > numero2):
#         if (numero2 > numero3):
#             mayor = numero1
#             central = numero2
#             menor = numero3
#         else:
#             mayor = numero1
#             central = numero3
#             menor = numero2
# if numero2 > numero1:
#     if numero2 > numero3:
#         if numero1 > numero3:
#             mayor = numero2
#             central = numero2
#             menor = numero3
#         else:
#             mayor = numero2
#             central = numero3
#             menor = numero1
# if numero2 > numero3:
#     if numero2 > numero1:
#         if numero1 > numero3:
#             mayor = numero2
#             central = numero1
#             menor = numero3
#         else:
#             mayor = numero2
#             central = numero3
#             menor = numero1
# if numero3 > numero1:
#     if numero3 > numero2:
#         if numero1 > numero2:
#             mayor = numero3
#             central = numero1
#             menor = numero2
#         else:
#             mayor = numero3
#             central = numero2
#             menor = numero1
# if numero3 > numero2:
#     if numero3 > numero1:
#         if numero1 > numero2:
#             mayor = numero3
#             central = numero1
#             menor = numero2
#         else:
#             mayor = numero3
#             central = numero2
#             menor = numero1

# print("Mayor", mayor)
# print("Central", central)
# print("Menor", menor)
