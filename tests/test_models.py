import pytest

from src.models import Job


def test_create_valid_job():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python", "Django"],
        application_date="2026-09-22",
        notes="Remote position"
    )

    assert job.company == "Google"
    assert job.position == "Python Developer"
    assert job.status == "Applied"
    assert job.technologies == ["Python", "Django"]
    assert job.application_date == "2026-09-22"
    assert job.notes == "Remote position"


def test_company_is_stripped():
    job = Job(
        company="  Google  ",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    assert job.company == "Google"


def test_position_is_stripped():
    job = Job(
        company="Google",
        position="  Python Developer  ",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    assert job.position == "Python Developer"


def test_technologies_are_stripped():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=[" Python ", " Django "],
        application_date="2026-09-22"
    )

    assert job.technologies == ["Python", "Django"]


def test_notes_are_stripped():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22",
        notes="  Remote position  "
    )

    assert job.notes == "Remote position"


def test_empty_company_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_company_with_only_spaces_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="   ",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_non_string_company_raises_error():
    with pytest.raises(ValueError):
        Job(
            company=123,
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_empty_position_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_position_with_only_spaces_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="   ",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_non_string_position_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position=123,
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_empty_technologies_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=[],
            application_date="2026-09-22"
        )


def test_technologies_must_be_list():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies="Python",
            application_date="2026-09-22"
        )


def test_technology_must_be_string():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python", 123],
            application_date="2026-09-22"
        )


def test_empty_technology_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python", ""],
            application_date="2026-09-22"
        )


def test_spaces_only_technology_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python", "   "],
            application_date="2026-09-22"
        )


def test_invalid_status_raises_error():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Invalid Status",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_status_must_be_string():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status=123,
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_change_status():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    job.change_status("Technical Interview")

    assert job.status == "Technical Interview"


def test_change_status_invalid():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    with pytest.raises(ValueError):
        job.change_status("Unknown")


def test_change_status_requires_string():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    with pytest.raises(ValueError):
        job.change_status(123)


def test_invalid_application_date_format():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="22-09-2026"
        )


def test_invalid_application_date():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-99-99"
        )


def test_application_date_must_be_string():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date=20260922
        )


def test_to_dict():
    job = Job(
        company="Google",
        position="Python Developer",
        status="Applied",
        technologies=["Python", "Django"],
        application_date="2026-09-22",
        notes="Remote position"
    )

    data = job.to_dict()

    assert data == {
        "company": "Google",
        "position": "Python Developer",
        "status": "Applied",
        "technologies": ["Python", "Django"],
        "application_date": "2026-09-22",
        "notes": "Remote position"
    }


def test_from_dict():
    data = {
        "company": "Google",
        "position": "Python Developer",
        "status": "Applied",
        "technologies": ["Python", "Django"],
        "application_date": "2026-09-22",
        "notes": "Remote position"
    }

    job = Job.from_dict(data)

    assert job.company == "Google"
    assert job.position == "Python Developer"
    assert job.status == "Applied"
    assert job.technologies == ["Python", "Django"]
    assert job.application_date == "2026-09-22"
    assert job.notes == "Remote position"


def test_from_dict_rejects_invalid_data():
    data = {
        "company": "",
        "position": "Python Developer",
        "status": "Applied",
        "technologies": ["Python"],
        "application_date": "2026-09-22",
        "notes": ""
    }

    with pytest.raises(ValueError):
        Job.from_dict(data)