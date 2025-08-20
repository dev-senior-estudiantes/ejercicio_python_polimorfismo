"""Módulo que define una clase de formas con un método abstracto
para calcular el área. Se implementan dos formas: Círculo y Cuadrado.
"""

from abc import ABC, abstractmethod
import math


class Forma(ABC):
    """
    Clase abstracta que representa una forma geométrica.

    Atributos:
        medicion (float): define la medida base de la forma (radio, lado, etc.).
    """

    def __init__(self, medicion):
        """
        Inicializa la forma con una medida dada.

        Args:
            medicion (float): medida para el cálculo del área.
        """
        self.medicion = medicion

    @abstractmethod
    def area(self):
        """
        Calcula el área de la forma.

        Returns:
            float: Área de la forma.
        """
class Circulo(Forma):
    """
    Clase que representa un círculo, derivada de Forma.
    """

    def area(self):
        """
        Calcula el área de un círculo usando el radio.
        """
        return math.pi * (self.medicion ** 2)


class Cuadrado(Forma):
    """
    Clase que representa un cuadrado, derivada de Forma.
    """

    def area(self):
        """
        Calcula el área de un cuadrado usando el lado.

        Returns:
            float: Área del cuadrado.
        """
        return self.medicion ** 2


# Crear un objeto Círculo con radio 4 y calcular su área
circulo1 = Circulo(4)
area1 = circulo1.area()
print(area1)

# Crear un objeto Cuadrado con lado 3 y calcular su área
cuadrado1 = Cuadrado(3)
area2 = cuadrado1.area()
print(area2)
