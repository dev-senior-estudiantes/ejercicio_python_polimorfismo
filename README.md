## Gestión de Dependencias

Este proyecto utiliza un archivo `requirements.txt` para gestionar las dependencias de Python necesarias. En este archivo se listan las librerías requeridas para que el proyecto funcione correctamente, incluyendo sus versiones (si se especifican).

### Creación y Actualización del Archivo

Para generar o actualizar el archivo `requirements.txt` con las dependencias instaladas en tu entorno virtual, ejecuta:

```bash
pip freeze > requirements.txt
```

Este comando captura la lista de paquetes instalados (con sus versiones) y la guarda en `requirements.txt`.

### Instalación de las Dependencias

Para instalar todas las dependencias listadas en `requirements.txt`, abre la terminal en el directorio del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

Esto se encargará de descargar e instalar las librerías necesarias, tales como:

- **PyGithub**: Para interactuar con la API de GitHub.
- **python-dotenv**: Para cargar variables de entorno.
- **requests**: Para realizar peticiones HTTP.
- **pylint**: Para analizar la calidad del código.
- **numpy** y **pandas**: Para operaciones numéricas y manipulación de datos.
- **flake8**: Para el análisis de estilo y convenciones del código.

Este proceso garantiza que todos los colaboradores o estudiantes tengan las mismas dependencias y versiones en sus entornos de desarrollo.

# Workflows de Calidad en GitHub Actions

Este repositorio utiliza workflows de GitHub Actions para asegurar la calidad del código en cada Pull Request. A continuación se documentan los principales workflows:

## `pr-quality-checks.yml`

Este workflow se ejecuta automáticamente cada vez que se crea o actualiza un Pull Request. Sus funciones principales son:

- Analizar el código con el linter `flake8` para Python.
- Verificar formato, convenciones y posibles errores de estilo.
- Bloquear la fusión de PRs si no se cumplen los estándares de calidad.

**Ubicación:** `.github/workflows/pr-quality-checks.yml`

**Disparador:**

```yaml
on:
  pull_request:
    branches: [main, master]
```

**Ejemplo de pasos principales:**

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r scripts/requirements.txt
    pip install flake8

- name: Lint with flake8
  run: |
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## `pylint.yml` (opcional)

Puedes agregar un workflow adicional para ejecutar el linter `pylint` sobre el código Python del repositorio y asegurar el cumplimiento de buenas prácticas y detectar posibles errores.

**¿Qué revisa pylint?**

- Errores de sintaxis y posibles bugs.
- Cumplimiento de convenciones de estilo (PEP8).
- Código no usado, variables sin usar, importaciones innecesarias, etc.
- Asigna una puntuación de calidad al código.

**Ubicación sugerida:** `.github/workflows/pylint.yml`

**Disparador típico:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

**Ejemplo de paso principal:**

```yaml
- name: Run pylint
  run: |
    pip install pylint
    pylint scripts/
```

---

Estos workflows ayudan a mantener el código limpio, consistente y libre de errores antes de ser integrado a la rama principal.

# ejercicio_python_polimorfismo

repositorio para desarrollar habilidades de programacion orientada a objetos
