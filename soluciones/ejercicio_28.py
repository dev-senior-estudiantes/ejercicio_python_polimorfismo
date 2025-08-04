"""CLASE SingletonMeta HEREDA DE type
  _instancias = {}
  METODO __call__(...)
    SI clase NO ESTA EN _instancias
      _instancias[clase] = crear nueva instancia
    FIN SI
    RETORNAR _instancias[clase]
  FIN METODO
FIN CLASE"""



class SingletonMeta(type):
    # Diccionario para almacenar instancias únicas por clase
    _instancia = {}

    def __call__(cls, *args, **kwargs):
        # Si la clase no tiene instancia, crea una nueva
        if cls not in cls._instancia:
            cls._instancia[cls] = super().__call__(*args, **kwargs)
        # Retorna la instancia única
        return cls._instancia[cls]


class Misingleton(metaclass=SingletonMeta):
    # Clase que utiliza el patrón Singleton
    pass


if __name__ == "__main__":
    # Se crean dos instancias de Misingleton
    a = Misingleton()
    b = Misingleton()
    # Se verifica que ambas variables apunten a la misma instancia
    print(a is b)
