# OPERADORES DE ASIGNACIÓN
# ENTRADAS
print("============================================")
x = int(input("Digite el valor de X: "))
y = int(input("Digite el valor de Y: "))
print("============================================")

# PROCESOS
r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = r10 = r11 = r12 = r13 = x
r1 = y    # x = y
r2 += y	  # x = x + y
r3 -= y	  # x = x - y
r4 *= y	  # x = x * y
r5 /= y	  # x = x / y
r6 %= y	  # x = x % y
r7 //= y  # x = x // y
r8 **= y  # x = x ** y
r9 &= y	  # x = x & y
r10 |= y  # x = x | y
r11 ^= y  # x = x ^ y
r12 >>= y  # x = x >> y
r13 <<= y  # x = x << y

# SALIDAS
print("===========================================================================")
print("RESULTADO OPERADORES DE ASIGNACIÓN")
print("(x = y) ASIGNACIÓN: ", r1)
print("(x += y) SUMA SU VALOR CON OTRO: ", r2)
print("(x -= y) RESTA SU VALOR CON OTRO: ", r3)
print("(x *= y) MULTIPLICA SU VALOR CON OTRO: ", r4)
print("(x /= y) DIVIDE SU VALOR CON OTRO: ", r5)
print("(x %= y) SACA SU PORCENTAJE ACORDE AL OTRO VALOR: ", r6)
print("(x //= y) MUESTRA CUÁNTAS VECES PUEDE CABER UN VALOR EN EL OTRO: ", r7)
print("(x **= y) POTENCIA SU VALOR POR LA CANTIDAD DE VECES DEL OTRO VALOR: ", r8)
print("(x &= y) COMPARACIÓN: ", r9)
print("(x |= y) COMPARACIÓN: ", r10)
# symmetric_difference_update ()
print("(x ^= y) ENCUENTRA LA DIFERENCIA SIMÉTRICA DE DOS CONJUNTOS: ", r11)
print("(x >>= y) CORRE UNA CANTIDAD DE VECES LOS BITS A LA DERECHA: ", r12)  # x/(2**y)
print("(x <<= y) CORRE UNA CANTIDAD DE VECES LOS BITS A LA IZQUIERDA: ", r13)  # x(2**y)
print("===========================================================================")
