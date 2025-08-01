"""
Esta es una solución de ejemplo para un ejercicio.
Los desarrolladores colocarían aquí el código.
"""

class MiClase:
    """Clase que representa una persona y puede saludarla."""
    def __init__(self, nombre):
        """
        Inicializa una instancia de MiClase.

        Args:
            nombre (str): El nombre de la persona a saludar.
        """
        self.nombre = nombre

    def saludar(self):
        """
        Genera un saludo personalizado usando el nombre.

        Returns:
            str: Un saludo en formato de cadena.
        """
        return f"Hola, {self.nombre}"
