from dbm import error
from pathlib import Path
from turtle import position

from models import Job
from storage import Storage
from job_manager import JobManager


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "jobs.json"


def show_menu():
    print("Job Tracker =)")
    print("1. Ver Trabajos")
    print("2. Agregar Trabajo")
    print("3. Buscar Trabajo")
    print("4. Actualizar Estado de Trabajo")
    print("5. Eliminar Trabajo")
    print("6. Salir")

def main():
    storage = Storage()

    manager = JobManager(
        storage, 
        str(DATA_FILE)
    )

    manager.load_jobs()


    while True:
        show_menu()

        option = input("Seleccione una opcion: ")

        if option == "1":
            show_jobs(manager)
        elif option == "2":
            add_jobs_cli(manager)
        elif option == "3":
            find_job_cli(manager)
        elif option == "4":
            update_status_cli(manager)
        elif option == "5":
            remove_job_cli(manager)
        elif option == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion valida.")

def show_jobs(manager: JobManager):
    jobs = manager.get_jobs()

    if not jobs:
        print("\nNO hay trabajos registrados.")
        return

    print("Trabajos Registrados")

    for index, job in enumerate(jobs, start=1):
        print(f"\n Trabajo {index}:")
        print(f"Empresa: {job.company}")    
        print(f"Cargo: {job.position}")
        print(f"Estado: {job.status}")
        print(f"Tecnologia: {job.technologies}")
        print(f"Fecha de Aplicacion: {job.application_date}")
        print(f"Notas: {job.notes}")

def add_jobs_cli(manager: JobManager):
    company = input("Ingrese el nombre de la empresa: ")
    position = input("Ingrese el cargo: ")
    status = input("Ingrese el estado del trabajo: ")
    technologies = input("Ingrese las tecnologias requeridas (separadas por comas): ")
    application_date = input("Ingrese la fecha de aplicacion (YYYY-MM-DD): ")
    notes = input("Ingrese notas adicionales: ")

    technologies = [
        technology.strip()
        for technology in technologies.split(",")
    ]
    try:
        job = Job(
            company=company,
            position=position,
            status=status,
            technologies=technologies,
            application_date=application_date,
            notes=notes
        )

        manager.add_job(job)
        print(f"Trabajo agregado exitosamente")

    except ValueError as error:
        print(f"\n Error: {error}")   

def find_job_cli(manager: JobManager):
    company = input("Ingrese el nombre de la empresa: ")
    position = input("Ingrese el cargo: ")

    job=manager.find_job(company, position)

    if job is None:
        print("\nTrabajo no encontrado.")
        return

    print(f"\nTrabajo encontrado:")
    print(f"Empresa: {job.company}")
    print(f"Cargo: {job.position}")
    print(f"Estado: {job.status}")
    print(f"Tecnologias: {', '.join(job.technologies)}")
    print(f"Fecha de Aplicacion: {job.application_date}")
    print(f"Notas: {job.notes}")

def update_status_cli(manager: JobManager):
    company = input("Ingrese el nombre de la empresa: ")
    position = input("Ingrese el cargo: ")
    new_status = input("Ingrese el nuevo estado del trabajo: ")

    try:
        manager.update_status(company, position, new_status)

        print(f"Estado del trabajo actualizado exitosamente.")

    except ValueError as error:
        print(f"\n Error: {error}")

def remove_job_cli(manager: JobManager):
    company = input("Ingrese el nombre de la empresa: ")
    position = input("Ingrese el cargo: ")

    try:
        manager.remove_job(company, position)
        print(f"Trabajo eliminado exitosamente.")
    except ValueError as error:
        print(f"\n Error: {error}")

if __name__ == "__main__":
    main()