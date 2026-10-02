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

def test_company_cannot_be_empty():
    with pytest.raises(ValueError):
        Job(
            company="",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-26",
            notes="Remote position"
        )


def test_position_cannot_be_empty():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-26",
            notes="Remote position"
        )        

def test_company_cannot_contain_only_spaces():
    with pytest.raises(ValueError):
        Job(
            company="   ",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-26",
            notes="Remote position"
        )


def test_position_cannot_contain_only_spaces():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="   ",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-26",
            notes="Remote position"
        )        

def test_application_date_must_have_valid_format():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="26/09/2026",
            notes="Remote position"
        )


def test_application_date_must_be_a_real_date():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-99-99",
            notes="Remote position"
        )        

def test_application_date_requires_exact_format():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-9-6",
            notes="Remote position"
        )