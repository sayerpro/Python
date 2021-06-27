# CALCULO INTERÉS COMPUESTO DE AHORRO
# ENTRADAS
import os
import math
print("=======================================================================")
initialCapital = int(input("Digite el capital inicial: "))
annualInterestRate = float(
    input("Digite el valor de la tasa de interés anual: "))
weedlyTime = int(input("Digite la duración del ahorro en semanas: "))
print("=======================================================================")

# PROCESOS
finalCapital = initialCapital * (1.0 + annualInterestRate) ** (weedlyTime/52)

# SALIDAS
print("============================================================================================================================")
print("RESULTADO CALCULO INTERÉS COMPUESTO DE AHORRO")
print("El capital total acumulado de ", initialCapital, ", durante ", weedlyTime,
      " semanas, con una tasa de interés anual del: ", annualInterestRate, "%, es de: ", finalCapital)
print("============================================================================================================================")
