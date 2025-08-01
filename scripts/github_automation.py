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

ORG_NAME = "dev-senior-estudiantes"
TEAM_SLUG = "python-dev-senior"

# --- Funciones de Carga y Utilidades --- #

def cargar_ejercicios():
    """Carga los ejercicios desde el archivo JSON."""
    try:
        script_dir = os.path.dirname(__file__)
        json_path = os.path.join(script_dir, 'ejercicios.json')
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo 'ejercicios.json'.")
    except json.JSONDecodeError:
        raise ValueError("El archivo 'ejercicios.json' tiene un formato inválido.")

def cargar_plantilla_issue():
    """Carga el contenido de la plantilla de issue."""
    try:
        script_dir = os.path.dirname(__file__)
        template_path = os.path.join(script_dir, "..", ".github", "ISSUE_TEMPLATE", "ejercicio_poo_template.md")
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró la plantilla de issue en .github/ISSUE_TEMPLATE/")

def main():
    """Función principal para automatizar la creación de issues y proyectos en GitHub."""
    try:
        # Verificar que las variables de entorno están definidas
        missing_vars = []
        if not GITHUB_TOKEN:
            missing_vars.append("GITHUB_TOKEN")
        if not ORG_PAT:
            missing_vars.append("ORG_PAT")
        if not REPO_NAME:
            missing_vars.append("REPO_NAME")
        if missing_vars:
            raise EnvironmentError(f"Faltan las siguientes variables de entorno: {', '.join(missing_vars)}")

        # 1. Autenticación
        g_repo = Github(GITHUB_TOKEN)
        g_org = Github(ORG_PAT)

        # 2. Obtener el repositorio
        try:
            repo = g_repo.get_repo(REPO_NAME)
        except GithubException as e:
            print(f"Error al acceder al repositorio: {e}")
            return

        # 3. Obtener miembros del equipo
        try:
            org = g_org.get_organization(ORG_NAME)
            team = org.get_team_by_slug(TEAM_SLUG)
            team_members = [member.login for member in team.get_members()]
            if not team_members:
                print(f"El equipo '{TEAM_SLUG}' no tiene miembros. No se pueden asignar issues.")
                return
        except GithubException as e:
            print(f"Error al obtener el equipo o sus miembros: {e}")
            return

        # 4. Cargar plantillas y datos
        try:
            issue_template = cargar_plantilla_issue()
            ejercicios_poo = cargar_ejercicios()
        except (FileNotFoundError, ValueError) as e:
            print(f"Error cargando archivos necesarios: {e}")
            return

        if not ejercicios_poo:
            print("No se encontraron ejercicios en 'ejercicios.json'. Abortando.")
            return

        # 5. Crear y asignar issues
        print("\nCreando y asignando issues...")
        for ejercicio in ejercicios_poo:
            assignee = random.choice(team_members)
            try:
                issue_body = issue_template.format(
                    planteamiento=ejercicio["planteamiento"],
                    pseudocodigo=ejercicio["pseudocodigo"]
                )
                issue = repo.create_issue(
                    title=ejercicio["titulo"],
                    body=issue_body,
                    assignee=assignee,
                    labels=["ejercicio", "POO", "python"]
                )
                print(f"Creado issue '{issue.title}' y asignado a '{assignee}'.")
            except KeyError as e:
                print(f"Error: falta la clave {e} en el ejercicio '{ejercicio.get('titulo', 'Sin título')}'.")
            except TypeError as e:
                print(f"Error de tipo en el ejercicio '{ejercicio.get('titulo', 'Sin título')}': {e}")
            except GithubException as e:
                print(f"Error de GitHub al procesar el issue '{ejercicio.get('titulo', 'Sin título')}': {e}")

        print("\n¡Proceso completado!")
        print("Los issues han sido creados y asignados.")

    except (FileNotFoundError, ValueError, EnvironmentError) as e:
        print(f"Error fatal: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
