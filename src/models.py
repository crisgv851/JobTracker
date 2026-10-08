from datetime import datetime


class Job:
    VALID_STATUSES = [
        "Applied",
        "Technical Assessment",
        "HR Interview",
        "Technical Interview",
        "Offer",
        "Hired",
        "Rejected"
    ]

    def __init__(
        self,
        company: str,
        position: str,
        status: str,
        technologies: list[str],
        application_date: str,
        notes: str = ""
    ):
        if not isinstance(company, str) or not company.strip():
            raise ValueError("Company cannot be empty.")

        self.company = company.strip()

        if not isinstance(position, str) or not position.strip():
            raise ValueError("Position cannot be empty.")

        self.position = position.strip()

        if not isinstance(technologies, list):
            raise ValueError("Technologies must be a list.")

        if not technologies:
            raise ValueError("Technologies cannot be empty.")

        if not all(
            isinstance(technology, str)
            for technology in technologies
        ):
            raise ValueError(
                "Each technology must be a string."
            )

        cleaned_technologies = [
            technology.strip()
            for technology in technologies
        ]

        if any(
            not technology
            for technology in cleaned_technologies
        ):
            raise ValueError(
                "Technologies cannot contain empty values."
            )

        self.technologies = cleaned_technologies

        self._validate_date(application_date)

        self.application_date = application_date

        self.change_status(status)

        if not isinstance(notes, str):
            raise ValueError("Notes must be a string.")

        self.notes = notes.strip()

    @staticmethod
    def _validate_date(application_date: str) -> None:
        if (
            not isinstance(application_date, str)
            or not application_date
        ):
            raise ValueError(
                "Application date cannot be empty."
            )

        try:
            parsed_date = datetime.strptime(
                application_date,
                "%Y-%m-%d"
            )

            if (
                parsed_date.strftime("%Y-%m-%d")
                != application_date
            ):
                raise ValueError

        except ValueError:
            raise ValueError(
                "Application date must have "
                "the format YYYY-MM-DD."
            )

    def change_status(self, new_status: str) -> None:
        if not isinstance(new_status, str):
            raise ValueError(
                "Status must be a string."
            )

        if new_status in self.VALID_STATUSES:
            self.status = new_status
        else:
            raise ValueError(
                f"Invalid status: {new_status}. "
                f"Valid statuses are: "
                f"{', '.join(self.VALID_STATUSES)}"
            )

    @property
    def is_active(self) -> bool:
        return self.status not in {
            "Hired",
            "Rejected"
        }

    def to_dict(self) -> dict:
        return {
            "company": self.company,
            "position": self.position,
            "status": self.status,
            "technologies": self.technologies,
            "application_date": self.application_date,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)