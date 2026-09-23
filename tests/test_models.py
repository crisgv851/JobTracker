import pytest

from src.models import Job


@pytest.fixture
def job():
    return Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python", "Django"],
        application_date="2026-09-22",
        notes="Remote position"
    )


def test_create_job(job):
    assert job.company == "Google"
    assert job.position == "Python Developer"
    assert job.status == "Applied"
    assert job.technologies == ["Python", "Django"]


def test_change_job_status(job):
    job.change_status("Technical Interview")

    assert job.status == "Technical Interview"


def test_invalid_status():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Invalid Status",
            technologies=["Python", "Django"],
            application_date="2026-09-22",
            notes="Remote position"
        )