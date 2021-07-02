mensaje = "aja"
punto = "Hola"


def oks(fijo, *arbitrario):
    if arbitrario:
        print(arbitrario)
    else:
        print(fijo)


oks(mensaje, punto, punto, punto)
