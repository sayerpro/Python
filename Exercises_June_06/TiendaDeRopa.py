# FACTURACIÓN TIENDA DE ROPA The Smitheren's
# ENTRADAS
print("==========================================")
print("Bienvenido al sistema de facturación The Smitheren's")
print("CONDICIONES DE COMPRA")
print("________________________")

fecha = input(("Fecha de diligenciamiento: "))
lugar = input(("Lugar de diligenciamiento: "))
nombre = input(("Nombre o Razón social: "))
dirección = input(("Dirección de residencia: "))
referencia = input(("Referencia: "))
telefono = input(("Teléfono: "))
orden = input(("Orden de compra: "))

condicionWhile = True
while condicionWhile:
    condicion = input(
        ("Condiciones de pago Si/No: "))
    condicionWhile = condicion != "Si" and condicion != "No"
    if condicionWhile:
        print("Por favor ingrese una opción valida")

condicionPagoIf = condicion == "Si"
if condicionPagoIf:
    condicionPago = input("Digite las condiciones de pago: ")

condicionWhile2 = True
while condicionWhile2:
    contado = input(
        ("Pago de contado Si/No: "))
    condicionWhile2 = contado != "Si" and contado != "No"
    if condicionWhile2:
        print("Por favor ingrese una opción valida")

if contado == "No":
    credito = input(("Duración del crédito en días: "))

print("\n")
print("ARTÍCULOS ADQUIRIDOS")
print("____________________")

totalArticulos = int(input("Total de artículos adquiridos máximo 12: "))

condicionTotales = 1
while condicionTotales <= totalArticulos:

    print("ARTICULO #", condicionTotales)

    if condicionTotales == 1:
        descripcion1 = input("Descripción del artículo: ")
        precioUnidad1 = int(input("Precio por unidad: "))
        totalUnidades1 = int(input("Total unidades: "))

    if condicionTotales == 2:
        descripcion2 = input("Descripción del artículo: ")
        precioUnidad2 = int(input("Precio por unidad: "))
        totalUnidades2 = int(input("Total unidades: "))

    if condicionTotales == 3:
        descripcion3 = input("Descripción del artículo: ")
        precioUnidad3 = int(input("Precio por unidad: "))
        totalUnidades3 = int(input("Total unidades: "))

    if condicionTotales == 4:
        descripcion4 = input("Descripción del artículo: ")
        precioUnidad4 = int(input("Precio por unidad: "))
        totalUnidades4 = int(input("Total unidades: "))

    if condicionTotales == 5:
        descripcion5 = input("Descripción del artículo: ")
        precioUnidad5 = int(input("Precio por unidad: "))
        totalUnidades5 = int(input("Total unidades: "))

    if condicionTotales == 6:
        descripcion6 = input("Descripción del artículo: ")
        precioUnidad6 = int(input("Precio por unidad: "))
        totalUnidades6 = int(input("Total unidades: "))

    if condicionTotales == 7:
        descripcion7 = input("Descripción del artículo: ")
        precioUnidad7 = int(input("Precio por unidad: "))
        totalUnidades7 = int(input("Total unidades: "))

    if condicionTotales == 8:
        descripcion8 = input("Descripción del artículo: ")
        precioUnidad8 = int(input("Precio por unidad: "))
        totalUnidades8 = int(input("Total unidades: "))

    if condicionTotales == 9:
        descripcion9 = input("Descripción del artículo: ")
        precioUnidad9 = int(input("Precio por unidad: "))
        totalUnidades9 = int(input("Total unidades: "))

    if condicionTotales == 10:
        descripcion10 = input("Descripción del artículo: ")
        precioUnidad10 = int(input("Precio por unidad: "))
        totalUnidades10 = int(input("Total unidades: "))

    if condicionTotales == 11:
        descripcion11 = input("Descripción del artículo: ")
        precioUnidad11 = int(input("Precio por unidad: "))
        totalUnidades11 = int(input("Total unidades: "))

    if condicionTotales == 12:
        descripcion12 = input("Descripción del artículo: ")
        precioUnidad12 = int(input("Precio por unidad: "))
        totalUnidades12 = int(input("Total unidades: "))

    condicionTotales += 1

print("\nForma de pago")
print("1. Efectivo")
print("2. Tarjeta de crédito")
print("3. Tarjeta de débito")
print("4. Cheque")

condicionWhile3 = True
while condicionWhile3:
    formaPago = int(input(
        "Por favor digite el número según la opción de pago: "))
    condicionWhile3 = formaPago != 1 and formaPago != 2 and formaPago != 3 and formaPago != 4
    if condicionWhile3:
        print("Por favor ingrese una opción valida")

condicionTarjeta = formaPago == 2 or formaPago == 3
if condicionTarjeta:
    numeroTarjeta = int(input("Digite el número de tarjeta: "))
    banco = input("Digite el Banco: ")

descuento = int(input(
    "Digite el descuento total solo en números sin el signo de porcentaje(%): "))
recibido = int(input("Total dinero recibido: "))

condicionWhile3 = True
while condicionWhile3:
    iva = input("¿Aplica IVA? Si/No: ")
    condicionWhile3 = iva != "Si" and iva != "No"
    if condicionWhile3:
        print("Por favor ingrese una opción valida")

otros = input("Observaciones adicionales: ")
print("==========================================")

# PROCESOS
baseImponible = 0

condicionTotales = 1
while condicionTotales <= totalArticulos:

    if condicionTotales == 1:
        baseImponible = baseImponible + precioUnidad1 * totalUnidades1
    if condicionTotales == 2:
        baseImponible = baseImponible + precioUnidad2 * totalUnidades2
    if condicionTotales == 3:
        baseImponible = baseImponible + precioUnidad3 * totalUnidades3
    if condicionTotales == 4:
        baseImponible = baseImponible + precioUnidad4 * totalUnidades4
    if condicionTotales == 5:
        baseImponible = baseImponible + precioUnidad5 * totalUnidades5
    if condicionTotales == 6:
        baseImponible = baseImponible + precioUnidad6 * totalUnidades6
    if condicionTotales == 7:
        baseImponible = baseImponible + precioUnidad7 * totalUnidades7
    if condicionTotales == 8:
        baseImponible = baseImponible + precioUnidad8 * totalUnidades8
    if condicionTotales == 9:
        baseImponible = baseImponible + precioUnidad9 * totalUnidades9
    if condicionTotales == 10:
        baseImponible = baseImponible + precioUnidad10 * totalUnidades10
    if condicionTotales == 11:
        baseImponible = baseImponible + precioUnidad11 * totalUnidades11
    if condicionTotales == 12:
        baseImponible = baseImponible + precioUnidad12 * totalUnidades12

    condicionTotales += 1

if formaPago == 1:
    formaDePago = "Efectivo"
elif formaPago == 2:
    formaDePago = "Tarjeta de crédito"
elif formaPago == 3:
    formaDePago = "Tarjeta de débito"
elif formaPago == 4:
    formaDePago = "Cheque"

ivaTotalSuma = 1.19  # 19% Año 2021
ivaTotalResta = 0.19  # 19% Año 2021

totalSinIva = baseImponible - descuento / 100 * baseImponible
if iva == "Si":
    ivaSacado = ivaTotalResta * totalSinIva
    totalIva = "19%"  # 19% Año 2021
    total = ivaTotalSuma * totalSinIva
else:
    ivaSacado = 0
    totalIva = "0%"  # 19% Año 2021
    total = totalSinIva

totalCambio = recibido - total
if totalCambio >= 0:
    deuda = False
else:
    deuda = True

# SALIDAS
print("==========================================")
print("FACTURACIÓN TIENDA DE ROPA The Smitheren's")
print("FACTURA\n")
print(lugar, ", ", fecha)
print("A nombre de: ", nombre)
print("Con dirección de residencia: ", dirección)
print("Teléfono de contacto: ", telefono)
print("Referencia: ", referencia)
print("Orden de compra: ", orden)
print("¿Tiene condiciones de pago?: ", condicion)

if condicionPagoIf:
    print("Las condiciones de pago son: ", condicionPago)

print("Pago de contado: ", contado)
print("Total dinero recibido: ", recibido)
print("\nArticulos adquiridos: ", totalArticulos)

condicionTotales = 1
while condicionTotales <= totalArticulos:

    print("ARTICULO #", condicionTotales)

    if condicionTotales == 1:
        print(descripcion1, ". Precio: ", precioUnidad1,
              ". Cantidad: ", totalUnidades1)
    if condicionTotales == 2:
        print(descripcion2, ". Precio: ", precioUnidad2,
              ". Cantidad: ", totalUnidades2)
    if condicionTotales == 3:
        print(descripcion3, ". Precio: ", precioUnidad3,
              ". Cantidad: ", totalUnidades3)
    if condicionTotales == 4:
        print(descripcion4, ". Precio: ", precioUnidad4,
              ". Cantidad: ", totalUnidades4)
    if condicionTotales == 5:
        print(descripcion5, ". Precio: ", precioUnidad5,
              ". Cantidad: ", totalUnidades5)
    if condicionTotales == 6:
        print(descripcion6, ". Precio: ", precioUnidad6,
              ". Cantidad: ", totalUnidades6)
    if condicionTotales == 7:
        print(descripcion7, ". Precio: ", precioUnidad7,
              ". Cantidad: ", totalUnidades7)
    if condicionTotales == 8:
        print(descripcion8, ". Precio: ", precioUnidad8,
              ". Cantidad: ", totalUnidades8)
    if condicionTotales == 9:
        print(descripcion9, ". Precio: ", precioUnidad9,
              ". Cantidad: ", totalUnidades9)
    if condicionTotales == 10:
        print(descripcion10, ". Precio: ", precioUnidad10,
              ". Cantidad: ", totalUnidades10)
    if condicionTotales == 11:
        print(descripcion11, ". Precio: ", precioUnidad11,
              ". Cantidad: ", totalUnidades11)
    if condicionTotales == 12:
        print(descripcion12, ". Precio: ", precioUnidad12,
              ". Cantidad: ", totalUnidades12)

    condicionTotales += 1

print("\nForma de pago: ", formaDePago)

if condicionTarjeta:
    print("Número de tarjeta: ", numeroTarjeta)
    print("Banco: ", banco, "\n")

print("DESCUENTO TOTAL: ", descuento, "%")
print("APLICA IVA: ", iva, " ", totalIva)
print("COBRO TOTAL IVA: ", ivaSacado)
print("BASE IMPONIBLE: ", baseImponible)
print("TOTAL SIN IVA: ", totalSinIva)
print("TOTAL CON IVA: ", total)
print("TOTAL A PAGAR: ", total)
print("TOTAL RECIBIDO: ", recibido)

if deuda:
    print("TOTAL FALTANTE: ", totalCambio)
else:
    print("TOTAL CAMBIO: ", totalCambio)

print("Observaciones adicionales: ", otros)
print("Muchas gracias por usar nuestro sistema automatizado de facturación - The Smitheren's :)")
print("==========================================")
