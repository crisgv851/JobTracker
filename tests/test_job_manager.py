import pytest

from src.job_manager import JobManager
from src.models import Job
from src.storage import Storage


@pytest.fixture
def manager(tmp_path):
    file_path = tmp_path / "jobs.json"
    storage = Storage()

    return JobManager(
        storage,
        str(file_path)
    )


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


def test_add_job(manager, job):
    manager.add_job(job)

    jobs = manager.get_jobs()

    assert len(jobs) == 1
    assert jobs[0].company == "Google"


def test_find_job(manager, job):
    manager.add_job(job)

    result = manager.find_job(
        "Google",
        "Python Developer"
    )

    assert result is not None
    assert result.company == "Google"


def test_prevent_duplicate_job(manager, job):
    manager.add_job(job)

    with pytest.raises(ValueError):
        manager.add_job(job)


def test_update_status(manager, job):
    manager.add_job(job)

    manager.update_status(
        "Google",
        "Python Developer",
        "Technical Interview"
    )

    result = manager.find_job(
        "Google",
        "Python Developer"
    )

    assert result.status == "Technical Interview"


def test_remove_job(manager, job):
    manager.add_job(job)

    manager.remove_job(
        "Google",
        "Python Developer"
    )

    assert len(manager.get_jobs()) == 0