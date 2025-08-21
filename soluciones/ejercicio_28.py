"""
Este es el ejercicio 28 clase SingletonMeta.
"""


class SingletonMeta(type):
    """Define una metaclase llamada SingletonMeta, que hereda de 'type'."""

    _instancia = {}  # Diccionario que alamcena las clases únicas.

    def __call__(cls, *args, **kwargs):
        """llama cuando se intenta crear una instancia de una clase."""
        if (
            cls not in cls._instancia
        ):  # Comprueba si la clase (cls) ya tiene una instancia en el dict.
            # Crea la instancia de la clase con el constructor normal 'type'.
            cls._instancia[cls] = super().__call__(*args, **kwargs)
        return cls._instancia[
            cls
        ]  # Devuelve la instancia única (existente o recién creada).


class Misingleton(metaclass=SingletonMeta):
    """Define la clase Misingleton, con SingletonMeta como su metaclase."""

    def saludar(self) -> str:
        """Método de ejemplo para comprobar el Singleton."""
        return "Hola, soy la única instancia de Misingleton"

    def info(self) -> str:
        """Devuelve información de la instancia única."""
        return f"Soy la instancia única con id: {id(self)}"


if (
    __name__ == "__main__"
):  # Este bloque se ejecuta solo si el script se corre directamente.
    a = Misingleton()  # Crea la primera instancia de Misingleton.
    b = Misingleton()  # Intenta crear una segunda instancia de Misingleton.
    print(a is b)  # True si 'a' y 'b' son el mismo objeto.
    print(a.info())
    print(a.saludar())
    print(b.info())
    print(b.saludar())
