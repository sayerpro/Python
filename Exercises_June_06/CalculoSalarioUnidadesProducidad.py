# CÁLCULO SLARIO SEGÚN UNIDADES PRODUCIDAS
# ENTRADAS
print("==========================================================")
print("Datos de lo laborado")
print("__________________")
dias = int(input("Digite el total de días trabajados: "))
unidadesProducidas = int(input("Digite el total de unidades producidas: "))
print("==========================================================")

# PROCESOS
incentivo0 = 0     # 0%
incentivo10 = 1.10  # 10%
incentivo12 = 1.12  # 12%
incentivo14 = 1.14  # 14%
incentivo16 = 1.16  # 16%
ingreso0 = 2
ingreso10 = 2
ingreso12 = 2.5
ingreso14 = 3
ingreso16 = 3.5

semanasTrabajadas = dias/7

if unidadesProducidas > 0 and unidadesProducidas <= 99:
    calculoSueldo = unidadesProducidas * ingreso0 * incentivo0 * semanasTrabajadas
elif unidadesProducidas >= 100 and unidadesProducidas <= 199:
    calculoSueldo = unidadesProducidas * ingreso10 * incentivo10 * semanasTrabajadas
elif unidadesProducidas >= 200 and unidadesProducidas <= 299:
    calculoSueldo = unidadesProducidas * ingreso12 * incentivo12 * semanasTrabajadas
elif unidadesProducidas >= 300 and unidadesProducidas <= 399:
    calculoSueldo = unidadesProducidas * ingreso14 * incentivo14 * semanasTrabajadas
elif unidadesProducidas >= 400:
    calculoSueldo = unidadesProducidas * ingreso16 * incentivo16 * semanasTrabajadas

# SALIDAS
print("==========================================================")
print("CÁLCULO FINAL DEL SALARIO")
print("El salario total es de: ", calculoSueldo)
print("==========================================================")
