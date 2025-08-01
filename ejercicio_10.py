from abc import ABC, abstractmethod
import math

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

print(f"El area del circulo de radio {circulo1.medicion} es {area1:.2f}")

cuadrado1 = Cuadrado(3)

#cálculo del área del cuadrado utilizando el método área y que ha sido modificado
#por la subclase cuadrado
area2 = cuadrado1.area()

print(area2)

