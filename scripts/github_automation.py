import os
import random
import json
import requests
from dotenv import load_dotenv
from github import Github

# --- Configuración --- #
# Cargar variables de entorno desde el archivo .env
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME") # Formato: 'nombre_usuario/nombre_repositorio'

# Constantes de la organización y equipo
ORG_NAME = "dev-senior-estudiantes"
TEAM_SLUG = "python-dev-senior" # El 'slug' del equipo

# --- Funciones de Carga y Utilidades --- #

def cargar_ejercicios():
    """Carga los ejercicios desde el archivo JSON."""
    try:
        # La ruta es relativa a la ubicación del script
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

def add_issue_to_project_column(issue_id, column_id):
    """Añade un issue a una columna de un proyecto (clásico) usando la API REST."""
    url = f"https://api.github.com/projects/columns/{column_id}/cards"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.inertia-preview+json" # Header requerido por la API de Proyectos
    }
    data = {
        "content_id": issue_id,
        "content_type": "Issue"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Issue {issue_id} añadido a la columna {column_id} con éxito.")
    else:
        print(f"Error al añadir issue {issue_id} a la columna: {response.status_code} - {response.text}")

def main():
    """Función principal para automatizar la creación de issues y proyectos en GitHub."""
    # 1. Autenticación
    g = Github(GITHUB_TOKEN)

    # 2. Obtener la organización y el repositorio
    try:
        org = g.get_organization(ORG_NAME)
        repo = org.get_repo(REPO_NAME.split('/')[1])
    except Exception as e:
        print(f"Error al acceder a la organización o repositorio: {e}")
        return

    # 3. Obtener miembros del equipo
    try:
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

    # 5. Crear un nuevo proyecto Kanban
    project_name = "Proyecto de Ejercicios POO - Python"
    todo_column_id = None
    print(f"Creando o verificando proyecto '{project_name}'...")
    try:
        project = repo.create_project(project_name, body="Proyecto para gestionar los ejercicios de POO.")
        # Crear columnas Kanban
        todo_column = project.create_column("Pendiente")
        project.create_column("En Progreso")
        project.create_column("Finalizado")
        todo_column_id = todo_column.id
        print("Proyecto y columnas creadas con éxito.")
    except Exception as e:
        # Si el proyecto ya existe, búscalo para obtener el ID de la columna
        print(f"No se pudo crear el proyecto (puede que ya exista): {e}")
        projects = repo.get_projects(state='open')
        found_project = next((p for p in projects if p.name == project_name), None)
        if found_project:
            print(f"Encontrado proyecto existente '{project_name}'.")
            columns = found_project.get_columns()
            todo_column = next((c for c in columns if c.name == "Pendiente"), None)
            if todo_column:
                todo_column_id = todo_column.id
            else:
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
                labels=["ejercicio", "POO", "python"] # Etiquetas personalizables
            )
            print(f"Creado issue '{issue.title}' y asignado a '{assignee}'.")

            # Añadir el issue al proyecto
            if todo_column_id:
                add_issue_to_project_column(issue.id, todo_column_id)

        except Exception as e:
            print(f"Error al procesar el issue '{ejercicio['titulo']}': {e}")

    print("\n¡Proceso completado!")
    print(f"Los issues han sido creados y añadidos a la columna 'Pendiente' del proyecto '{project_name}'.")

if __name__ == "__main__":
    main()
