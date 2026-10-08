from src.models import Job
from src.storage import Storage


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
        if not isinstance(job, Job):
            raise ValueError(
                "Job must be a Job instance."
            )

        existing_job = self.find_job(
            job.company,
            job.position
        )

        if existing_job is not None:
            raise ValueError(
                f"A job for {job.company} - "
                f"{job.position} already exists."
            )

        self.jobs.append(job)

        data = [
            job.to_dict()
            for job in self.jobs
        ]

        self.storage.save_data(
            self.file_path,
            data
        )

    def find_job(
        self,
        company: str,
        position: str
    ) -> Job | None:

        if not isinstance(company, str):
            raise ValueError(
                "Company must be a string."
            )

        if not isinstance(position, str):
            raise ValueError(
                "Position must be a string."
            )

        company = company.strip()
        position = position.strip()

        for job in self.jobs:
            if (
                job.company.lower() == company.lower()
                and
                job.position.lower() == position.lower()
            ):
                return job

        return None

    def find_by_status(
        self,
        status: str
    ) -> list[Job]:

        if not isinstance(status, str):
            raise ValueError(
                "Status must be a string."
            )

        status = status.strip()

        normalized_status = status.lower()

        matching_status = None

        for valid_status in Job.VALID_STATUSES:
            if valid_status.lower() == normalized_status:
                matching_status = valid_status
                break

        if matching_status is None:
            raise ValueError(
                f"Invalid status: {status}."
            )

        return [
            job
            for job in self.jobs
            if job.status == matching_status
        ]

    def find_by_technology(
        self,
        technology: str
    ) -> list[Job]:

        if not isinstance(technology, str):
            raise ValueError(
                "Technology must be a string."
            )

        technology = technology.strip()

        if not technology:
            raise ValueError(
                "Technology cannot be empty."
            )

        technology = technology.lower()

        return [
            job
            for job in self.jobs
            if any(
                job_technology.lower() == technology
                for job_technology in job.technologies
            )
        ]

    def get_statistics(self) -> dict:
        statistics = {
            "total": len(self.jobs)
        }

        for status in Job.VALID_STATUSES:
            statistics[status] = 0

        for job in self.jobs:
            statistics[job.status] += 1

        total_jobs = len(self.jobs)

        successful_jobs = (
            statistics["Offer"]
            + statistics["Hired"]
        )

        if total_jobs == 0:
            success_rate = 0.0
        else:
            success_rate = (
                successful_jobs / total_jobs
            ) * 100

        statistics["success_rate"] = round(
            success_rate,
            2
        )

        return statistics

    def get_jobs(self) -> list[Job]:
        return self.jobs.copy()

    def remove_job(
        self,
        company: str,
        position: str
    ) -> None:

        job_to_remove = self.find_job(
            company,
            position
        )

        if job_to_remove is None:
            raise ValueError(
                f"No job found for "
                f"{company} - {position}."
            )

        self.jobs.remove(job_to_remove)

        data = [
            job.to_dict()
            for job in self.jobs
        ]

        self.storage.save_data(
            self.file_path,
            data
        )

    def update_status(
        self,
        company: str,
        position: str,
        new_status: str
    ) -> None:

        job = self.find_job(
            company,
            position
        )

        if job is None:
            raise ValueError(
                f"Job Not Found: "
                f"{company} - {position}"
            )

        job.change_status(new_status)

        data = [
            job.to_dict()
            for job in self.jobs
        ]

        self.storage.save_data(
            self.file_path,
            data
        )