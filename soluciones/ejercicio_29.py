# Crear una clase `Contador` que actúe como un iterador, devolviendo números del 1 hasta un límite especificado."
class Contador:
    """
    Clase que actúa como iterador, devolviendo números del 1 hasta un límite especificado.
    """
    def __init__(self, limite): # Inicializa el contador con un limite
        self.limite = limite
        self.actual = 0 # Inicializa el contador '0' como contador interno
    
    def __iter__(self):
        return self # Retorna el objeto iterador
    
    def __next__(self): # Define que el objeto es iterable
        if self.actual < self.limite:
            self.actual += 1
            return self.actual # Retorna el siguiente numero de la secuencia
        else:
            raise StopIteration # Detiene la iteracion cuando se alcanza el limite

# Usar el iterador
for num in Contador(5):
    print(num)
    
