"""
Este módulo define las clases de personajes y una fábrica para crearlos.

Sigue las convenciones de PEP 8 y buenas prácticas de diseño con POO.
"""

from abc import ABC, abstractmethod

class Personaje(ABC):
    """
    Clase base abstracta para todos los tipos de personajes.

    Define los atributos comunes y los métodos abstractos que todas
    las subclases de personaje deben implementar.
    """
    def __init__(self, nombre: str, vida: int, ataque: int, curacion_base = 5):
        """
        Inicializa un nuevo personaje.

        Args:
            nombre (str): El nombre del personaje.
            vida (int): Los puntos de vida iniciales del personaje.
            ataque (int): El valor de ataque base del personaje.
            curacion_base (int): Cantidad base que un personaje puede curarse.
        """
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.curacion_base = curacion_base
        self.esta_vivo = True
        
    @abstractmethod
    def atacar(self, objetivo):
        """
        Método abstracto para el ataque.

        Cada subclase de personaje debe implementar cómo ataca.
        Args:
            objetivo (Personaje): El personaje que será atacado.
        """
        pass
    
    @abstractmethod
    def curar(self):
        """
        Método abstracto para curarse.

        Cada subclase de personaje debe implementar cómo se cura.
        """
        pass

    def recibir_danio(self, cantidad_danio: int):
        """
        Gestiona la lógica cuando el personaje recibe daño.

        Args:
            cantidad_danio (int): La cantidad de daño a recibir.
        """
        if not self.esta_vivo:
            print(f"{self.nombre} ya está inconsciente y no puede recibir más daño.")
            return

        self.vida -= cantidad_danio
        print(f"{self.nombre} recibe {cantidad_danio} de daño.")
        if self.vida <= 0:
            self.vida = 0
            self.esta_vivo = False
            print(f"¡{self.nombre} ha sido derrotado!")
        else:
            print(f"Salud actual de {self.nombre}: {self.vida}")
            
# --- 2. Clases Concretas de Personaje (Implementan el "Molde") ---
class Guerrero(Personaje):
    """Clase que representa a un Guerrero."""

    def __init__(self, nombre: str):
        """
        Inicializa un nuevo Guerrero.

        Args:
            nombre (str): El nombre del guerrero.
        """
        self.vida_maxima = 150
        super().__init__(nombre, self.vida_maxima, 30, curacion_base=10)
        print(f"Guerrero {self.nombre} ha sido creado.")

    def atacar(self, objetivo: 'Personaje'):
        """
        Implementación de ataque para el Guerrero.
        """
        if not self.esta_vivo:
            print(f"{self.nombre} está inconsciente y no puede atacar.")
            return

        if not objetivo.esta_vivo:
            print(f"{objetivo.nombre} ya está derrotado.")
            return

        print(f"{self.nombre} (Guerrero) ataca con su espada a {objetivo.nombre}!")
        daño_infligido = self.ataque
        objetivo.recibir_danio(daño_infligido)

    def curar(self):
        """
        Implementación de curación para el Guerrero.
        """
        if not self.esta_vivo:
            print(f"{self.nombre} está inconsciente y no puede curarse.")
            return

        curacion_real = self.curacion_base + 5
        self.vida = min(self.vida_maxima, self.vida + curacion_real)
        print(
            f"{self.nombre} (Guerrero) se ha curado {curacion_real} puntos. "
            f"Salud actual: {self.vida}."
        )

class Mago(Personaje):
    """Clase que representa a un Mago."""

    def __init__(self, nombre: str):
        """
        Inicializa un nuevo Mago.

        Args:
            nombre (str): El nombre del mago.
        """
        self.vida_maxima = 80
        super().__init__(nombre, self.vida_maxima, 40, curacion_base=15)
        self.mana = 100  # Atributo específico del Mago
        print(f"Mago {self.nombre} ha sido creado.")

    def atacar(self, objetivo: 'Personaje'):
        """
        Implementación de ataque para el Mago.
        """
        if not self.esta_vivo:
            print(f"{self.nombre} está inconsciente y no puede atacar.")
            return
        if not objetivo.esta_vivo:
            print(f"{objetivo.nombre} ya está derrotado.")
            return

        if self.mana >= 10:
            print(f"{self.nombre} (Mago) lanza un hechizo a {objetivo.nombre}!")
            daño_infligido = self.ataque
            objetivo.recibir_danio(daño_infligido)
            self.mana -= 10
            print(f"Maná restante de {self.nombre}: {self.mana}")
        else:
            print(f"{self.nombre} no tiene suficiente maná para atacar.")

    def curar(self):
        """
        Implementación de curación para el Mago.
        """
        if not self.esta_vivo:
            print(f"{self.nombre} está inconsciente y no puede curarse.")
            return

        if self.mana >= 5:
            curacion_real = self.curacion_base + 10
            self.vida = min(self.vida_maxima, self.vida + curacion_real)
            self.mana -= 5
            print(
                f"{self.nombre} (Mago) se ha curado {curacion_real} puntos con magia. "
                f"Salud actual: {self.vida}. Maná restante: {self.mana}."
            )
        else:
            print(f"{self.nombre} no tiene suficiente maná para curarse.")

# --- 3. La Clase Fábrica (Implementa el Patrón Factory) ---
class FabricaPersonajes:
    """
    Fábrica para crear diferentes tipos de objetos Personaje.

    Implementa el Patrón Factory para desacoplar la creación
    de personajes del código cliente.
    """

    @staticmethod
    def crear_personaje(tipo_personaje: str, nombre_personaje: str) -> Personaje:
        """
        Método de fábrica para crear una instancia de un personaje.
        Args:
            tipo_personaje (str): El tipo de personaje a crear (ej. "Guerrero", "Mago").
            nombre_personaje (str): El nombre que se le dará al personaje.
        Returns:
            Personaje: Una instancia de la clase de personaje solicitada.
        """
        tipo_personaje_lower = tipo_personaje.lower()
        if tipo_personaje_lower == "guerrero":
            return Guerrero(nombre_personaje)
        if tipo_personaje_lower == "mago":
            return Mago(nombre_personaje)
        