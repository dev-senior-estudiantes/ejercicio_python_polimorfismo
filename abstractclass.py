from abc import ABC, abstractmethod
import math

"""_summary_

Este archivo contiene un método abstracta que considera a la clase general forma y tiene
dos subclases implementan su método.

"""

#Clase Abstracta
class Forma(ABC):

    def __init__ (self, medicion):
        self.medicion = medicion

    #método abstracto
    @abstractmethod
    def area(self):
       pass
    

class Circulo(Forma):
    #este método encuentra el área de un círculo utilizando como atributo medición,
    #que corresponde al radio.
    def area(self):
       return math.pi*(self.medicion**2)
    

class Cuadrado(Forma):
    #este método calcula el área de un cuadrado utilzando como atributo medición,
    #que corresponde al lado.
    def area(self):
        return self.medicion**2



#creación del objeto círculo de radio 4
circulo1 = Circulo(4)

#cálculo del área del círculo utilizando el método área y que ha sido modificado
#por la subclase círculo
area1 = circulo1.area()

print(area1)

cuadrado1 = Cuadrado(3)

#cálculo del área del cuadrado utilizando el método área y que ha sido modificado
#por la subclase cuadrado
area2 = cuadrado1.area()
print(area2)

