import os

# MENÚ
# PROCESOS
restart = "Si"

while restart == "Si":

    userOption = "Esperando"

    # ENTRADAS
    print("==========================================================")
    print("Menú de opciones")
    print("1.Cálculo area triángulo")
    print("2.Calificación notas")
    print("3.Definir número central")
    print("4.Funciones matemáticas MATH")
    print("5.Operaciones matemáticas")
    print("6.Operadores de asignación")
    print("7.Procesar respuestas")
    print("==========================================================")
    option = int(
        input("Porfavor digite el número según la opción que desea realizar: "))

    if option == 1:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/CalculoAreaTriangulo.py')
    elif option == 2:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/CalificacionNotas.py')
    elif option == 3:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/DefinicionNumeroCentral.py')
    elif option == 4:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/FuncionesMatematicasMath.py')
    elif option == 5:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/Operaciones.py')
    elif option == 6:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/OperadoresDeAsignacion.py')
    elif option == 7:
        os.system(
            'D:/TheSrSmith/Estudio/UPB/Programacion/Python/Ejercicios_Junio_05/ProcesarRespuestas.py')
    else:
        print("__________________________________________________________")
        print(option, " No es una opcion valida; Porfavor ingrese una opción valida")
        print("__________________________________________________________")

    if option > 0 and option < 8:
        userOption = "Esperando"
        while userOption != "No" and userOption != "Si":
            userOption = input("Desea volver al menu prinicpal (Si/No): ")
            if userOption == "No":
                restart = "No"
            elif userOption == "Si":
                restart = "Si"
            else:
                print("__________________________________________________________")
                print(
                    userOption, " No es una opcion valida; Porfavor ingrese una opción valida")
                print("__________________________________________________________")
