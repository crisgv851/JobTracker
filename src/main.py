from pathlib import Path

from src.models import Job
from src.storage import Storage
from src.job_manager import JobManager


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "jobs.json"


def show_menu():
    print("Job Tracker")
    print("1. Ver trabajos")
    print("2. Agregar trabajo")
    print("3. Buscar trabajo")
    print("4. Filtrar por estado")
    print("5. Buscar por tecnología")
    print("6. Actualizar estado")
    print("7. Eliminar trabajo")
    print("8. Ver estadísticas")
    print("9. Salir")


def main():
    storage = Storage()

    manager = JobManager(
        storage,
        str(DATA_FILE)
    )

    manager.load_jobs()

    while True:
        print()
        show_menu()

        option = input(
            "Seleccione una opción: "
        ).strip()

        if option == "1":
            show_jobs(manager)

        elif option == "2":
            add_job_cli(manager)

        elif option == "3":
            find_job_cli(manager)

        elif option == "4":
            find_by_status_cli(manager)

        elif option == "5":
            find_by_technology_cli(manager)

        elif option == "6":
            update_status_cli(manager)

        elif option == "7":
            remove_job_cli(manager)

        elif option == "8":
            show_statistics_cli(manager)

        elif option == "9":
            print("Saliendo del programa...")
            break

        else:
            print(
                "Opción no válida. "
                "Seleccione una opción válida."
            )


def show_jobs(manager: JobManager):
    jobs = manager.get_jobs()

    if not jobs:
        print("No hay trabajos registrados.")
        return

    print("Trabajos registrados:")

    for index, job in enumerate(
        jobs,
        start=1
    ):
        print(f"\nTrabajo {index}:")
        print(f"Empresa: {job.company}")
        print(f"Cargo: {job.position}")
        print(f"Estado: {job.status}")
        print(
            f"Tecnologías: "
            f"{', '.join(job.technologies)}"
        )
        print(
            f"Fecha de aplicación: "
            f"{job.application_date}"
        )
        print(f"Notas: {job.notes}")


def add_job_cli(manager: JobManager):
    company = input(
        "Ingrese el nombre de la empresa: "
    )

    position = input(
        "Ingrese el cargo: "
    )

    status = input(
        "Ingrese el estado del trabajo: "
    )

    technologies_input = input(
        "Ingrese las tecnologías requeridas "
        "(separadas por comas): "
    )

    application_date = input(
        "Ingrese la fecha de aplicación "
        "(YYYY-MM-DD): "
    )

    notes = input(
        "Ingrese notas adicionales: "
    )

    technologies = [
        technology.strip()
        for technology in technologies_input.split(",")
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

        print(
            "Trabajo agregado exitosamente."
        )

    except ValueError as error:
        print(f"Error: {error}")


def find_job_cli(manager: JobManager):
    company = input(
        "Ingrese el nombre de la empresa: "
    )

    position = input(
        "Ingrese el cargo: "
    )

    job = manager.find_job(
        company,
        position
    )

    if job is None:
        print("Trabajo no encontrado.")
        return

    print("Trabajo encontrado:")
    print(f"Empresa: {job.company}")
    print(f"Cargo: {job.position}")
    print(f"Estado: {job.status}")
    print(
        f"Tecnologías: "
        f"{', '.join(job.technologies)}"
    )
    print(
        f"Fecha de aplicación: "
        f"{job.application_date}"
    )
    print(f"Notas: {job.notes}")


def find_by_status_cli(manager: JobManager):
    status = input(
        "Ingrese el estado: "
    )

    try:
        jobs = manager.find_by_status(status)

        if not jobs:
            print(
                "No hay trabajos con ese estado."
            )
            return

        print(
            f"Trabajos con estado "
            f"'{status.strip()}':"
        )

        for index, job in enumerate(
            jobs,
            start=1
        ):
            print(
                f"{index}. "
                f"{job.company} - "
                f"{job.position} "
                f"({job.status})"
            )

    except ValueError as error:
        print(f"Error: {error}")


def find_by_technology_cli(manager: JobManager):
    technology = input(
        "Ingrese la tecnología: "
    )

    try:
        jobs = manager.find_by_technology(
            technology
        )

        if not jobs:
            print(
                "No hay trabajos que "
                "requieran esa tecnología."
            )
            return

        print(
            f"Trabajos que requieren "
            f"'{technology.strip()}':"
        )

        for index, job in enumerate(
            jobs,
            start=1
        ):
            print(
                f"{index}. "
                f"{job.company} - "
                f"{job.position}"
            )

    except ValueError as error:
        print(f"Error: {error}")


def update_status_cli(manager: JobManager):
    company = input(
        "Ingrese el nombre de la empresa: "
    )

    position = input(
        "Ingrese el cargo: "
    )

    new_status = input(
        "Ingrese el nuevo estado: "
    )

    try:
        manager.update_status(
            company,
            position,
            new_status
        )

        print(
            "Estado del trabajo "
            "actualizado exitosamente."
        )

    except ValueError as error:
        print(f"Error: {error}")


def remove_job_cli(manager: JobManager):
    company = input(
        "Ingrese el nombre de la empresa: "
    )

    position = input(
        "Ingrese el cargo: "
    )

    try:
        manager.remove_job(
            company,
            position
        )

        print(
            "Trabajo eliminado exitosamente."
        )

    except ValueError as error:
        print(f"Error: {error}")


def show_statistics_cli(manager: JobManager):
    statistics = manager.get_statistics()

    print("Estadísticas")
    print(
        f"Total de aplicaciones: "
        f"{statistics['total']}"
    )

    for status in Job.VALID_STATUSES:
        print(
            f"{status}: "
            f"{statistics[status]}"
        )

    print(
        f"Tasa de éxito: "
        f"{statistics['success_rate']}%"
    )


if __name__ == "__main__":
    main()