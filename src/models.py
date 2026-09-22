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
        self.company = company
        self.position = position
        self.change_status(status)
        self.technologies = technologies
        self.application_date = application_date
        self.notes = notes

    def change_status(self, new_status: str) -> None:
        if new_status in self.VALID_STATUSES:
            self.status = new_status
        else:
            raise ValueError(
                f"Invalid status: {new_status}. "
                f"Valid statuses are: {', '.join(self.VALID_STATUSES)}"
            )

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