# Este es un test de ejemplo.
# El workflow de GitHub Actions ejecutará los archivos de esta carpeta.

from soluciones.ejemplo_solucion import MiClase

def test_saludo():
    instancia = MiClase("Mundo")
    assert instancia.saludar() == "Hola, Mundo"
