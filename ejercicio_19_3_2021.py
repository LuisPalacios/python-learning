# Curso Python -
# 20210319. Luis Palacios
#

'''

    Create an application where an employee class is defined, 
   
    with a constructor that defines 4 attributes (name, position, salary, years in the company) 
    and two methods. 
    
    One of them will return to us if you charge more than 20k euros 
    and another one that includes a new attribute, 
    of the boolean type that confirms if you have been promoted or not.
    
    Create 10 employees with different information.
    
    Write in a file, a list of employees who charge less than 20k.
'''


#
# Clases
#
class Empleado: 
    """
        Concesionario y su lista de coches
        - string Nombre
        - string Ciudad
        - coches - Lista de Vehiculo()'s
    """
    def __init__(self, nombre, posicion, salario, years):
        self.setNombre(nombre)
        self.setPosicion(posicion)
        self.setSalario(salario)
        self.setYears(years)
        self.setPromoted(True)
        

    ## SETTERS
    def setNombre(self, elNombre):
        self.nombre = elNombre

    def setPosicion(self, laPosicion):
        self.posicion = laPosicion

    def setSalario(self, elSalario):
        self.salario = elSalario

    def setYears(self, losYears):
        self.years = losYears

    def setPromoted(self, promocion):
        self.promoted = promocion

    ## GETTERS
    def getNombre(self):
        return self.nombre

    def getPosicion(self):
        return self.posicion
        
    def getSalario(self):
        return self.salario

    def getYears(self):
        return self.years

    def getPromoted(self):
        return self.promoted
     
    # METODOS
    def isSalarioMayor20(self):
        if (self.getSalario()>20000):
            return True 
        return False

    def isPromoted(self):
        return self.getPromoted()
        

empleados = []
for i in range(10):
    empleados.append(Empleado("Empleado_"+str(i+1), "Currito", i*4000, 20+i))

for i in range(10):
    print("Empleado: " + empleados[i].getNombre() + " >20K: " + str(empleados[i].isSalarioMayor20()) + ". Promoted: " + str(empleados[i].isPromoted()))
    
