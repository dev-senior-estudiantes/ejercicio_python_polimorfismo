import os
import random
import json
from dotenv import load_dotenv
from github import Github

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
        return
    if not ORG_PAT:
        print("Error: ORG_PAT is not set")
        return
    if not REPO_NAME:
        print("Error: REPO_NAME is not set")
        return

    # 1. Autenticación
    g_repo = Github(GITHUB_TOKEN)  # Para operaciones de repositorio
    g_org = Github(ORG_PAT)  # Para operaciones de organización

    # 2. Obtener el repositorio
    try:
        repo = g_repo.get_repo(REPO_NAME)
    except Exception as e:
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
    except Exception as e:
        print(f"Error al obtener el equipo o sus miembros: {e}")
        return

    # 4. Cargar plantillas y datos
    issue_template = cargar_plantilla_issue()
    if not issue_template:
        return
    
    ejercicios_poo = cargar_ejercicios()
    if not ejercicios_poo:
        print("No se encontraron ejercicios en 'ejercicios.json'. Abortando.")
        return

    # 5. Crear o obtener el proyecto Kanban
    project_name = "Proyecto de Ejercicios POO - Python"
    print(f"Creando o verificando proyecto '{project_name}'...")
    try:
        # Intentar crear el proyecto
        project = repo.create_project(project_name, body="Proyecto para gestionar los ejercicios de POO.")
        # Crear columnas Kanban si no existen
        columns = project.get_columns()
        if not any(col.name == "Pendiente" for col in columns):
            todo_column = project.create_column("Pendiente")
        else:
            todo_column = next(col for col in columns if col.name == "Pendiente")
        if not any(col.name == "En Progreso" for col in columns):
            project.create_column("En Progreso")
        if not any(col.name == "Finalizado" for col in columns):
            project.create_column("Finalizado")
        print("Proyecto y columnas configuradas con éxito.")
    except Exception as e:
        # Si el proyecto ya existe, obtenerlo
        print(f"No se pudo crear el proyecto (puede que ya exista): {e}")
        projects = repo.get_projects(state='open')
        project = next((p for p in projects if p.name == project_name), None)
        if project:
            print(f"Encontrado proyecto existente '{project_name}'.")
            columns = project.get_columns()
            todo_column = next((c for c in columns if c.name == "Pendiente"), None)
            if not todo_column:
                print("Error: No se encontró la columna 'Pendiente' en el proyecto existente.")
                return
        else:
            print("Error: No se pudo encontrar un proyecto existente con ese nombre.")
            return

    # 6. Crear y asignar issues
    print("\nCreando, asignando y añadiendo issues al proyecto...")
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
                labels=["ejercicio", "POO", "python"]  # Etiquetas personalizables
            )
            print(f"Creado issue '{issue.title}' y asignado a '{assignee}'.")

            # Añadir el issue a la columna 'Pendiente'
            if todo_column:
                card = todo_column.create_card(content_id=issue.id, content_type="Issue")
                print(f"Issue {issue.id} añadido a la columna 'Pendiente' con éxito.")
        except Exception as e:
            print(f"Error al procesar el issue '{ejercicio['titulo']}': {e}")

    print("\n¡Proceso completado!")
    print(f"Los issues han sido creados y añadidos a la columna 'Pendiente' del proyecto '{project_name}'.")

if __name__ == "__main__":
    main()