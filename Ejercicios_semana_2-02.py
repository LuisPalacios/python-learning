
# Curso Python -
# 20210315. Luis Palacios
#

"""
En este ejercicio vamos a crear un programa de creación y consulta de BBDD sobre ficheros. 
Temática concesionarios. 

La estructura de ficheros será la siguiente:

Fichero principal:
  - Nombre del concesionario.
  - Ciudad de ubicación.
  - Fichero de cada concesionario. Es un fichero .csv con la información de los coches para ese concesionario.

Fichero de cada concesionario:
  - Matrícula
  - Marca
  - Precio
  - Tipo de vehículo (sedan, deportivo, sub...)

Se debe poder realizar las siguientes tareas:

  - Funcion crear concesionario (pedirá introducir varios vehículos)
  - Función crear fichero principal (pedirá introducir un único indice de concesionarios)
  - consultar concesionario
  - consultar por marca
  - consultar por precio
  - consultar por tipo
  - consultar el de menor precio
  - Indicar el número de coches dispobible que se tiene de algún tipo de coche

"""

# Para trabajar con fechas
from datetime import datetime

# ======= VARIABLES
"""
  Fichero Principal: Lista de tuplas (concesionario, diccionario_datos)
  Nombre: tmp_principal.csv
    NombreConcesionario, Ciudad, Fichero
    :
  
  Fichero Concesionarios (filename=Nombre_Concesionario):
  Nombre: tmp_<matrícula>.csv
    Matricula, Marca, Precio, Tipo
    :
"""

sPre = "tmp_"
sFilenamePrincipal = sPre+"principal.csv"
dPrincipal = {}


# ======= FUNCIONES
#

# Lee todos los ficheros CSV en memoria en la variable diccionario dPrincipal
#
def leeDiccionarioPrincipal():
    """
      Leo todos los ficheros: principal y concesionarios y guardo todo en un Diccionario
      dPrincipal = {

        "NombreConcesionario": {
                'Ciudad':x, 
                'Fichero':x
                'Vehículos':
                  { 
                    "Matrícula1": {'Marca':x, 'Precio':x, 'Tipo':x},
                    "Matrícula2": {'Marca':x, 'Precio':x, 'Tipo':x},
                    :
                  }
              }
        :
        :
      }
    """
    # BBDD principal
    global dPrincipal

    # Primero el principal
    try:
        with open(sFilenamePrincipal, 'r') as fd:
            for lineaPrincipal in fd:
                lineaPrincipal = lineaPrincipal.strip()
                lConcesionario = lineaPrincipal.split(',')
                #print("lConcesionario: ", lConcesionario)
                sNombreConcesionario = lConcesionario[0]
                sCiudad = lConcesionario[1]
                sFilenameConcesionario = lConcesionario[2]
                # Por cada concesionario abro su fichero
                with open(sFilenameConcesionario, 'r') as fd:
                    for lineaConcesionario in fd:
                        lineaConcesionario = lineaConcesionario.strip()
                        lVehículo = lineaConcesionario.split(',')
                        #print("lVehículo: ", lVehículo)
                        sMatrícula = lVehículo[0]
                        sMarca = lVehículo[1]
                        sPrecio = int(lVehículo[2])
                        sTipo = lVehículo[3]
                        # Añado el concesionario si no existe
                        if not sNombreConcesionario in dPrincipal:
                            dPrincipal[sNombreConcesionario] = {
                                'Ciudad': sCiudad,
                                'Fichero': sFilenameConcesionario,
                                'Vehículos': {
                                }
                            }
                        # Añado el vehículo
                        dPrincipal[sNombreConcesionario]['Vehículos'][sMatrícula] = {
                            'Marca': sMarca,
                            'Precio': sPrecio,
                            'Tipo': sTipo
                        }
    except:
        print("Error al procesar el fichero de control.")


# DEVELOPER MODE: Muestra todos los concesionarios y equipos
def muestraTodo():
    """
      Esta función no se expone al usuario, es útil para el desarrollador
    """
    print("\n--")
    print("Fichero de control: "+sFilenamePrincipal)
    leeDiccionarioPrincipal()

    # Muestro la información
    for sNombreConcesionario in dPrincipal:
        sCiudad = dPrincipal[sNombreConcesionario]['Ciudad']
        for sMatrícula in dPrincipal[sNombreConcesionario]['Vehículos']:
            dVehículo = dPrincipal[sNombreConcesionario]['Vehículos'][sMatrícula]
            print(" -> " + sNombreConcesionario + " en " + sCiudad + ": " + sMatrícula + " 8- Marca: " +
                  dVehículo['Marca'] + " - Precio: " + str(dVehículo['Precio']) + " - Tipo: " + dVehículo['Tipo'])


# Creo el fichero del Concesionario y añado una entrada en el Principal apuntando a él.
#
def creaFicheroConcesionarioYAñadeAFicheroPrincipal(sNombre, sCiudad, dVehículos, bLimpiaDatos):

    # Construyo el nombre del concesionario
    sFilenameConcesionario = sPre+sNombre+".csv"

    # Crea el fichero del concesionario en formato CSV
    with open(sFilenameConcesionario, 'a') as fd:
        for key, value in dVehículos.items():
            linea = str(key+","+value["Marca"]+"," +
                        value["Precio"]+","+value["Tipo"]+"\n")
            fd.write(linea)

    # Crea o actualiza el fichero principal en formato CSV
    filename = sPre+sNombre
    if (limpiaDatos == True):
        cAction = 'w'
    else:
        cAction = 'a'
    linea = sNombre+","+sCiudad+","+filename+".csv\n"
    with open(sFilenamePrincipal, cAction) as fd:
        fd.write(linea)

    return

# Crear Concesionario:


def crearConcesionario():
    """
      Crea un concesionario, pidiendo la creación de varios vehículos y 
      luego crea su fichero CSV y añáde su referencia al CSV principal
    """

    # Pido el nombre del concesionario
    sNombre = input("Nombre del concesionario: ")
    sNombre.replace(" ", "")
    sCiudad = input("Ciudad del concesionario: ")
    if (sNombre == "" or sCiudad == ""):
        return

    # Pido vehículos
    dVehículos = {}
    while True:
        print("  >> Añadir vehículo a '"+sNombre+"'")
        sMatrícula = input("   --- Matrícula (Intro para terminar): ")
        if (sMatrícula == ""):
            break
        sMarca = input("   --- Marca: ")
        sPrecio = input("   --- Precio: ")
        sTipo = input("   --- Tipo: ")
        dVehículos[sMatrícula] = {'Marca': sMarca,
                                  'Precio': sPrecio, 'Tipo': sTipo}

    # Si tengo datos suficientes ...
    if (len(dVehículos)):
        # Una vez creado el fichero del concesionario y lo añado a principal
        creaFicheroConcesionarioYAñadeAFicheroPrincipal(
            sNombre, sCiudad, dVehículos)

    return


# Consulta los datos de un concesionario concreto.
def consultaConcesionario(sNombreConcesionario):
    # Añado el concesionario si no existe
    if not sNombreConcesionario in dPrincipal:
        print("Lo siento pero no tengo ese concesionario.")
        return

    # Muestro la información
    dConcesionario = dPrincipal[sNombreConcesionario]
    print()
    print("Concesionario : ", sNombreConcesionario)
    print("Ciudad        : ", dConcesionario['Ciudad'])
    for dMatrícula in dConcesionario['Vehículos']:
        dVehículo = dConcesionario['Vehículos'][dMatrícula]
        print(" -> " + dMatrícula + " - Marca: " + dVehículo['Marca'] + " - Precio: " + str(
            dVehículo['Precio']) + " - Tipo: " + dVehículo['Tipo'])


# Consulta los datos de un concesionario concreto.
def consultaMarca(sMarca):

    # Muestro la información
    for sNombreConcesionario in dPrincipal:
        sCiudad = dPrincipal[sNombreConcesionario]['Ciudad']
        for sMatrícula in dPrincipal[sNombreConcesionario]['Vehículos']:
            dVehículo = dPrincipal[sNombreConcesionario]['Vehículos'][sMatrícula]
            if (dVehículo['Marca'] == sMarca):
                print(" -> " + sNombreConcesionario + " en " + sCiudad + ": " + sMatrícula + " - " + " - Marca: " +
                      dVehículo['Marca'] + " - Precio: " + str(dVehículo['Precio']) + " - Tipo: " + dVehículo['Tipo'])

    return


# Muestra coches con precios menores al que nos pasan
def consultaPrecioMáximo(iPrecio):

    # Muestro la información
    for sNombreConcesionario in dPrincipal:
        sCiudad = dPrincipal[sNombreConcesionario]['Ciudad']
        for sMatrícula in dPrincipal[sNombreConcesionario]['Vehículos']:
            dVehículo = dPrincipal[sNombreConcesionario]['Vehículos'][sMatrícula]
            if (dVehículo['Precio'] <= iPrecio):
                print(" -> " + sNombreConcesionario + " en " + sCiudad + ": " + sMatrícula + " - " + " - Marca: " +
                      dVehículo['Marca'] + " - Precio: " + str(dVehículo['Precio']) + " - Tipo: " + dVehículo['Tipo'])

    return


# Consulta los datos de un tipo de coche concreto.
def consultaTipo(sTipo, bSoloMostrarNúmero):

    num = 0

    # Muestro la información
    for sNombreConcesionario in dPrincipal:
        sCiudad = dPrincipal[sNombreConcesionario]['Ciudad']
        for sMatrícula in dPrincipal[sNombreConcesionario]['Vehículos']:
            dVehículo = dPrincipal[sNombreConcesionario]['Vehículos'][sMatrícula]
            if (dVehículo['Tipo'] == sTipo):
                if (bSoloMostrarNúmero == True):
                    num = num+1
                else:
                    print(" -> " + sNombreConcesionario + " en " + sCiudad + ": " + sMatrícula + " - " + " - Marca: " +
                          dVehículo['Marca'] + " - Precio: " + str(dVehículo['Precio']) + " - Tipo: " + dVehículo['Tipo'])

    print("Número de coches de tipo '"+sTipo+" disponibles: "+str(num))

    return

# Consulta los datos de un tipo de coche concreto.


def consultaElMásBarato():

    menorValor = -1
    sFound = ""

    # Muestro la información
    for sNombreConcesionario in dPrincipal:
        sCiudad = dPrincipal[sNombreConcesionario]['Ciudad']
        for sMatrícula in dPrincipal[sNombreConcesionario]['Vehículos']:
            dVehículo = dPrincipal[sNombreConcesionario]['Vehículos'][sMatrícula]
            if (menorValor == -1 or dVehículo['Precio'] < menorValor):
                menorValor = dVehículo['Precio']
                sFound = str(" -> " + sNombreConcesionario + " en " + sCiudad + ": " + sMatrícula + " - " + " - Marca: " +
                             dVehículo['Marca'] + " - Precio: " + str(dVehículo['Precio']) + " - Tipo: " + dVehículo['Tipo'])

    print(sFound)

    return


# Menú de opciones
def menu():
    """
      Muestra el menú y devuelve un entero con la opción escogida.
    """
    cmd = -1

    while cmd == -1:
        print("\n-------------------------------")
        print("(1) Crear concesionario y vehículos")
        print("(2) Consultar concesionario")
        print("(3) Consultar por marca")
        print("(4) Consultar por precio")
        print("(5) Consultar por tipo")
        print("(6) Consultar el de menor precio")
        print("(7) Número disponible por tipo")
        #print("(8) Mostrar todos los concesionario y coches")
        print("(0) Salir")

        try:
            cmd = int(input("Comando: "))
            if (cmd not in range(0, 9)):
                print("ERROR: Opción inválida !!")
                cmd = -1
        except:
            print("ERROR: Espero un número entre 0-8 !!")
            continue

    return cmd


# =================================
# ======= INICIO DEL PROGRAMA

# Bucle para mostrar el menú
#
while True:

    # Muestra el menú
    cmd = menu()

    # Crear concesionario y vehículos:
    if (cmd == 1):
        crearConcesionario()
        leeDiccionarioPrincipal()
        continue

    # Consultar concesionario
    elif (cmd == 2):
        sNombreConcesionario = input("Nombre del concesionario: ")
        consultaConcesionario(sNombreConcesionario)
        continue

    # Consultar por marca
    elif (cmd == 3):
        sMarca = input("Nombre de la marca: ")
        consultaMarca(sMarca)
        continue

    # Consultar por precio
    elif (cmd == 4):
        iPrecio = int(input("Precio máximo: "))
        consultaPrecioMáximo(iPrecio)
        continue

    # Consultar por tipo
    elif (cmd == 5):
        sTipo = input("Tipo de coche: ")
        consultaTipo(sTipo, False)
        continue

    # Consultar el de menor precio de todos
    elif (cmd == 6):
        consultaElMásBarato()
        continue

    # Número disponible por tipo
    elif (cmd == 7):
        sTipo = input("Tipo de coche: ")
        consultaTipo(sTipo, True)
        continue

    # DEVELOPER MODE: Muestra todos los concesionarios y equipos
    # Esta opción no se muestra en el menú, pero viene bien durante la fase de desarrollo,
    elif (cmd == 8):
        muestraTodo()
        continue

    # Salir
    elif (cmd == 0):
        print("Hasta luego lucas !!")
        break

    else:
        continue
