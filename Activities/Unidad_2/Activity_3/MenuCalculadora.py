# CALCULO PROMEDIO
userOption = "99"
while userOption != "0":
    print("=================================================================")
    print("MENU DE OPCIONES")
    print("Digite el número según la operación que desea realizar")
    print("1. Saludar")
    print("2. Validar si el número es par")
    print("3. Promedio de 5 notas")
    print("4. Residuo")
    print("5. Procentaje")
    print("6. Potencia")
    print("0. Salir")

    # ENTRADAS
    validOption = False
    while not validOption:
        userOption = input()
        validOption = userOption.isdigit()
        if not validOption:
            print("Por favor digite un número")
        else:
            validOption = int(userOption) in range(*[0, 7])
            if not validOption:
                print("Por favor digite un número dentro del rango de opciones")

    # PROCESOS
    if userOption == "1":

        # SALIDAS
        print(" _   _       _                                     _         _")
        print("| | | | ___ | | __ _     _ __ ___  _   _ _ __   __| | ___   | |")
        print("| |_| |/ _ \| |/ _` |   | '_ ` _ \| | | | '_ \ / _` |/ _ \  | |")
        print("|  _  | (_) | | (_| |   | | | | | | |_| | | | | (_| | (_) | |_|))")
        print("|_| |_|\___/|_|\__,_|   |_| |_| |_|\__,_|_| |_|\__,_|\___/  (_)")

    elif userOption == "2":
        numberPar = float(input("Digite el número a validr: "))
        if numberPar % 2 == 0:
            print("El número ", numberPar, " es un número par")
        else:
            print("El número ", numberPar, " no es un número par")

    elif userOption == "3":
        sum = 0
        for item in range(5):
            note = float(input(f"Digite la nota #{item}: "))
            sum += note
        print("El promedio de las notas ingresaas es: ", sum / 5)

    elif userOption == "4":
        numberOne = int(
            input("Digite el número del cual desea sacar el residuo: "))
        numberTwo = int(input("Digite el residuo que desea sacar: "))
        print(f"El residuo {numberTwo} de {numberOne} es:",
              numberOne % numberTwo)

    elif userOption == "5":
        numberOne = int(
            input("Digite el número del que desea sacar el porcentaje: "))
        numberTwo = int(input("Digite el procentaje que desea sacar: "))
        print(f"El {numberTwo}% de {numberOne} es:",
              (numberTwo * numberOne) / 100)

    elif userOption == "6":
        number = int(input("Digite el número a potenciar al cuadrado: "))
        print(f"La potencia al cuadrado de {number} es: ", number**2)
    print("=================================================================")
