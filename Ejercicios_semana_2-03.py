
# Curso Python -
# 20210319. Luis Palacios
#

"""

Partimos del ejercicio 02. Editar el ejercicio anterior, para trabajar con POO en lugar de con ficheros.

Tendrán que existir 3 clases:

La clase vehiculo, que tendrá todas las características de cada vehículo anteriormente mencionadas.

La clase concesionario, que tendrá una lista de vehículos, así como información sobre su nombre, localización, etc.

La clase indice que contendrá una lista de todos los concesionarios de España.

Se deberán implementar los metodos get y set para acceder o asignar los atributos de una clase.

Elaborar los métodos necesarios para cada clase para poder reutilizar el mismo menu:

crear concesionario (se reclamarán N coches)
crear indice principal (Se reclamará una lista de concesionarios)
consultar concesionario
consultar por marca
consultar por precio
consultar por tipo
consultar el de menor precio
Indicar el número de coches dispobible que se tiene de algún tipo de coche

"""

#
# Clases
#
class Concesionario: 
    """
        Concesionario y su lista de coches
        - string Nombre
        - string Ciudad
        - coches - Lista de Vehiculo()'s
    """
    def __init__(self):
        self.coches=[]
        return

    def setNombre(self, elNombre):
        self.nombre = elNombre

    def setCiudad(self, laCiudad):
        self.ciudad = laCiudad

    def addCoche(self, coche):
        self.coches.append(coche)
        
    def getNombre(self):
        return self.nombre

    def getCiudad(self):
        return self.ciudad

    def getVehiculos(self):
        return self.coches

    def print(self):
        print(" ==> " + self.getNombre() + " - " + self.getCiudad()) 
        for coche in self.getVehiculos():
            coche.print()

class Vehiculo:
    """
        Vehículo concreto que irá en un concesionario:
        - string Matrícula
        - string Marca
        - int    Precio
        - string Tipo de vehículo (sedan, deportivo, sub...)
    """
    def __init__(self, laMatricula, laMarca, elPrecio, elTipo):
        self.matricula = laMatricula
        self.marca = laMarca
        self.precio = elPrecio
        self.tipo = elTipo

    def setMatricula(self, laMatricula):
        self.matricula = laMatricula

    def setMarca(self, laMarca):
        self.marca = laMarca

    def setPrecio(self, elPrecio):
        self.precio = elPrecio

    def setTipo(self, elTipo):
        self.tipo = elTipo

    def getMatricula(self):
        return self.matricula
        
    def getMarca(self):
        return self.marca
        
    def getPrecio(self):
        return self.precio

    def getTipo(self):
        return self.tipo

    def print(self):
        print("    >> ", self.matricula, " - ", self.tipo, " - ", self.marca, "  >> ", self.precio)


# ======= FUNCIONES
#

# DEVELOPER MODE: Muestra todos los concesionarios y equipos
def muestraConcesionarios(concesionarios):
    """
      Esta función no se expone al usuario, es útil para el desarrollador
    """
    for concesionario in concesionarios:
        concesionario.print()


# Crear Concesionario:
def crearConcesionario():
    """
      Crea un concesionario, pidiendo la creación de varios vehículos y 
      luego crea su fichero CSV y añáde su referencia al CSV principal
    """

    concesionario = Concesionario()

    # Pido el nombre del concesionario
    sNombre = input("Nombre del concesionario: ")
    concesionario.setNombre(sNombre)
    sCiudad = input("Ciudad del concesionario: ")
    concesionario.setCiudad(sCiudad)

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
        # Instancio el coche y lo guardo en el objeto concesionario
        concesionario.addCoche(Vehiculo(sMatrícula, sMarca, sPrecio, sTipo))

    return concesionario


# Consulta los datos de un concesionario concreto.
def consultaConcesionario(sNombreConcesionario, concesionarios):
    for concesionario in concesionarios:
        if ( concesionario.getNombre() == sNombreConcesionario ):
            concesionario.print()


# Consulta los datos de un concesionario concreto.
def consultaMarca(sMarca, concesionarios):
    for concesionario in concesionarios:
        for coche in concesionario.getVehiculos():
            if ( coche.getMarca() == sMarca ):
                coche.print()

# Muestra coches con precios menores al que nos pasan
def consultaPrecioMáximo(iPrecio, concesionarios):
    for concesionario in concesionarios:
        for coche in concesionario.getVehiculos():
            if ( int(coche.getPrecio()) <= iPrecio ):
                coche.print()


# Consulta los datos de un tipo de coche concreto.
def consultaTipo(sTipo, bSoloMostrarNúmero, concesionarios):

    num = 0
    for concesionario in concesionarios:
        for coche in concesionario.getVehiculos():
            if ( coche.getTipo() == sTipo ):
                if (bSoloMostrarNúmero == True):
                    num += 1
                else:
                    coche.print()
    print("Número de coches de tipo '"+sTipo+" disponibles: "+str(num))


# Consulta los datos de un tipo de coche concreto.
def consultaElMásBarato(concesionarios):
    menorValor = -1
    for concesionario in concesionarios:
        for coche in concesionario.getVehiculos():
            if (menorValor == -1 or int(coche.getPrecio()) < menorValor):
                menorValor = int(coche.getPrecio())
                elCoche = coche

    elCoche.print()
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
        # print("(8) Mostrar todos los concesionario y coches")
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

# Lista de concesionarios
concesionarios = []

# Bucle para mostrar el menú
#
while True:

    # Muestra el menú
    cmd = menu()

    # Salir
    if (cmd == 0):
        print("Hasta luego lucas !!")
        break

    # Crear concesionario y vehículos:
    elif (cmd == 1):
        concesionarios.append(crearConcesionario())
        for concesionario in concesionarios:
            concesionario.print()
        continue

    # Tengo que tener concesionarios o no sigo
    elif not ( len(concesionarios) ):
        print("Primero tienes que crear los concesionarios")
        continue

    # Consultar concesionario
    elif (cmd == 2):
        sNombreConcesionario = input("Nombre del concesionario: ")
        consultaConcesionario(sNombreConcesionario, concesionarios)
        continue

    # Consultar por marca
    elif (cmd == 3):
        sMarca = input("Nombre de la marca: ")
        consultaMarca(sMarca, concesionarios)
        continue

    # Consultar por precio
    elif (cmd == 4):
        iPrecio = int(input("Precio máximo: "))
        consultaPrecioMáximo(iPrecio, concesionarios)
        continue

    # Consultar por tipo
    elif (cmd == 5):
        sTipo = input("Tipo de coche: ")
        consultaTipo(sTipo, False, concesionarios)
        continue

    # Consultar el de menor precio de todos
    elif (cmd == 6):
        consultaElMásBarato(concesionarios)
        continue

    # Número de coches disponible según su tipo
    elif (cmd == 7):
        sTipo = input("Tipo de coche: ")
        consultaTipo(sTipo, True, concesionarios)
        continue

    # DEVELOPER MODE: Muestra todos los concesionarios y equipos
    # Esta opción no se muestra en el menú, pero viene bien durante la fase de desarrollo,
    elif (cmd == 8):
        muestraConcesionarios(concesionarios)
        continue

    else:
        continue
