# CALCULADORA
import math


def imprimir(mensaje: str):
    print(mensaje)


def imprimirMensajes(mensaje: str, tipoImpresion: int):
    if tipoImpresion == numero0:
        imprimir(mensaje)
    elif tipoImpresion == numero1:
        for item in range(len(list(mensaje))):
            imprimir(f"{item}{punto} {mensaje[item]}")
    # ENTRADAS
    elif tipoImpresion == 2:
        return input(mensaje)


def validarEntradaNumerica(mensaje: str, mensajeError: str, rango: bool):
    condicionWhile = falso
    while not condicionWhile:
        desicionUsuario = imprimirMensajes(mensaje, numero2)
        condicionWhile = desicionUsuario.isdigit()
    if not condicionWhile or not validarRangoNumerico(int(desicionUsuario), numero0, numero9) and rango:
        imprimirMensajes(mensajeError, numero0)
    return int(desicionUsuario)


def validarRangoNumerico(numero: int, desde: int, hasta: int):
    if numero in range(*[desde, hasta]):
        return verdadero
    else:
        return falso


def dirigirLogica(decisionUsuario: int):
    if validarRangoNumerico(decisionUsuario, numero0, numero2):
        numero1Operacion = validarEntradaNumerica(
            primerNumero, errorNumero, falso)
        numero2Operacion = validarEntradaNumerica(
            segundoNumero, errorNumero, falso)
        if decisionUsuario == numero0:
            imprimirMensajes(
                f"{opcionesMenu[0].join(resultadoFemenino)}{numero1Operacion + numero2Operacion}", numero0)
        if decisionUsuario == numero1:
            imprimirMensajes(
                f"{opcionesMenu[1].join(resultadoFemenino)}{numero1Operacion - numero2Operacion}", numero0)
        if decisionUsuario == numero2:
            imprimirMensajes(
                f"{opcionesMenu[2].join(resultadoFemenino)}{numero1Operacion * numero2Operacion}", numero0)
    else:
        numero = validarEntradaNumerica(numeroSolo, errorNumero, falso)
        if decisionUsuario == numero3:
            imprimirMensajes(
                f"{opcionesMenu[3].join(resultadoMasculino)}{math.log(numero)}", numero0)
        if decisionUsuario == numero4:
            imprimirMensajes(
                f"{opcionesMenu[4].join(resultadoMasculino)}{math.cos(numero)}", numero0)
        if decisionUsuario == numero5:
            imprimirMensajes(
                f"{opcionesMenu[5].join(resultadoMasculino)}{math.sin(numero)}", numero0)
        if decisionUsuario == numero6:
            imprimirMensajes(
                f"{opcionesMenu[6].join(resultadoMasculino)}{math.isqrt(numero)}", numero0)
        if decisionUsuario == numero7:
            imprimirMensajes(
                f"{opcionesMenu[7].join(resultadoMasculino)}{bin(numero)[2:]}", numero0)
        if decisionUsuario == numero8:
            imprimirMensajes(
                f"{opcionesMenu[8].join(resultadoMasculino)}{int(str(numero), 2)}", numero0)


decorador = "==================================================="
bienvenida = "Bienvenido al sistema de OPERACIONES MATEMATICAS"
opcionesMenu = ["Suma", "Resta", "Multiplicación", "Logaritmo", "Coseno", "Seno",
                "Raíz cuadrada", "Convertir decimal a binario", "Convertir binario a decimal"]
elegirOperacion = "Porfavor digite el número de opción según la operación que desea realizar: "
errorOpciones = "Por favor digite un número entero dentro de las opciones establecidas"
errorNumero = "Por favor digite un número entero"
primerNumero = "Digite el primer número: "
segundoNumero = "Digite el segundo número: "
numeroSolo = "Digite un número: "
resultadoFemenino = "El resultado de la ", " es: "
resultadoMasculino = "El resultado del ", " es: "
punto = "."
numero0 = 0
numero1 = 1
numero2 = 2
numero3 = 3
numero4 = 4
numero5 = 5
numero6 = 6
numero7 = 7
numero8 = 8
numero9 = 9
verdadero = True
falso = False

# PROCESOS


def logicaPrograma():
    imprimirMensajes(decorador, numero0)
    imprimirMensajes(bienvenida, numero0)
    imprimirMensajes(opcionesMenu, numero1)
    decisionUsuario = validarEntradaNumerica(
        elegirOperacion, errorOpciones, verdadero)
    dirigirLogica(decisionUsuario)


logicaPrograma()
