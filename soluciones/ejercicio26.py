# Define la clase Punto para representar un punto en un plano 2D.
class Punto:
    # Utiliza __slots__ para pre-declarar los atributos de la instancia.
    # Esto optimiza el uso de memoria y acelera el acceso a los atributos,
    # además de evitar la creación de __dict__ para cada instancia.
    __slots__ = ['_x', '_y']

    # El método de inicialización (constructor) de la clase.
    # Se llama cuando se crea una nueva instancia de Punto.
    # Asigna las coordenadas x e y a los atributos privados _x y _y.
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Define una propiedad de solo lectura para el atributo 'x'.
    # El decorador @property permite acceder al método x() como si fuera un atributo.
    @property
    def x(self):
        # Devuelve el valor del atributo privado _x.
        return self._x

    # Define una propiedad de solo lectura para el atributo 'y'.
    # El decorador @property permite acceder al método y() como si fuera un atributo.
    @property
    def y(self):
        # Devuelve el valor del atributo privado _y.
        return self._y

# Crea una instancia de la clase Punto con coordenadas (4, 6).
p = Punto(4, 6)

# Imprime las coordenadas del punto utilizando las propiedades x e y.
print(f"El punto es: ({p.x}, {p.y})") 

# Intenta modificar el valor de la propiedad 'x'.
# Esto generará un AttributeError porque las propiedades son de solo lectura
# (no se ha definido un @x.setter).
try:
    p.x = 10
# Captura la excepción AttributeError que se produce al intentar modificar 'x'.
except AttributeError as e:
    # Imprime un mensaje de error informando que no se puede modificar el atributo.
    print(f"Error al intentar modificar 'x': {e}")