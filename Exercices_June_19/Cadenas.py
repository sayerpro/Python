# Métodos principales en las cadenas
# PROCESOS
restart = True
while restart:
    name = "saYer smIth plAza zaPAta"
    age = "23"
    nameWithoutSpaces = name.replace(" ", "")
    ageWithSpaces = "2 3"
    nameOnlyLowerCase = name.lower()
    nameAgeLower = nameOnlyLowerCase + age
    nameOnlyUpperCase = name.upper()
    nameAgeUpper = nameOnlyUpperCase + age
    whiteSpaces = "     "
    titleName = name.title()
    nickName = "TheSrSmith"
    nameWithSpacesLeft = "       " + name
    nameWithSpacesRight = name + "       "
    web = "www.google.com"
    webWithJoin = "www.google", ".com"
    lines = "Linea1, Linea2, Linea3"
    size = len(name)
    numero = 645987132.63521654

    # SALIDAS
    print("==============================================================================================================================================================")
    print("Nombre ---------------------------------------------------------------------------------------------------- : ", name)
    print("Tamaño del nombre en caracteres                                                                             : ", size)
    for count in range(size):
        word = name[count]
        print("Posicion del contador[", count,
              "] --------------------------------------------------------------------- : ", word)
    print("Nombre                                                                                                      : ", name)
    print(
        "Imprimir los cincos primeros caracteres del nombre ---------------------------------------------------------: ", name[:5])
    print(
        "Imprimir los caracteres del nombre desde la posicion 8 hasta la posicion final                              : ", name[8:])
    print(
        "Nombre desde la posicion 0 hasta la posicion -------------------------------------------------------------- : ", name[:6])
    print("Ultimos 5 caracteres del nombre: ", name[size - 5:])
    print("Su nombre con la primera letra en mayúscula --------------------------------------------------------------- : ", name.capitalize())
    print("Su nombre en minúsculas                                                                                     : ", name.lower())
    print("Su nombre en mayúsculas ----------------------------------------------------------------------------------- : ", name.upper())
    print("Su nombre con las mayúsculas en minúsculas y viceversa                                                      : ", name.swapcase())
    print("Su nombre convertido en título ---------------------------------------------------------------------------- : ", name.title())
    print("Su nombre centrado                                                                                          : ", name.center(50, "="))
    print("Su nombre alineao a la izquierda -------------------------------------------------------------------------- : ", name.ljust(50, "="))
    print("Su nombre alineao a la derecha                                                                              : ", name.rjust(50, "="))
    print("Edad ------------------------------------------------------------------------------------------------------ : ", age)
    print("Rellenar un texto de una determinada longitud (Ejemplo: 10) anteponiendo de ceros                           : ", age.zfill(10))
    print("Contar una cantidad de apariciones de una subcadena (Ejemplo: a) en una cadena ---------------------------- : ", name.count("a"))
    print("Buscar una subcadena (Ejemplo: za) dentro de una cadena                                                     : ", name.find("za"))
    print("Buscar una subcadena (Ejemplo: za) dentro de una cadena y determinar el rango de bsuqueda (Ejemplo: 0 a 10) : ", name.find("za", 0, 10))
    print("Saber si una cadena empieza con una subadena (Ejemplo: saYer) --------------------------------------------- : ", name.startswith("saYer"))
    print("Saber si una cadena empieza con una subadena (Ejemplo: sayer)                                               : ", name.startswith("sayer"))
    print("Saber si una cadena empieza con una subadena determinando el inicio de busqueda (Ejemplo: smIth posicion 6) : ",
          name.startswith("smIth", 6))
    print("Saber si una cadena termina con una subadena (Ejemplo: zaPAta)                                              : ", name.endswith("zaPAta"))
    print("Saber si una cadena termina con una subadena (Ejemplo: zapata) -------------------------------------------- : ", name.endswith("zapata"))
    print("Saber si una cadena termina con una subadena determinando el rango de busqueda (Ejemplo: plAza 12 a 17)     : ",
          name.endswith("plAza", 12, 17))
    print("Saber si una cadena es alfanumérica (Ejemplo: saYer smIth plAza zaPAta) ----------------------------------- : ", name.isalnum())
    print("Saber si una cadena es alfanumérica (Ejemplo: 23)                                                           : ", age.isalnum())
    print("Saber si una cadena es alfabética (Ejemplo: saYer smIth plAza zaPAta) ------------------------------------- : ", name.isalpha())
    print("Saber si una cadena es alfabética (Ejemplo: saYersmIthplAzazaPAta)                                          : ",
          nameWithoutSpaces.isalpha())
    print("Saber si una cadena es alfabética (Ejemplo: 23) ----------------------------------------------------------- : ", age.isalpha())
    print("Saber si una cadena es numérica (Ejemplo: 23)                                                               : ", age.isdigit())
    print("Saber si una cadena es numérica (Ejemplo: 2 3) ------------------------------------------------------------ : ", ageWithSpaces.isdigit())
    print("Saber si una cadena contiene solo minúsculas (Ejemplo: saYer smIth plAza zaPAta)                            : ", name.islower())
    print("Saber si una cadena contiene solo minúsculas (Ejemplo: sayer smith plaza zapata) -------------------------- : ",
          nameOnlyLowerCase.islower())
    print("Saber si una cadena contiene solo minúsculas (Ejemplo: sayer smith plaza zapata23)                          : ", nameAgeLower.islower())
    print("Saber si una cadena contiene solo minúsculas (Ejemplo: saYer smIth plAza zaPAta)                            : ", name.isupper())
    print("Saber si una cadena contiene solo minúsculas (Ejemplo: SAYER SMITH PLAZA ZAPATA) -------------------------- : ",
          nameOnlyUpperCase.isupper())
    print("Saber si una cadena contiene solo minúsculas (Ejemplo: SAYER SMITH PLAZA ZAPATA23)                          : ", nameAgeUpper.isupper())
    print("Saber si una cadena contiene solo espacios en blanco (Ejemplo:      ) ------------------------------------- : ", whiteSpaces.isspace())
    print("Saber si una cadena contiene solo espacios en blanco (Ejemplo: saYer smIth plAza zaPAta)                    : ", name.isspace())
    print("Saber si una cadena contiene formato de titúlo (Ejemplo: saYer smIth plAza zaPAta) ------------------------ : ", name.istitle())
    print("Saber si una cadena contiene formato de titúlo (Ejemplo: Sayer Smith Plaza Zapata)                          : ", titleName.istitle())
    print("Reemplazar texto de una cadena (Ejemplo: plAza zaPAta por TheSrSmith) ------------------------------------- : ",
          name.replace(name, nickName))
    print("Eliminar caracteres a la izquierda y derecha de una cadena (Ejemplo:        saYer smIth plAza zaPAta)       : ",
          nameWithSpacesLeft.strip())
    print("Eliminar caracteres a la izquierda y derecha de una cadena (Ejemplo: saYer smIth plAza zaPAta       ) ----- : ",
          nameWithSpacesRight.strip(""))
    print("Web                                                                                                         : ", web)
    print("Eliminar caracteres a la izquierda de una cadena (Ejemplo: www.google.com con w.) ------------------------- : ", web.lstrip("w."))
    print("Eliminar caracteres a la derecha de una cadena (Ejemplo: www.google.com con .com)                           : ", web.rstrip(".com"))
    print("Unir una caena e forma iterativa (Ejemplo: 23 con www.google.com) ----------------------------------------- : ", age.join(webWithJoin))
    print("Partir una cadena en tres partes utilizando un separador (Ejemplo: www.google.com con google)               : ", web.partition("google"))
    print("Partir una cadena en varias partes utilizando un separador (Ejemplo: www.google.com con .) ---------------- : ", web.split("."))
    print("Partir una cadena en lineas (Ejemplo: www.google.com con .)                                                 : ", lines.splitlines())
    print("Imprimir una determinada cantidad de la cadena despues de indicar un separador parte de la cadena %.2f      : " % numero)
    print("Imprimir una determinada cantidad de la cadena despues de indicar un separador parte de la cadena %20.2f    : " % numero)
    print("Duplicar cadena                                                                                             : ", web * 3)
    print("Tambien poidemos cojer posiciones como si la cadena fuese una lista                                         : ",
          web[3], web[10])
    print("{web:^10} {age}". format(web="Al", age="Revéz"))
    print("{web:<10} {age}". format(web="Al", age="Revéz"))
    print("{web:>10} {age}". format(web="Al", age="Revéz"))

    questionCondition = True
    while questionCondition:
        questionInput = input("Desea repetir el proceso Si/No: ")
        if questionInput == "Si":
            restart = True
        elif questionInput == "No":
            restart = False
        questionCondition = questionInput != "Si" and questionInput != "No"
        if questionCondition:
            print("Por favor digite una opción valida")
print("==============================================================================================================================================================")
