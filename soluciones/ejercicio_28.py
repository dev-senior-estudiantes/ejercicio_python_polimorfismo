'''CLASE SingletonMeta HEREDA DE type
  _instancias = {}
  METODO __call__(...)
    SI clase NO ESTA EN _instancias
      _instancias[clase] = crear nueva instancia
    FIN SI
    RETORNAR _instancias[clase]
  FIN METODO
FIN CLASE'''


class SingletonMeta(type):
    _instancia = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancia:
            cls._instancia[cls] = super().__call__(*args, **kwargs)
        return cls._instancia[cls]


class Misingleton(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    a = Misingleton()
    b = Misingleton()
    print(a is b)
