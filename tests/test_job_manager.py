import pytest

from src.job_manager import JobManager
from src.models import Job
from src.storage import Storage


@pytest.fixture
def manager(tmp_path):
    storage = Storage()
    file_path = tmp_path / "jobs.json"

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


# ============================================================
# ADD JOB
# ============================================================

def test_add_job(manager, job):
    manager.add_job(job)

    jobs = manager.get_jobs()

    assert len(jobs) == 1
    assert jobs[0] == job


def test_add_job_requires_job_instance(manager):
    with pytest.raises(ValueError):
        manager.add_job(None)


def test_add_job_rejects_invalid_object(manager):
    with pytest.raises(ValueError):
        manager.add_job("not a job")


def test_add_duplicate_job(manager, job):
    manager.add_job(job)

    duplicate = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    with pytest.raises(ValueError):
        manager.add_job(duplicate)


# ============================================================
# FIND JOB
# ============================================================

def test_find_job(manager, job):
    manager.add_job(job)

    result = manager.find_job(
        "Google",
        "Python Developer"
    )

    assert result == job


def test_find_job_ignores_spaces(manager, job):
    manager.add_job(job)

    result = manager.find_job(
        "  Google  ",
        "  Python Developer  "
    )

    assert result == job


def test_find_job_is_case_insensitive(manager, job):
    manager.add_job(job)

    result = manager.find_job(
        "google",
        "python developer"
    )

    assert result is not None
    assert result.company == "Google"
    assert result.position == "Python Developer"


def test_find_job_returns_none_when_not_found(manager):
    result = manager.find_job(
        "Microsoft",
        "Developer"
    )

    assert result is None


def test_find_job_requires_company_string(manager):
    with pytest.raises(ValueError):
        manager.find_job(
            123,
            "Python Developer"
        )


def test_find_job_requires_position_string(manager):
    with pytest.raises(ValueError):
        manager.find_job(
            "Google",
            123
        )


# ============================================================
# FIND BY STATUS
# ============================================================

def test_find_by_status(manager, job):
    manager.add_job(job)

    results = manager.find_by_status("Applied")

    assert len(results) == 1
    assert results[0] == job


def test_find_by_status_is_case_insensitive(manager, job):
    manager.add_job(job)

    results = manager.find_by_status("applied")

    assert len(results) == 1
    assert results[0].status == "Applied"


def test_find_by_status_returns_empty_list(manager):
    results = manager.find_by_status("Applied")

    assert results == []


def test_find_by_status_invalid_status(manager):
    with pytest.raises(ValueError):
        manager.find_by_status("Invalid")


def test_find_by_status_requires_string(manager):
    with pytest.raises(ValueError):
        manager.find_by_status(123)


def test_find_by_status_ignores_spaces(manager, job):
    manager.add_job(job)

    results = manager.find_by_status(
        "  Applied  "
    )

    assert len(results) == 1


# ============================================================
# FIND BY TECHNOLOGY
# ============================================================

def test_find_by_technology(manager, job):
    manager.add_job(job)

    results = manager.find_by_technology("Python")

    assert len(results) == 1
    assert results[0] == job


def test_find_by_technology_is_case_insensitive(manager, job):
    manager.add_job(job)

    results = manager.find_by_technology("python")

    assert len(results) == 1


def test_find_by_technology_ignores_spaces(manager, job):
    manager.add_job(job)

    results = manager.find_by_technology(
        "  Python  "
    )

    assert len(results) == 1


def test_find_by_technology_returns_empty_list(manager):
    results = manager.find_by_technology("Python")

    assert results == []


def test_find_by_technology_requires_string(manager):
    with pytest.raises(ValueError):
        manager.find_by_technology(123)


def test_find_by_technology_rejects_empty_value(manager):
    with pytest.raises(ValueError):
        manager.find_by_technology("")


def test_find_by_technology_rejects_spaces(manager):
    with pytest.raises(ValueError):
        manager.find_by_technology("   ")


# ============================================================
# GET JOBS
# ============================================================

def test_get_jobs_returns_all_jobs(manager):
    job_1 = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    job_2 = Job(
        company="Microsoft",
        position="Backend Developer",
        status="Technical Interview",
        technologies=["C#", "Azure"],
        application_date="2026-09-23"
    )

    manager.add_job(job_1)
    manager.add_job(job_2)

    jobs = manager.get_jobs()

    assert len(jobs) == 2


def test_get_jobs_returns_copy(manager, job):
    manager.add_job(job)

    jobs = manager.get_jobs()

    jobs.clear()

    assert len(manager.get_jobs()) == 1


# ============================================================
# UPDATE STATUS
# ============================================================

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


def test_update_status_is_case_insensitive_for_job_search(
    manager,
    job
):
    manager.add_job(job)

    manager.update_status(
        "google",
        "python developer",
        "Technical Interview"
    )

    result = manager.find_job(
        "Google",
        "Python Developer"
    )

    assert result.status == "Technical Interview"


def test_update_status_invalid_status(manager, job):
    manager.add_job(job)

    with pytest.raises(ValueError):
        manager.update_status(
            "Google",
            "Python Developer",
            "Invalid"
        )


def test_update_status_job_not_found(manager):
    with pytest.raises(ValueError):
        manager.update_status(
            "Google",
            "Python Developer",
            "Hired"
        )


# ============================================================
# REMOVE JOB
# ============================================================

def test_remove_job(manager, job):
    manager.add_job(job)

    manager.remove_job(
        "Google",
        "Python Developer"
    )

    assert manager.get_jobs() == []


def test_remove_job_is_case_insensitive(manager, job):
    manager.add_job(job)

    manager.remove_job(
        "google",
        "python developer"
    )

    assert manager.get_jobs() == []


def test_remove_nonexistent_job(manager):
    with pytest.raises(ValueError):
        manager.remove_job(
            "Google",
            "Python Developer"
        )


# ============================================================
# LOAD JOBS / PERSISTENCE
# ============================================================

def test_load_jobs(manager, job):
    manager.add_job(job)

    new_manager = JobManager(
        manager.storage,
        manager.file_path
    )

    new_manager.load_jobs()

    jobs = new_manager.get_jobs()

    assert len(jobs) == 1
    assert jobs[0].company == "Google"


def test_load_jobs_persists_data(manager, job):
    manager.add_job(job)

    new_manager = JobManager(
        manager.storage,
        manager.file_path
    )

    new_manager.load_jobs()

    jobs = new_manager.get_jobs()

    assert len(jobs) == 1
    assert jobs[0].company == "Google"
    assert jobs[0].position == "Python Developer"
    assert jobs[0].status == "Applied"
    assert jobs[0].technologies == ["Python", "Django"]
    assert jobs[0].application_date == "2026-09-22"
    assert jobs[0].notes == "Remote position"


def test_load_jobs_empty_file(manager):
    manager.load_jobs()

    assert manager.get_jobs() == []


# ============================================================
# STATISTICS
# ============================================================

def test_get_statistics_empty(manager):
    statistics = manager.get_statistics()

    assert statistics["total"] == 0
    assert statistics["success_rate"] == 0.0


def test_get_statistics(manager):
    jobs = [
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        ),
        Job(
            company="Microsoft",
            position="Backend Developer",
            status="Technical Interview",
            technologies=["Python"],
            application_date="2026-09-23"
        ),
        Job(
            company="Amazon",
            position="Software Engineer",
            status="Rejected",
            technologies=["Java"],
            application_date="2026-09-24"
        )
    ]

    for job in jobs:
        manager.add_job(job)

    statistics = manager.get_statistics()

    assert statistics["total"] == 3
    assert statistics["Applied"] == 1
    assert statistics["Technical Interview"] == 1
    assert statistics["Rejected"] == 1


def test_get_statistics_success_rate(manager):
    jobs = [
        Job(
            company="Google",
            position="Developer",
            status="Offer",
            technologies=["Python"],
            application_date="2026-09-22"
        ),
        Job(
            company="Microsoft",
            position="Developer",
            status="Hired",
            technologies=["C#"],
            application_date="2026-09-23"
        ),
        Job(
            company="Amazon",
            position="Developer",
            status="Rejected",
            technologies=["Java"],
            application_date="2026-09-24"
        ),
        Job(
            company="Meta",
            position="Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-25"
        )
    ]

    for job in jobs:
        manager.add_job(job)

    statistics = manager.get_statistics()

    assert statistics["success_rate"] == 50.0