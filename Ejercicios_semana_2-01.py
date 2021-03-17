
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

# Fichero fuente de datos
filenameResultados2019="la-liga-2019.csv" 

# Lista "global" donde guardaré los resultados de cada partido que encuentre en el fichero fuente de datos CSV
# Cada entrada contienen un diccionario con dichros resultados, con el siguiente formato. 
#
#   listaPartidos = [
#     { 'Round Number':<valor>, 'Date':<valor>, 'Location':<valor>, 'Home Team':<valor>, 'Away Team':<valor>, 'Result':<valor> }
#     :
#     :
#   ]
listaPartidos=[]                          


# ======= FUNCIONES

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

# Leer los resultados de los partidos, 
def LeerPartidos():
  """
    Esta función lee la fuente de datos desde fichero CSV y lo mete en la lista "listaPartidos=[]"
    
    Espero que me pasen las siguientes variables: 

      filename: Un string con el nombre del fichero csv

    En la primera línea tenemos las CLAVES. 
    En el resto de líneas los VALOREs.
  """

  # Identifico la variable "listaPartidos" como Global porque VOY A MODIFICARLA !!
  # Solo hace falta identificarla como global cuando se modifica, si solo se va a leer no es necesario. 
  # Si no lo haces y la modificas entonces entonces te crea una variable local de esta función. 
  global listaPartidos
  # Inicializo a cero la lista global
  listaPartidos=[]

  # Abro el fichero en lectura
  with open(filenameResultados2019,'r') as fd:
    first_line = fd.readline().strip()  # Leo la primera línea con las claves, quitando el \n
    keys=first_line.split(",")          # Guardo cada string separada por comas en la lista keys[]
    nKeys=len(keys)                     # También me guardo cuantas claves tengo.

    # Recorro el resto de líneas del fichero CSV
    for values_line in fd:  
      values_line=values_line.strip()   # Leo una línea y le quito el \n del final si lo tuviese.
      values=values_line.split(",")     # Guardo cada string separada por comas en la lista valores[]
      dict={}                           # Defino la variable "dict" como un diccionario vacío

      # Cada Clave recibe su Valor, el diccionario "dict" quedará así:
      #  { 'Round Number':<valor>, 
      #    'Date':<valor>, 
      #    'Location':<valor>, 
      #    'Home Team':<valor>, 
      #    'Away Team':<valor>, 
      #    'Result':<valor> 
      #  }
      for i in range(nKeys):  
        dict[keys[i]] = values[i]

      # Añado este Diccionario (resultados de este partido) a mi lista global
      listaPartidos.append(dict)

  if not ( len(listaPartidos) ):
    # Informa que el fichero fuente CSV debía venir sin datos válidos ... 
    print("Error: la base de datos está vacía, no tengo datos")
  
  return 



# Devolver información de un equipo concreto.
def infoEquipo(equipo):
  """ 
    Función que recibe un nombre de un equipo y muestra 
    cuales han sido sus paridos ganados, perdidos y empatados.

    Uso la función Quiniela() que me devuelve una lista de tuplas "nombre_equipo, diccionario_valores",
    y busco en ella al equipo sobre el cual de interrogan
    [
       ( "equipo1", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       ( "equipo2", {{ 'Puntos':x, 'Goles casa':x, 'Goles fuera':x, 'Goles total':x, 'Ganados':x, 'Perdidos':x, 'Empatados':x} ),
       :
    ]

  """

  # Si no le he hecho ya, leo el fichero CSV 
  if not (len(listaPartidos) ):
    LeerPartidos()

  # Pido la Quiniela a fecha de hoy
  now = datetime.now()
  quiniela = creaQuinielaHastaFecha(now.day, now.month, now.year)

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
# Muestro en pantalla la situación actual de la quiniela
def showQuiniela(quiniela):
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


#
# número de goles que ha metido, los paridos ganados, perdidos y empatados
#
# PT, PJ, PG, PE, PP, GF, GC
# PT: Puntos, 
# PJ: Partidos jugados, PG: Partidos Ganados
# PE: Partidos Empatados, PP: Partidos Perdidos, 
# GF: Goles a favor, GC: Goles en contra
def creaQuinielaHastaFecha(día, mes, año):
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
    showQuiniela(creaQuinielaHastaFecha(now.day, now.month, now.year))

  # Quiniela
  elif ( cmd == 4): 
    """
      **Quiniela por fecha:** Introducimos una fecha y nos dice los resultados de la quiniela de ese día.
    """
    día=int(input("Día: "))
    mes=int(input("Mes: "))
    año=int(input("Año: "))
    showQuiniela(creaQuinielaHastaFecha(día, mes, año))

  # Salir
  elif ( cmd == 0):
    print("Hasta luego lucas !!")
    break

  else:
    continue
