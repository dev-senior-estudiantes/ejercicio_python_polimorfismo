'''
CLASE Empleado
  METODO __init__(nombre, salario)
    self.nombre = nombre
    self.salario = salario
FIN CLASE

CLASE Gerente HEREDA DE Empleado
  METODO __init__(nombre, salario, departamento)
    super().__init__(nombre, salario)
    self.departamento = departamento
FIN CLASE
'''


class Empleado:
    """
    Representa a un empleado genérico dentro de la organización.

    Atributos
    ----------
    nombre : str
        Nombre del empleado.
    salario : float
        Salario asignado al empleado.
    """

    def __init__(self, nombre, salario):
        """
        Inicializa un nuevo objeto de tipo Empleado.

        Parámetros
        ----------
        nombre : str
            Nombre del empleado.
        salario : float
            Salario del empleado.
        """
        self.nombre = nombre
        self.salario = salario

    def get_nombre(self):
        """
    Método para obtener el nombre del empleado.

    """
        return self.nombre

    def set_nombre(self, value):
        """
    Método para setear el nombre del empleado.

    """
        self.nombre = value

    def get_salario(self):
        """
    Método para obtener el salario del empleado.

    """
        return self.salario

    def set_salario(self, value):
        """
    Método para setear el salario del empleado.

    """
        self.salario = value


class Gerente(Empleado):
    """
    Representa a un gerente, que es un tipo especializado de Empleado.

    Además de los atributos de `Empleado`, un gerente está asociado
    a un departamento específico.

    Atributos
    ----------
    nombre : str
        Nombre del gerente.
    salario : float
        Salario asignado al gerente.
    departamento : str
        Departamento que gestiona el gerente.
    """

    def __init__(self, nombre, salario, departamento):
        """
        Inicializa un nuevo objeto de tipo Gerente.

        Parámetros
        ----------
        nombre : str
            Nombre del gerente.
        salario : float
            Salario del gerente.
        departamento : str
            Nombre del departamento a cargo del gerente.
        """
        super().__init__(nombre, salario)
        self.departamento = departamento

    def get_departamento(self):
        """
    Método para obtener el departamento del gerente.

    """
        return self.departamento

    def set_departamento(self, value):
        """
    Método para setear el departamento del gerente.

    """
        self.departamento = value
