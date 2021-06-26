# AHORCAO
import winsound
import random

# PROCESOS
paises = ["colombia", "bolivia", "alemania", "rusia", "japon"]
frutas = ["banano", "pera", "durazno", "naranja", "uva"]
generosMusicales = ["pop", "rock", "alternativo", "metal", "chillwave"]
animales = ["gato", "elefante", "ballena", "aguila", "perro"]
categoriasPeliculas = ["amor", "accion", "drama", "comedia", "terror"]

matrix = [paises, frutas, generosMusicales, animales, categoriasPeliculas]
bienvenida = "Bienvenido al sistema"
seguridad = "¿Desea jugar al juego AHORCADO?"
seguridad2 = "¿ESTA SEGURO Y NO LE A MIEDO?"
desicion = "Si/No: "
opcionCategoria = "Mij@ le estan diciendo que ingrese Si o No (Si/No)."
opcionNumero = "Digite el número según la opción: "
opcionCategoriaNumero = "¿No entiende que es un número entero del 1 al 5?"
miedoso = "Hasta nunca miedosin"
indeciso = "Cuando tengas mas confianza vuelve INDECISO"
indicacionCategorias = [
    "====================================", "Seleccione una categoria", "1. Países             ", "2. Frutas             ",
    "3. Géneros musicales  ", "4. Animales           ", "5. Categoria películas", "===================================="]
# Frecuency Min 37 Max 32767, Duration Min 0 Max "Undefined"
sonidoTitulo = [80, 100]
sonidoFinTitulo = [4000, 1000]
sonidoBienvenida = [1000, 100]
sonidoFinBienvenia = [4000, 1000]
sonidoHorcaE = [40, 10]
sonidoFinHorcaE = [500, 1000]
sinSonido = [37, 0]
comiezo = "LA HORCA COMIENZA, LA PALABRA A ADIVINAR TIENE ", " LETRAS, INTENTA NO MORIR ..."
letraMensaje = "Digite una letra: "
opcionLetra = "Mij@, ¿que no entiende que es una letra? A B C ..."
repetir = "¿Desea seguir jugando?"
bienJugado = "Bien jugado palabra adivinada ", ""
malJugado = "PESIMO ¿lo dejaste morir? la palabra a adivinar era ", " FACILITO"

tituloAO = [
    "        ",
    " ▄▄▄       ██░ ██  ▒█████   ██▀███  ▄████▄   ▄▄▄      ▓█████▄  ▒█████  ",
    "▒████▄    ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒██▀ ▀█  ▒████▄    ▒██▀ ██▌▒██▒  ██▒",
    "▒██  ▀█▄  ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒▓█    ▄ ▒██  ▀█▄  ░██   █▌▒██░  ██▒",
    "░██▄▄▄▄██ ░▓█ ░██ ▒██   ██░▒██▀▀█▄ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░",
    " ▓█   ▓██▒░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒ ▓███▀ ░ ▓█   ▓██▒░▒████▓ ░ ████▓▒░",
    " ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ",
    "  ▒   ▒▒ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░  ▒     ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ",
    "  ░   ▒    ░  ░░ ░░ ░ ░ ▒    ░░   ░░          ░   ▒    ░ ░  ░ ░ ░ ░ ▒  ",
    "      ░  ░ ░  ░  ░    ░ ░     ░    ░ ░            ░  ░   ░        ░ ░  ",
    "                                   ░                   ░               "]

alaHorca = [
    "        (               )                     )   (      (          )   ",
    "   (    )\ )         ( /(                  ( /(   )\ )   )\ )    ( /(   )",
    " ( )\  (()/(   (     )\())  (   (    (     )\()) (()/(  (()/(    )\())  ",
    " )((_)  /(_))  )\   ((_)\   )\  )\   )\   ((_)\   /(_))  /(_))  ((_)\   ",
    "((_)_  (_))   ((_)   _((_) ((_)((_) ((_)   _((_) (_))   (_))_     ((_)  )",
    " | _ ) |_ _|  | __| | \| | \ \ / /  | __| | \| | |_ _|   |   \   / _ \  ",
    " | _ \  | |   | _|  | .` |  \ V /   | _|  | .` |  | |    | |) | | (_) | ))",
    " |___/ |___|  |___| |_|\_|   \_/    |___| |_|\_| |___|   |___/   \___/  ",
    "                                                                        ",
    "             (                     )      )    (                        ",
    "   (         )\ )     (         ( /(   ( /(    )\ )     (       (       ",
    "   )\       (()/(     )\        )\())  )\())  (()/(     )\      )\      ",
    "((((_)(      /(_)) ((((_)(     ((_)\  ((_)\    /(_))  (((_)  ((((_)(    ))",
    " )\ _ )\    (_))    )\ _ )\     _((_)   ((_)  (_))    )\___   )\ _ )\   )",
    " (_)_\(_)   | |     (_)_\(_)   | || |  / _ \  | _ \  ((/ __|  (_)_\(_)  ))",
    "  / _ \     | |__    / _ \     | __ | | (_) | |   /   | (__    / _ \    )",
    " /_/ \_\    |____|  /_/ \_\    |_||_|  \___/  |_|_\    \___|  /_/ \_\   ",
    "                                                                        "]

intento = [["___________.._______",
            "| ._________)______|",
            "| | / /",
            "| |/ /",
            "| | /",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |__________________________",
            "| |__________________________|",
            "| |                    |     |",
            ": :                    :     :",
            ". .                    .     ."],
           [" ___________.._______",
            "| .__________))______|",
            "| | / /      ||",
            "| |/ /       ||",
            "| | /        ||.-''.",
            "| |/         |/  _  \"",
            "| |          ||  `/,|",
            "| |          (\\`_.'",
            "| |         .-`--'.",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |__________________________",
            "| |__________________________|",
            "| |        \ \        | |",
            ": :         \ \       : :",
            ". .          `'       . ."],
           [" ___________.._______",
            "| .__________))______|",
            "| | / /      ||",
            "| |/ /       ||",
            "| | /        ||.-''.",
            "| |/         |/  _  \"",
            "| |          ||  `/,|",
            "| |          (\\`_.'",
            "| |         .-`--'.",
            "| |           . .",
            "| |          |   |",
            "| |          | . |",
            "| |          |   |",
            "| |            '",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |__________________________",
            "| |__________________________|",
            "| |        \ \        | |",
            ": :         \ \       : :",
            ". .          `'       . ."],
           [" ___________.._______",
            "| .__________))______|",
            "| | / /      ||",
            "| |/ /       ||",
            "| | /        ||.-''.",
            "| |/         |/  _  \"",
            "| |          ||  `/,|",
            "| |          (\\`_.'",
            "| |         .-`--'.",
            "| |        /Y . .",
            "| |       // |   |",
            "| |      //  | . |",
            "| |     ')   |   |",
            "| |            '",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |__________________________",
            "| |__________________________|",
            "| |        \ \        | |",
            ": :         \ \       : :",
            ". .          `'       . ."],
           [" ___________.._______",
            "| .__________))______|",
            "| | / /      ||",
            "| |/ /       ||",
            "| | /        ||.-''.",
            "| |/         |/  _  \"",
            "| |          ||  `/,|",
            "| |          (\\`_.'",
            "| |         .-`--'.",
            "| |        /Y . . Y\"",
            "| |       // |   | \\",
            "| |      //  | . |  \\",
            "| |     ')   |   |   (`",
            "| |            '",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |__________________________",
            "| |__________________________|",
            "| |        \ \        | |",
            ": :         \ \       : :",
            ". .          `'       . ."],
           [" ___________.._______",
            "| .__________))______|",
            "| | / /      ||",
            "| |/ /       ||",
            "| | /        ||.-''.",
            "| |/         |/  _  \"",
            "| |          ||  `/,|",
            "| |          (\\`_.'",
            "| |         .-`--'.",
            "| |        /Y . . Y\"",
            "| |       // |   | \\",
            "| |      //  | . |  \\",
            "| |     ')   |   |   (`",
            "| |          ||'",
            "| |          ||",
            "| |          ||",
            "| |          ||",
            "| |         / |",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |"],
           [" ___________.._______",
            "| .__________))______|",
            "| | / /      ||",
            "| |/ /       ||",
            "| | /        ||.-''.",
            "| |/         |/  _  \"",
            "| |          ||  `/,|",
            "| |          (\\`_.'",
            "| |         .-`--'.",
            "| |        /Y . . Y\"",
            "| |       // |   | \\",
            "| |      //  | . |  \\",
            "| |     ')   |   |   (`",
            "| |          ||'||",
            "| |          || ||",
            "| |          || ||",
            "| |          || ||",
            "| |         / | | \"",
            "| |",
            "| |",
            "| |",
            "| |",
            "| |"]]

felicitacion = [
    "███████╗███████╗██╗     ██╗ ██████╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗",
    "██╔════╝██╔════╝██║     ██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██║",
    "█████╗  █████╗  ██║     ██║██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗██║",
    "██╔══╝  ██╔══╝  ██║     ██║██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║╚═╝",
    "██║     ███████╗███████╗██║╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║██╗",
    "╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝",
    " ",
    "████████╗███████╗    ███████╗ █████╗ ██╗     ██╗   ██╗ █████╗ ███████╗████████╗███████╗",
    "╚══██╔══╝██╔════╝    ██╔════╝██╔══██╗██║     ██║   ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝",
    "   ██║   █████╗      ███████╗███████║██║     ██║   ██║███████║███████╗   ██║   █████╗",
    "   ██║   ██╔══╝      ╚════██║██╔══██║██║     ╚██╗ ██╔╝██╔══██║╚════██║   ██║   ██╔══╝",
    "   ██║   ███████╗    ███████║██║  ██║███████╗ ╚████╔╝ ██║  ██║███████║   ██║   ███████╗    ██╗██╗██╗",
    "   ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝╚═╝╚═╝",
    "                                                                                                    "]

perdioms = [
    " ██████  ██    ██ ███████     ███    ███  █████  ██",
    "██    ██ ██    ██ ██          ████  ████ ██   ██ ██",
    "██    ██ ██    ██ █████       ██ ████ ██ ███████ ██",
    "██ ▄▄ ██ ██    ██ ██          ██  ██  ██ ██   ██ ██",
    " ██████   ██████  ███████     ██      ██ ██   ██ ███████",
    "    ▀▀",
    " ",
    " █████                ██   ██  ██████  ██████                 ██████  █████                ██████   ██████",
    "██   ██               ██   ██ ██    ██ ██   ██               ██      ██   ██               ██   ██ ██    ██",
    "███████     █████     ███████ ██    ██ ██████      █████     ██      ███████     █████     ██   ██ ██    ██",
    "██   ██               ██   ██ ██    ██ ██   ██               ██      ██   ██               ██   ██ ██    ██",
    "██   ██               ██   ██  ██████  ██   ██                ██████ ██   ██               ██████   ██████",
    "                                                                                                            ",
    " ",
    "██████  ██    ██  █████       ██  █████       ██  █████",
    "██   ██ ██    ██ ██   ██      ██ ██   ██      ██ ██   ██",
    "██████  ██    ██ ███████      ██ ███████      ██ ███████",
    "██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██   ██ ██   ██",
    "██████   ██████  ██   ██  █████  ██   ██  █████  ██   ██",
    " "]

despedia = [
    " ",
    ".   .    .     .-. .---.    .         .   ..   ..   . .--.    .    ",
    "|   |   / \   (   )  |     / \        |\  ||   ||\  |:       / \   ",
    "|---|  /___\   `-.   |    /___\       | \ ||   || \ ||      /___\  ",
    "|   | /     \ (   )  |   /     \      |  \|:   ;|  \|:     /     \ ",
    "'   ''       ` `-'   '  '       `     '   ' `-' '   ' `--''       `"]


def logicaJuego():
    result = dirigirACategoria(validarEntradaNumerica())
    palabra = result[0]
    guionBajo = result[1]
    palabraImpresion = palabra
    intentos = 0
    salida = 0
    while intentos < 6:
        letra = valiarEntradaAlfabetica()
        apariciones = palabra.count(letra)
        contador = 0
        while contador < apariciones or contador == 0:
            posicionLetra = validarLetra(letra, palabra)
            if posicionLetra > -1:
                palabra = palabra.replace(palabra[posicionLetra], "&", 1)
                guionBajo[posicionLetra] = letra
                salida += 1
                if salida == len(palabra):
                    return [True, palabraImpresion]
            else:
                intentos += 1
                imprimirMensajeLista(intento[intentos], sinSonido, sinSonido)
                imprimirMensaje(guionBajo, 3)
            contador += 1
        imprimirMensaje(guionBajo, 3)
    return [False, palabraImpresion]


def validarLetra(letra: str, palabra: str):
    letra = letra.lower()
    palabra = palabra.lower()
    return palabra.find(letra)


def valiarEntradaAlfabetica():
    cadena = False
    while not cadena:
        letra = imprimirMensaje(letraMensaje, 1)
        cadena = letra.isalpha()
        if not cadena:
            imprimirMensaje(opcionLetra, 0)
        else:
            return letra


def imprimirMensajeLista(mensaje: list, sonidoImpresion: list, sonidoFinal: list):
    for item in range(len(mensaje)):
        imprimirMensaje(mensaje[item], 0)
        emitirSonido(sonidoImpresion[0], sonidoImpresion[1])
    emitirSonido(sonidoFinal[0], sonidoFinal[1])


def seleccionarOpcionRandom(categoria: list):
    palabra = random.choice(categoria)
    result = str(len(palabra))
    imprimirMensajeLista(alaHorca, sonidoBienvenida, sonidoFinBienvenia)
    imprimirMensaje(result.join(comiezo), 0)
    imprimirMensajeLista(intento[0], sonidoHorcaE, sonidoFinHorcaE)
    cantidadLetras = int(result)
    guionBajo = []
    for item in range(cantidadLetras):
        guionBajo.append("_")
    imprimirMensaje(guionBajo, 3)
    return [palabra, guionBajo]


def dirigirACategoria(opcion: int):
    result = []
    if opcion == 1:
        result = seleccionarOpcionRandom(paises)
    elif opcion == 2:
        result = seleccionarOpcionRandom(frutas)
    elif opcion == 3:
        result = seleccionarOpcionRandom(generosMusicales)
    elif opcion == 4:
        result = seleccionarOpcionRandom(animales)
    elif opcion == 5:
        result = seleccionarOpcionRandom(categoriasPeliculas)
    return result


def finalizarEjecucion(mensaje: str, entrada: int):
    imprimirMensaje(mensaje, entrada)
    exit()


def emitirSonido(frecuencia: int, duracion: int):
    winsound.Beep(frecuencia, duracion)


def validarEntradaNumerica():
    numerico = False
    while not numerico:
        opcion = imprimirMensaje(opcionNumero, 1)
        numerico = opcion.isdigit()
        if not numerico or not int(opcion) in range(*[1, 6]):
            numerico = False
            imprimirMensaje(opcionCategoriaNumero, 0)
        else:
            return int(opcion)


def validarDesicion():
    cadena = ""
    valido = False
    result = False
    while not valido:
        cadena = imprimirMensaje(desicion, 1)
        if cadena == "Si":
            valido = True
            result = True
        elif cadena == "No":
            valido = True
            result = False
        else:
            imprimirMensaje(opcionCategoria, 0)
    return result


def imprimirMensaje(mensaje: str, tipoImpresion: int):
    if tipoImpresion == 0:
        print(mensaje)
    elif tipoImpresion == 1:
        return input(mensaje)
    elif tipoImpresion == 2:
        print("{web:^70}". format(web=mensaje))
    else:
        auxiliar = []
        for item in range(len(list(mensaje))):
            auxiliar.append(str(mensaje[item]))
        print(' '.join(auxiliar))


def logicaPrograma():
    # SALIDAS
    imprimirMensaje(bienvenida, 0)
    imprimirMensaje(seguridad, 0)
    # ENTRADAS
    if validarDesicion():
        imprimirMensaje(seguridad2, 0)
        if validarDesicion():
            imprimirMensajeLista(tituloAO, sonidoTitulo, sonidoFinTitulo)
        else:
            finalizarEjecucion(indeciso, 0)
    else:
        finalizarEjecucion(miedoso, 0)
    dicisionRepetir = True
    while dicisionRepetir:
        for item in range(len(indicacionCategorias)):
            imprimirMensaje(indicacionCategorias[item], 2)
        resultado = logicaJuego()
        if resultado[0]:
            imprimirMensajeLista(
                felicitacion, sonidoBienvenida, sonidoFinBienvenia)
            mensaje = resultado[1].join(bienJugado)
            imprimirMensaje(mensaje, 0)
        else:
            imprimirMensajeLista(
                perdioms, sonidoBienvenida, sonidoFinBienvenia)
            mensaje = resultado[1].join(malJugado)
            imprimirMensaje(mensaje, 0)
        imprimirMensaje(repetir, 0)
        dicisionRepetir = validarDesicion()
    imprimirMensajeLista(despedia, sinSonido, sinSonido)


logicaPrograma()
