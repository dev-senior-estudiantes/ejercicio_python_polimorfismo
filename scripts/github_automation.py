"""
Para automatizar la creación y asignación de issues de ejercicios de POO en un repo de GitHub.
"""

import os
import random
import json
from dotenv import load_dotenv
from github import Github
from github.GithubException import GithubException

# --- Configuración --- #
# Cargar variables de entorno desde el archivo .env
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")  # Formato: 'nombre_usuario/nombre_repositorio'
ORG_PAT = os.getenv('ORG_PAT')

# Constantes de la organización y equipo
ORG_NAME = "dev-senior-estudiantes"
TEAM_SLUG = "python-dev-senior"  # El 'slug' del equipo

# --- Funciones de Carga y Utilidades --- #

def cargar_ejercicios():
    """Carga los ejercicios desde el archivo JSON."""
    try:
        script_dir = os.path.dirname(__file__)
        json_path = os.path.join(script_dir, 'ejercicios.json')
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'ejercicios.json'.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo 'ejercicios.json' tiene un formato inválido.")
        return []

def cargar_plantilla_issue():
    """Carga el contenido de la plantilla de issue."""
    try:
        script_dir = os.path.dirname(__file__)
        template_path = os.path.join(script_dir, "..", ".github", "ISSUE_TEMPLATE", "ejercicio_poo_template.md")
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: No se encontró la plantilla de issue en .github/ISSUE_TEMPLATE/")
        return None

def main():
    """Función principal para automatizar la creación de issues y proyectos en GitHub."""
    # Verificar que las variables de entorno están definidas
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN is not set")
        return None
    if not ORG_PAT:
        print("Error: ORG_PAT is not set")
        return None
    if not REPO_NAME:
        print("Error: REPO_NAME is not set")
        return None

    # 1. Autenticación
    g_repo = Github(GITHUB_TOKEN)  # Para operaciones de repositorio
    g_org = Github(ORG_PAT)  # Para operaciones de organización

    # 2. Obtener el repositorio
    try:
        repo = g_repo.get_repo(REPO_NAME)
    except GithubException as e:
        print(f"Error al acceder al repositorio: {e}")
        return None

    # 3. Obtener miembros del equipo
    try:
        org = g_org.get_organization(ORG_NAME)
        team = org.get_team_by_slug(TEAM_SLUG)
        team_members = [member.login for member in team.get_members()]
        if not team_members:
            print(f"El equipo '{TEAM_SLUG}' no tiene miembros. No se pueden asignar issues.")
            return None
    except GithubException as e:
        print(f"Error al obtener el equipo o sus miembros: {e}")
        return None

    # 4. Cargar plantillas y datos
    issue_template = cargar_plantilla_issue()
    if not issue_template:
        return None

    ejercicios_poo = cargar_ejercicios()
    if not ejercicios_poo:
        print("No se encontraron ejercicios en 'ejercicios.json'. Abortando.")
        return None

    # 5. Crear y asignar issues (sin gestión de proyectos clásicos ni columnas Kanban)
    print("\nCreando y asignando issues...")
    for ejercicio in ejercicios_poo:
        assignee = random.choice(team_members)
        # Formatear el cuerpo del issue
        issue_body = issue_template.format(
            planteamiento=ejercicio["planteamiento"],
            pseudocodigo=ejercicio["pseudocodigo"]
        )

        try:
            # Crear el issue
            issue = repo.create_issue(
                title=ejercicio["titulo"],
                body=issue_body,
                assignee=assignee,
                labels=["ejercicio", "POO", "python"]
            )
            print(f"Creado issue '{issue.title}' y asignado a '{assignee}'.")
        except (KeyError, TypeError) as e:
            print(f"Error en los datos del ejercicio '{ejercicio.get('titulo', 'Sin título')}': {e}")
        except GithubException as e:
            print(f"Error de GitHub al procesar el issue '{ejercicio.get('titulo', 'Sin título')}': {e}")

    print("\n¡Proceso completado!")
    print("Los issues han sido creados y asignados.")


if __name__ == "__main__":
    main()