import winsound


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
seguridad2 = "¿ESTA SEGURO?"
desicion = "Si/No: "
opcionCategoria = "Digite el Si/No según la opción."
opcionNumero = "Digite el número según la opción: "
opcionCategoriaNumero = "Por favor digite un número entero entre 1 y 5"
miedoso = "Hasta nunca miedosin"
indeciso = "Cuando tengas mas confianza vuelve INDECISO"
indicacionCategorias = ["====================================", "Seleccione una categoria", "1. Países             ", "2. Frutas             ",
                        "3. Géneros musicales  ", "4. Animales           ", "5. Categoria películas", "===================================="]
# Frecuency Min 37 Max 32767, Duration Min 0 Max "Undefined"
sonidoTitulo = [80, 100]
sonidoFinTitulo = [4000, 1000]


def imprimirMensaje(mensaje: str, entrada: bool, centrar: bool):
    if entrada:
        return input(mensaje)
    elif centrar:
        print("{web:^70}". format(web=mensaje))
    else:
        print(mensaje)


def validarDesicion():
    cadena = ""
    valido = False
    result = False
    while not valido:
        cadena = imprimirMensaje(desicion, True, False)
        if cadena == "Si":
            valido = True
            result = True
        elif cadena == "No":
            valido = True
            result = False
        else:
            imprimirMensaje(opcionCategoria, False, False)
    return result


def finalizarEjecucion(mensaje: str, entrada: bool):
    imprimirMensaje(mensaje, entrada, False)
    exit()


def emitirSonido(frecuencia: int, duracion: int):
    winsound.Beep(frecuencia, duracion)


def validarEntradaNumerica():
    numerico = False
    while not numerico:
        numerico = imprimirMensaje(
            opcionNumero, True, False).isdigit()
        if not numerico:
            imprimirMensaje(opcionCategoriaNumero, False, False)


def logicaPrograma():
    imprimirMensaje(bienvenida, False, False)
    imprimirMensaje(seguridad, False, False)
    if validarDesicion():
        imprimirMensaje(seguridad2, False, False)
        if validarDesicion():
            for item in range(len(tituloAO)):
                imprimirMensaje(tituloAO[item], False, False)
                emitirSonido(sonidoTitulo[0], sonidoTitulo[1])
            emitirSonido(sonidoFinTitulo[0], sonidoFinTitulo[1])
        else:
            finalizarEjecucion(indeciso, False)
    else:
        finalizarEjecucion(miedoso, False)
    for item in range(len(indicacionCategorias)):
        imprimirMensaje(indicacionCategorias[item], False, True)
    validarEntradaNumerica()


logicaPrograma()
