
# Curso Python - 
# 20210314. Luis Palacios
#

"""
Vamos a crear un programa que lea los resultados de los partidos de la liga española en el año 2019-2020, y nos devuelva información sobre estos datos. El fichero está subido junto con los ejercicios.

El programa ofrecerá un menú, para seleccionar la información deseada:

Estadística de un equipo: Nos pide por teclado el nombre de un equipo y nos muestra el número de goles que ha metido, los paridos ganados, perdidos y empatados.

Nombres de equipos: Nos muestra la lista de equipos que juegan.

Clasificación de la liga: Nos muestra los tres primeros equipos de la liga.

Quiniela por fecha: Introducimos una fecha y nos dice los resultados de la quiniela de ese día.

Salir
----

Para realizar este programa podemos realizar las siguientes funciones:

menu(): Muestra el menú y devuelve un entero con la opción escogida.

LeerPartidos(): Función que lee el fichero y devuelve una lista con los partidos (cada partido se va a guardar en un diccionario).

SumarGoles(equipo): Función que recibe un nombre de un equipo y devuelve el total de goles metidos.

InfoEquipos(equipo): Función que recibe un nombre de un equipo y devuelve una lista con los paridos ganados, perdidos y empatados.

Equipos(): Función que devuelve una lista con todos los equipos.

Quiniela(dia,mes,año): Función que recibe el día, el mes y el año. Y devuelve una lista con los partidos y resultados de la quiniela.

"""

# Para trabajar con fechas
from datetime import date
from datetime import datetime

# ======= VARIABLES

#filename="la-liga-2019.csv"
filenameResultados2019="la-liga-2019.csv"

# Variables globales
listaPartidos=[]

# ======= FUNCIONES

# Cargar CSV en un diccionario
def errorNoTengoDatos():
  """
    Informa que la BBDD de Partidos está vacía
  """
  print("Error: la base de datos está vacía, no tengo datos")
  return


# Cargar CSV en una lista de diccionarios
def leerCSVenListaDict(filename):
  """
    Leer un fichero CSV y lo mete en un diccionario. 

    En la primera línea tenemos las CLAVES. 
    En el resto de líneas los VALOREs.
  """

  # Si voy a asignarle algo a una variable global tengo que indicar que es global
  global listaPartidos

  listaPartidos=[]
  with open(filename,'r') as fd:
    first_line = fd.readline().strip() # Leo la primera línea con las claves, quitando el \n
    keys=first_line.split(",")
    nKeys=len(keys)
    for values_line in fd:  # Leo el resto de líneas
      values_line=values_line.strip() # quito el \n del final si lo tuviese
      values=values_line.split(",") 
      dict={}
      for i in range(nKeys):  # Guardo todos los valores en sus claves correspondientes
        dict[keys[i]] = values[i]
      listaPartidos.append(dict)

  if not ( len(listaPartidos) ):
    errorNoTengoDatos()
  return 

# Menú de opciones
def menu():
  """
    Muestra el menú y devuelve un entero con la opción escogida.
  """
  cmd=-1

  while cmd==-1:
    print("\n-------------------------------")
    print("(1) Estadística de un equipo")
    print("(2) Nombres de equipos")
    print("(3) Clasificación de la liga")
    print("(4) Quiniela por fecha")
    print("(0) Salir")

    try:
      cmd=int(input("Comando: "))
      if ( cmd not in range(0,5) ):
        print("ERROR: Opción inválida !!")
        cmd=-1
    except:
      print("ERROR: Espero un número entre 0-4 !!")
      continue

  return cmd

# 
def LeerPartidos():
  """
    **LeerPartidos()**: Función que lee el fichero y devuelve una lista 
    con los partidos (cada partido se va a guardar en un diccionario).

    Leo el CSV y además 

  """

  # Leo el CSV en el diccionario "dictPartidos"
  #
  leerCSVenListaDict(filenameResultados2019)

  return


def infoEquipo(equipo):
  """ 
    **InfoEquipos(equipo)**: Función que recibe un nombre de un equipo y 
    devuelve una lista con los paridos ganados, perdidos y empatados.

    Espero recibir una lista de tuplas "nombre_equipo, diccionario_valores", lo devuelto por Quiniela()
    [
       ( "equipo1", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       ( "equipo2", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       :
    ]

  """

  # Si no le he hecho ya, leo el fichero CSV y lo cargo en una 
  # lista con todos los resultados de los partidos. Asumo que las claves son: 
  # 'Round Number':, 'Date':, 'Location':, 'Home Team':, 'Away Team':, 'Result':
  if not (len(listaPartidos) ):
    LeerPartidos()

  # Pido la Quiniela a fecha de hoy
  now = datetime.now()
  quiniela = Quiniela(now.day, now.month, now.year)

  # Convierto lo que me devuelven a un diccionario
  dictEquipos = dict(quiniela)

  # Si existe el equipo que me pasan pues muestro sus datos
  if  equipo in dictEquipos:
    print("Equipo                PT PG PE PP")
    print("---------------------------------")
    print("{:<20}: {:>2} {:>2} {:>2} {:>2}".format(equipo, dictEquipos[equipo]["Puntos"], dictEquipos[equipo]["Ganados"], dictEquipos[equipo]["Empatados"], dictEquipos[equipo]["Perdidos"])) 
  else:
    print("Lo siento pero ese equipo no está en la Liga")

  return

def Equipos():
  """
    **Equipos()**: Función que devuelve una lista con todos los equipos.
  """

  # Si no le he hecho ya, leo el fichero CSV y lo cargo en una 
  # lista con todos los resultados de los partidos. Asumo que las claves son: 
  # 'Round Number':, 'Date':, 'Location':, 'Home Team':, 'Away Team':, 'Result':
  if not (len(listaPartidos) ):
    LeerPartidos()

  # Creo una lista con los nombres de todos los equipos
  if ( len(listaPartidos) > 0 ):

    listaEquipos=[]
    # Extraigo todos los nombres de los equipos.
    for partido in listaPartidos:
      listaEquipos.append(partido["Home Team"])
      listaEquipos.append(partido["Away Team"])

    # Hago que la lista solo tenga nombres únicos
    listaEquipos = list(set(listaEquipos))
    listaEquipos.sort()

  return listaEquipos

def showEquipos(listaEquipos):
  """
    **Equipos()**: Muestra la lista de equipos
  """
  print ("\nEquipos")
  print ("=======================")
  # Muestro la lista
  for equipo in listaEquipos:
    print(equipo)
  


#
# número de goles que ha metido, los paridos ganados, perdidos y empatados
#
# PT, PJ, PG, PE, PP, GF, GC
# PT: Puntos, 
# PJ: Partidos jugados, PG: Partidos Ganados
# PE: Partidos Empatados, PP: Partidos Perdidos, 
# GF: Goles a favor, GC: Goles en contra
def Quiniela(día, mes, año):
  """
    **Quiniela(dia,mes,año)**: Función que recibe el día, el mes y el año. 
    
    Devuelve una lista con los partidos y resultados de la quiniela
    hasta la fecha que nos han pasado. 

    Devuelve una lista del tipo: 
     
    return [
       ( "equipo1", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       ( "equipo2", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       :
     ]

  """
  dictLigaTotal={}

  # Si no le he hecho ya, leo el fichero CSV y lo cargo en una 
  # lista con todos los resultados de los partidos. Asumo que las claves son: 
  # 'Round Number':, 'Date':, 'Location':, 'Home Team':, 'Away Team':, 'Result':
  if not (len(listaPartidos) ):
    LeerPartidos()

  # Creo un diccionario para la Quiniela, con el NOMBRE DEL EQUIPO como clave
  if ( len(listaPartidos) > 0 ):

    # Creo el diccionario dictLigaTotal {}
    for partido in listaPartidos:

        # Fecha del partido
        partidoDía,partidoMes,partidoAño = partido["Date"].split()[0].split('/')
        partidoDate = datetime(int(partidoAño), int(partidoMes), int(partidoDía) )
        fechaCorte = datetime(int(año), int(mes), int(día) )

        if partidoDate <= fechaCorte: 
          if not partido["Home Team"] in dictLigaTotal:
              dictLigaTotal[partido["Home Team"]] = { 'Puntos':0, 'Goles casa':0, 'Goles fuera':0, 'Goles total':0, 'Ganados':0, 'Perdidos':0, 'Empatados':0 }
          if not partido["Away Team"] in dictLigaTotal:
              dictLigaTotal[partido["Away Team"]] = { 'Puntos':0, 'Goles casa':0, 'Goles fuera':0, 'Goles total':0, 'Ganados':0, 'Perdidos':0, 'Empatados':0 }

          golesCasa=int(partido["Result"].split('-')[0])
          golesVisitante=int(partido["Result"].split('-')[1])

          dictLigaTotal[partido["Home Team"]]["Goles casa"] = dictLigaTotal[partido["Home Team"]]["Goles casa"] + golesCasa
          dictLigaTotal[partido["Home Team"]]["Goles total"] = dictLigaTotal[partido["Home Team"]]["Goles total"] + golesCasa

          dictLigaTotal[partido["Away Team"]]["Goles fuera"] = dictLigaTotal[partido["Away Team"]]["Goles fuera"] + golesVisitante
          dictLigaTotal[partido["Away Team"]]["Goles total"] = dictLigaTotal[partido["Away Team"]]["Goles total"] + golesVisitante

          if ( golesCasa > golesVisitante ):
            dictLigaTotal[partido["Home Team"]]["Ganados"] = dictLigaTotal[partido["Home Team"]]["Ganados"] + 1
            dictLigaTotal[partido["Home Team"]]["Puntos"] = dictLigaTotal[partido["Home Team"]]["Puntos"] + 3
            dictLigaTotal[partido["Away Team"]]["Perdidos"] = dictLigaTotal[partido["Away Team"]]["Perdidos"] + 1

          elif ( golesCasa < golesVisitante ):
            dictLigaTotal[partido["Home Team"]]["Perdidos"] = dictLigaTotal[partido["Home Team"]]["Perdidos"] + 1
            dictLigaTotal[partido["Away Team"]]["Ganados"] = dictLigaTotal[partido["Away Team"]]["Ganados"] + 1
            dictLigaTotal[partido["Away Team"]]["Puntos"] = dictLigaTotal[partido["Away Team"]]["Puntos"] + 3

          else:
            dictLigaTotal[partido["Home Team"]]["Empatados"] = dictLigaTotal[partido["Home Team"]]["Empatados"] + 1
            dictLigaTotal[partido["Home Team"]]["Puntos"] = dictLigaTotal[partido["Home Team"]]["Puntos"] + 1
            dictLigaTotal[partido["Away Team"]]["Empatados"] = dictLigaTotal[partido["Away Team"]]["Empatados"] + 1
            dictLigaTotal[partido["Away Team"]]["Puntos"] = dictLigaTotal[partido["Away Team"]]["Puntos"] + 1

  # Ordeno el diccionario basándome en el campo Puntos. El resultado se 
  # Se devuelve una lista de tuples dictLigaTotalSorted=[("equipo",{valores}),...]
  return sorted(dictLigaTotal.items(), key = lambda x: x[1]['Puntos'], reverse=True) 


#
# Muestro en pantalla la situación actual de la quiniela
def printQuiniela(quiniela):
  """
    Muestro en pantalla la situación actual de la quiniela. 

    Espero recibir una lista de tuplas "nombre_equipo, diccionario_valores" como este ejemplo:     
    [
       ( "equipo1", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       ( "equipo2", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       :
    ]

  """
  print("Equipo                PT PG PE PP")
  print("---------------------------------")
  for equipo,valores in quiniela:
    print("{:<20}: {:>2} {:>2} {:>2} {:>2}".format(equipo, valores["Puntos"], valores["Ganados"], valores["Empatados"], valores["Perdidos"]))



# =================================
# ======= INICIO DEL PROGRAMA

# Bucle para mostrar el menú
#
while True:

  # Muestra el menú
  cmd=menu()
  
  # Selecciona comando

  ## Estadística de un equipo:
  if ( cmd == 1 ):
    """
      Nos pide por teclado el nombre de un equipo y nos muestra el número 
      de goles que ha metido, los partidos ganados, perdidos y empatados.
    """
    equipo=input("Nombre del equipo: ")
    infoEquipo(equipo)

  # Lista de equipos
  elif ( cmd == 2):
    """
      Nos muestra la lista de equipos que juegan.
    """
    showEquipos(Equipos())

  # Clasificación
  elif ( cmd == 3):
    """
      **Clasificación de la liga**: Nos muestra los tres primeros equipos de la liga.

      Lo he mejorado y muestro la tabla de la liga completa, no solo los tres primeros
    """
    # Qué fecha tenemos?
    now = datetime.now()
    printQuiniela(Quiniela(now.day, now.month, now.year))

  # Quiniela
  elif ( cmd == 4): 
    """
      **Quiniela por fecha:** Introducimos una fecha y nos dice los resultados de la quiniela de ese día.
    """
    día=int(input("Día: "))
    mes=int(input("Mes: "))
    año=int(input("Año: "))
    printQuiniela(Quiniela(día, mes, año))

  # Salir
  elif ( cmd == 0):
    print("Hasta luego lucas !!")
    break

  else:
    continue

