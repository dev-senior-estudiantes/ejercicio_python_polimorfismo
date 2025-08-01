"""Ejercicio 1. Definición de una clase simple y creación de un objeto

Crea una clase llamada Perro que represente a un perro. 
Esta clase no necesitará atributos ni métodos por ahora, 
solo servirá para demostrar la creación de una clase y un objeto. 
Luego, crea un objeto (una instancia) de esta clase.

Pseudocódigo:  
DEFINIR CLASE Perro
PASAR (No hacer nada por ahora) 
CREAR objeto mi_perro de tipo Perro 
IMPRIMIR tipo de mi_perro
"""

class Perro:
    pass

mi_perro = Perro()

print(f" Este es mi perro, de tipo {type(mi_perro)}")