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
    print("6. Buscar por empresa")
    print("7. Buscar por cargo")
    print("8. Filtrar por rango de fechas")
    print("9. Ver trabajos recientes")
    print("10. Actualizar estado")
    print("11. Eliminar trabajo")
    print("12. Ver estadísticas")
    print("13. Salir")


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
            find_by_company_cli(manager)

        elif option == "7":
            find_by_position_cli(manager)

        elif option == "8":
            find_by_date_range_cli(manager)

        elif option == "9":
            show_recent_jobs_cli(manager)

        elif option == "10":
            update_status_cli(manager)

        elif option == "11":
            remove_job_cli(manager)

        elif option == "12":
            show_statistics_cli(manager)

        elif option == "13":
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

    print_job(job)


def find_by_status_cli(manager: JobManager):
    status = input(
        "Ingrese el estado: "
    )

    try:
        jobs = manager.find_by_status(status)

        show_job_list(
            jobs,
            f"Trabajos con estado '{status.strip()}':"
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

        show_job_list(
            jobs,
            f"Trabajos que requieren "
            f"'{technology.strip()}':"
        )

    except ValueError as error:
        print(f"Error: {error}")


def find_by_company_cli(manager: JobManager):
    company = input(
        "Ingrese el nombre de la empresa: "
    )

    try:
        jobs = manager.find_by_company(
            company
        )

        show_job_list(
            jobs,
            f"Trabajos en '{company.strip()}':"
        )

    except ValueError as error:
        print(f"Error: {error}")


def find_by_position_cli(manager: JobManager):
    position = input(
        "Ingrese el cargo: "
    )

    try:
        jobs = manager.find_by_position(
            position
        )

        show_job_list(
            jobs,
            f"Trabajos para '{position.strip()}':"
        )

    except ValueError as error:
        print(f"Error: {error}")


def find_by_date_range_cli(manager: JobManager):
    start_date = input(
        "Ingrese la fecha inicial (YYYY-MM-DD): "
    )

    end_date = input(
        "Ingrese la fecha final (YYYY-MM-DD): "
    )

    try:
        jobs = manager.find_by_date_range(
            start_date,
            end_date
        )

        show_job_list(
            jobs,
            f"Trabajos entre "
            f"{start_date} y {end_date}:"
        )

    except ValueError as error:
        print(f"Error: {error}")


def show_recent_jobs_cli(manager: JobManager):
    limit_input = input(
        "¿Cuántos trabajos recientes desea ver? "
        "Presione Enter para 5: "
    ).strip()

    if not limit_input:
        limit = 5
    else:
        try:
            limit = int(limit_input)
        except ValueError:
            print(
                "Error: El límite debe ser un entero."
            )
            return

    try:
        jobs = manager.get_recent_jobs(limit)

        show_job_list(
            jobs,
            f"Trabajos más recientes ({limit}):"
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


def show_job(job: Job):
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


def show_job_list(
    jobs: list[Job],
    title: str
):
    if not jobs:
        print("No se encontraron trabajos.")
        return

    print(title)

    for index, job in enumerate(
        jobs,
        start=1
    ):
        print(
            f"{index}. "
            f"{job.company} - "
            f"{job.position} "
            f"({job.status}) - "
            f"{job.application_date}"
        )


if __name__ == "__main__":
    main()