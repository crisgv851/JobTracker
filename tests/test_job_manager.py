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
        technologies=[
            "Python",
            "Django"
        ],
        application_date="2026-09-22",
        notes="Remote position"
    )


@pytest.fixture
def multiple_jobs():
    return [
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python", "Django"],
            application_date="2026-09-22"
        ),
        Job(
            company="Microsoft",
            position="Backend Developer",
            status="Technical Interview",
            technologies=["Python", "FastAPI"],
            application_date="2026-09-28"
        ),
        Job(
            company="Amazon",
            position="Software Engineer",
            status="Rejected",
            technologies=["Java", "AWS"],
            application_date="2026-09-15"
        ),
        Job(
            company="Google",
            position="Backend Developer",
            status="Offer",
            technologies=["Python", "FastAPI"],
            application_date="2026-10-01"
        )
    ]


def test_add_job(manager, job):
    manager.add_job(job)

    jobs = manager.get_jobs()

    assert len(jobs) == 1
    assert jobs[0] == job


def test_add_duplicate_job(manager, job):
    manager.add_job(job)

    duplicate = Job(
        company="google",
        position="python developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-25"
    )

    with pytest.raises(ValueError):
        manager.add_job(duplicate)


def test_find_job(manager, job):
    manager.add_job(job)

    result = manager.find_job(
        "Google",
        "Python Developer"
    )

    assert result == job


def test_find_job_case_insensitive(
    manager,
    job
):
    manager.add_job(job)

    result = manager.find_job(
        "google",
        "python developer"
    )

    assert result == job


def test_find_job_not_found(manager):
    result = manager.find_job(
        "Google",
        "Python Developer"
    )

    assert result is None


def test_find_job_invalid_company(manager):
    with pytest.raises(ValueError):
        manager.find_job(
            123,
            "Python Developer"
        )


def test_find_job_invalid_position(manager):
    with pytest.raises(ValueError):
        manager.find_job(
            "Google",
            123
        )


def test_find_by_company(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_company(
        "Google"
    )

    assert len(results) == 2

    assert all(
        job.company == "Google"
        for job in results
    )


def test_find_by_company_case_insensitive(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_company(
        "google"
    )

    assert len(results) == 2


def test_find_by_company_no_results(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_company(
        "Apple"
    )

    assert results == []


def test_find_by_company_empty(manager):
    with pytest.raises(ValueError):
        manager.find_by_company("")


def test_find_by_position(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_position(
        "Backend Developer"
    )

    assert len(results) == 2


def test_find_by_position_case_insensitive(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_position(
        "backend developer"
    )

    assert len(results) == 2


def test_find_by_position_no_results(
    manager
):
    results = manager.find_by_position(
        "Data Scientist"
    )

    assert results == []


def test_find_by_position_empty(manager):
    with pytest.raises(ValueError):
        manager.find_by_position("")


def test_find_by_status(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_status(
        "Applied"
    )

    assert len(results) == 1
    assert results[0].company == "Google"


def test_find_by_status_case_insensitive(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_status(
        "applied"
    )

    assert len(results) == 1


def test_find_by_status_invalid(manager):
    with pytest.raises(ValueError):
        manager.find_by_status(
            "Unknown"
        )


def test_find_by_technology(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_technology(
        "Python"
    )

    assert len(results) == 3


def test_find_by_technology_case_insensitive(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_technology(
        "python"
    )

    assert len(results) == 3


def test_find_by_technology_no_results(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_technology(
        "Docker"
    )

    assert results == []


def test_find_by_technology_empty(manager):
    with pytest.raises(ValueError):
        manager.find_by_technology("")


def test_find_by_date_range(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_date_range(
        "2026-09-20",
        "2026-09-30"
    )

    assert len(results) == 2

    assert all(
        "2026-09-20"
        <= job.application_date
        <= "2026-09-30"
        for job in results
    )


def test_find_by_date_range_includes_boundaries(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_date_range(
        "2026-09-22",
        "2026-09-28"
    )

    dates = [
        job.application_date
        for job in results
    ]

    assert "2026-09-22" in dates
    assert "2026-09-28" in dates


def test_find_by_date_range_no_results(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.find_by_date_range(
        "2026-11-01",
        "2026-11-30"
    )

    assert results == []


def test_find_by_date_range_invalid_start_date(
    manager
):
    with pytest.raises(ValueError):
        manager.find_by_date_range(
            "invalid",
            "2026-09-30"
        )


def test_find_by_date_range_invalid_end_date(
    manager
):
    with pytest.raises(ValueError):
        manager.find_by_date_range(
            "2026-09-01",
            "invalid"
        )


def test_find_by_date_range_start_after_end(
    manager
):
    with pytest.raises(ValueError):
        manager.find_by_date_range(
            "2026-10-01",
            "2026-09-01"
        )


def test_sort_jobs_by_date_descending(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.sort_by_date()

    dates = [
        job.application_date
        for job in results
    ]

    assert dates == [
        "2026-10-01",
        "2026-09-28",
        "2026-09-22",
        "2026-09-15"
    ]


def test_sort_jobs_by_date_ascending(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.sort_by_date(
        descending=False
    )

    dates = [
        job.application_date
        for job in results
    ]

    assert dates == [
        "2026-09-15",
        "2026-09-22",
        "2026-09-28",
        "2026-10-01"
    ]


def test_sort_jobs_does_not_modify_original_list(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    original_order = manager.get_jobs()

    manager.sort_by_date()

    assert manager.get_jobs() == original_order


def test_sort_jobs_invalid_descending(
    manager
):
    with pytest.raises(ValueError):
        manager.sort_by_date(
            descending="yes"
        )


def test_get_recent_jobs(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.get_recent_jobs()

    assert len(results) == 4

    assert results[0].application_date == (
        "2026-10-01"
    )


def test_get_recent_jobs_respects_limit(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.get_recent_jobs(2)

    assert len(results) == 2

    assert results[0].application_date == (
        "2026-10-01"
    )

    assert results[1].application_date == (
        "2026-09-28"
    )


def test_get_recent_jobs_returns_all_when_limit_is_greater(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    results = manager.get_recent_jobs(100)

    assert len(results) == 4


def test_get_recent_jobs_invalid_limit_zero(
    manager
):
    with pytest.raises(ValueError):
        manager.get_recent_jobs(0)


def test_get_recent_jobs_invalid_limit_negative(
    manager
):
    with pytest.raises(ValueError):
        manager.get_recent_jobs(-1)


def test_get_recent_jobs_invalid_limit_type(
    manager
):
    with pytest.raises(ValueError):
        manager.get_recent_jobs("5")


def test_get_recent_jobs_does_not_modify_original_list(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    original_order = manager.get_jobs()

    manager.get_recent_jobs(2)

    assert manager.get_jobs() == original_order


def test_get_jobs_returns_copy(
    manager,
    job
):
    manager.add_job(job)

    jobs = manager.get_jobs()

    jobs.clear()

    assert len(manager.get_jobs()) == 1


def test_update_status(
    manager,
    job
):
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

    assert result.status == (
        "Technical Interview"
    )


def test_update_status_job_not_found(
    manager
):
    with pytest.raises(ValueError):
        manager.update_status(
            "Google",
            "Python Developer",
            "Offer"
        )


def test_remove_job(
    manager,
    job
):
    manager.add_job(job)

    manager.remove_job(
        "Google",
        "Python Developer"
    )

    assert manager.get_jobs() == []


def test_remove_job_not_found(manager):
    with pytest.raises(ValueError):
        manager.remove_job(
            "Google",
            "Python Developer"
        )


def test_load_jobs(
    manager,
    job
):
    manager.add_job(job)

    new_manager = JobManager(
        manager.storage,
        manager.file_path
    )

    new_manager.load_jobs()

    assert len(new_manager.get_jobs()) == 1

    assert (
        new_manager.get_jobs()[0].company
        == "Google"
    )


def test_statistics(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    statistics = manager.get_statistics()

    assert statistics["total"] == 4
    assert statistics["Applied"] == 1
    assert statistics["Technical Interview"] == 1
    assert statistics["Offer"] == 1
    assert statistics["Rejected"] == 1


def test_success_rate(
    manager,
    multiple_jobs
):
    for job in multiple_jobs:
        manager.add_job(job)

    statistics = manager.get_statistics()

    assert statistics["success_rate"] == 25.0