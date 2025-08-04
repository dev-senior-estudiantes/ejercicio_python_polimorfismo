"""
Este es el ejercicio 28 clase SingletonMeta.
"""


class SingletonMeta(type):
    """Define una metaclase llamada SingletonMeta, que hereda de 'type'."""

    _instancia = {}  # Diccionario para almacenar las instancias únicas de las clases.

    def __call__(cls, *args, **kwargs):
        """llama cuando se intenta crear una instancia de una clase."""
        if (
            cls not in cls._instancia
        ):  # Comprueba si la clase (cls) ya tiene una instancia en el diccionario.
            # Si no existe, crea la instancia de la clase usando el constructor normal de 'type'.
            cls._instancia[cls] = super().__call__(*args, **kwargs)
        return cls._instancia[
            cls
        ]  # Devuelve la instancia única (existente o recién creada).


class Misingleton(metaclass=SingletonMeta):
    """Define la clase Misingleton, especificando SingletonMeta como su metaclase."""


if (
    __name__ == "__main__"
):  # Este bloque se ejecuta solo si el script se corre directamente.
    a = Misingleton()  # Crea la primera instancia de Misingleton.
    b = Misingleton()  # Intenta crear una segunda instancia de Misingleton.
    print(
        a is b
    )  # Imprime True si 'a' y 'b' son el mismo objeto (lo que confirma el patrón Singleton).
