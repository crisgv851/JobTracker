from models import Job
from storage import Storage


class JobManager:

    def __init__(self, storage: Storage, file_path: str):
        self.storage = storage
        self.file_path = file_path
        self.jobs: list[Job] = []

    def load_jobs(self) -> None:
        data = self.storage.load_data(self.file_path)

        self.jobs = [
            Job.from_dict(job_data)
            for job_data in data
        ]

    def add_job(self, job: Job) -> None:

        existing_job = self.find_job(job.company, job.position)

        if existing_job is not None:
            raise ValueError(
                f"A job for {job.company} - {job.position} already exists."
            )

        self.jobs.append(job)

        data = [
            job.to_dict()
            for job in self.jobs
        ]

        self.storage.save_data(self.file_path, data)

    def find_job(self, company: str, position: str) -> Job | None:
        for job in self.jobs:
            if job.company == company and job.position == position:
                return job

        return None

    def get_jobs(self) -> list[Job]:
        return self.jobs.copy()

    def remove_job(self, company: str, position: str) -> None:
        job_to_remove = self.find_job(company, position)

        if job_to_remove is None:
            raise ValueError(
                f"No job found for {company} - {position}."
            )

        self.jobs.remove(job_to_remove)

        data = [
            job.to_dict()
            for job in self.jobs
        ]

        self.storage.save_data(self.file_path, data)

    def update_status(
            self,
            company: str,
            position: str,
            new_status: str
    ) -> None:

        job = self.find_job(company, position)

        if job is None: 
            raise ValueError(
               f"Job Not Found: {company} - {position}"
            )

        job.change_status(new_status)

        data = [
            job.to_dict()
            for job in self.jobs
        ]

        self. storage.save_data(self.file_path, data)


















            