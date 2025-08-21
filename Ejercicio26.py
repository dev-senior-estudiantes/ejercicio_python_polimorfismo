# Define una clase para representar un punto en un plano 2D.
class Punto:
    # Utiliza __slots__ para optimizar el uso de memoria.
    # Esto predefine los atributos que la clase puede tener,
    # evitando la creación de un __dict__ para cada instancia.
    __slots__ = ["_x", "_y"]

    # El método de inicialización (constructor) de la clase.
    # Se llama cuando se crea una nueva instancia de Punto.
    # Asigna las coordenadas x e y a los atributos privados _x y _y.
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Define una propiedad de solo lectura para la coordenada x.
    # El decorador @property permite acceder a _x como si fuera un atributo público (p.x),
    # pero sin permitir la modificación directa.
    @property
    def x(self):
        return self._x

    # Define una propiedad de solo lectura para la coordenada y.
    # Similar a la propiedad x, protege el atributo _y.
    @property
    def y(self):
        return self._y

# Crea una instancia de la clase Punto con coordenadas (3, 5).
p = Punto(3, 5)

# Imprime las coordenadas del punto utilizando las propiedades x e y.
print(f"El punto es: {p.x}, {p.y}")

# Intenta modificar el valor de la propiedad 'x'.
# Esto fallará porque las propiedades se definieron como de solo lectura
# y no tienen un método 'setter' definido.
try:
    p.x = 10
# Captura la excepción AttributeError que se genera al intentar
# asignar un valor a una propiedad de solo lectura.
except AttributeError as e:
    # Imprime un mensaje de error para informar al usuario que la modificación no es posible.
    print(f"Error al intentar modificar 'x': {e}")