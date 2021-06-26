import winsound
import random


paises = ["Colombia", "Bolivia", "Alemania", "Rusia", "Japon"]
frutas = ["Banano", "Pera", "Durazno", "Naranja", "Uva"]
generosMusicales = ["Pop", "Rock", "Alternativo", "Metal", "Chillwave"]
animales = ["Gato", "Elefante", "Ballena", "Aguila", "Perro"]
categoriasPeliculas = ["Amor", "Accion", "Drama", "Comedia", "Terror"]

matrix = [paises, frutas, generosMusicales, animales, categoriasPeliculas]

tituloAO = ["        ",
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

bienvenida = "Bienvenido al sistema"
seguridad = "¿Desea jugar al juego AHORCADO?"
seguridad2 = "¿ESTA SEGURO Y NO LE A MIEDO?"
desicion = "Si/No: "
opcionCategoria = "Mij@ le estan diciendo que ingrese Si o No (Si/No)."
opcionNumero = "Digite el número según la opción: "
opcionCategoriaNumero = "¿No entiende que es un número entero del 1 al 5?"
miedoso = "Hasta nunca miedosin"
indeciso = "Cuando tengas mas confianza vuelve INDECISO"
indicacionCategorias = ["====================================", "Seleccione una categoria", "1. Países             ", "2. Frutas             ",
                        "3. Géneros musicales  ", "4. Animales           ", "5. Categoria películas", "===================================="]
# Frecuency Min 37 Max 32767, Duration Min 0 Max "Undefined"
sonidoTitulo = [80, 100]
sonidoFinTitulo = [4000, 1000]
sonidoBienvenida = [1000, 100]
sonidoFinBienvenia = [4000, 1000]
sonidoHorcaE = [40, 10]
sonidoFinHorcaE = [500, 1000]
guionBajo = []
comiezo = "LA HORCA COMIENZA, LA PALABRA A ADIVINAR TIENE ", " LETRAS, INTENTA NO MORIR ..."
letraMensaje = "Digita la una letra: "
opcionLetra = "Mij@, ¿que no entiende que es una letra? A B C ..."

alaHorca = ["        (               )                     )   (      (          )   ",
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
            "| |                  ",
            "| |                  ",
            "| |                   ",
            "| |                    ",
            "| |               ",
            "| |               ",
            "| |               ",
            "| |               ",
            "| |                ",
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
            "| |           . .    ",
            "| |          |   |   ",
            "| |          | . |    ",
            "| |          |   |     ",
            "| |            '  ",
            "| |               ",
            "| |               ",
            "| |               ",
            "| |                ",
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
            "| |        /Y . .    ",
            "| |       // |   |   ",
            "| |      //  | . |    ",
            "| |     ')   |   |     ",
            "| |            '  ",
            "| |               ",
            "| |               ",
            "| |               ",
            "| |                ",
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
            "| |            '  ",
            "| |               ",
            "| |               ",
            "| |               ",
            "| |                ",
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
            "| |          ||'  ",
            "| |          ||   ",
            "| |          ||   ",
            "| |          ||   ",
            "| |         / |     ",
            "_______", "|_`-'     |", " | ",
            "|" "| ____\ \       '"  "|",
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
            "| |          ||'||",
            "| |          || ||",
            "| |          || ||",
            "| |          || ||",
            "| |         / | | \"",
            "_______", "|_`-'  `-'  |", " | ",
            "|" "| ____\ \       '"  "|",
            "| |        \ \        | |",
            ": :         \ \       : :",
            ". .          `'       . ."]]


def validarLetra(letra: str, palabra: str):
    return palabra.lower.find(letra.lower)


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
    guionBajo = ["_" * int(result)]
    imprimirMensaje(guionBajo, 0)
    return palabra


def dirigirACategoria(opcion: int):
    palabra = ""
    if opcion == 1:
        palabra = seleccionarOpcionRandom(paises)
    elif opcion == 2:
        palabra = seleccionarOpcionRandom(frutas)
    elif opcion == 3:
        palabra = seleccionarOpcionRandom(generosMusicales)
    elif opcion == 4:
        palabra = seleccionarOpcionRandom(animales)
    elif opcion == 5:
        palabra = seleccionarOpcionRandom(categoriasPeliculas)
    return palabra


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
    else:
        print("{web:^70}". format(web=mensaje))


def logicaPrograma():
    imprimirMensaje(bienvenida, 0)
    imprimirMensaje(seguridad, 0)
    if validarDesicion():
        imprimirMensaje(seguridad2, 0)
        if validarDesicion():
            imprimirMensajeLista(tituloAO, sonidoTitulo, sonidoFinTitulo)
        else:
            finalizarEjecucion(indeciso, 0)
    else:
        finalizarEjecucion(miedoso, 0)
    for item in range(len(indicacionCategorias)):
        imprimirMensaje(indicacionCategorias[item], 2)
    palabra = dirigirACategoria(validarEntradaNumerica())
    intentos = 0
    while intentos <= 6:
        letra = valiarEntradaAlfabetica()
        posicionLetra = validarLetra(letra, palabra)
        if posicionLetra > -1:
            guionBajo[posicionLetra] = letra
            imprimirMensaje(guionBajo, 2)
        else:
            intentos += 1


logicaPrograma()
