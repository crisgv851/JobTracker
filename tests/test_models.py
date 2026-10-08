import pytest

from src.models import Job


def create_job(
    status="Applied",
    application_date="2026-09-22"
):
    return Job(
        company="Google",
        position="Python Developer",
        status=status,
        technologies=[
            "Python",
            "Django"
        ],
        application_date=application_date,
        notes="Backend position"
    )


def test_create_valid_job():
    job = create_job()

    assert job.company == "Google"
    assert job.position == "Python Developer"
    assert job.status == "Applied"
    assert job.technologies == [
        "Python",
        "Django"
    ]
    assert job.application_date == "2026-09-22"


def test_company_cannot_be_empty():
    with pytest.raises(ValueError):
        Job(
            company="",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )

    with pytest.raises(ValueError):
        Job(
            company="   ",
            position="Python Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_company_is_stripped():
    job = Job(
        company="  Google  ",
        position="Python Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    assert job.company == "Google"


def test_position_cannot_be_empty():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )

    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="   ",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22"
        )


def test_position_is_stripped():
    job = Job(
        company="Google",
        position="  Python Developer  ",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    assert job.position == "Python Developer"


def test_technologies_must_be_list():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies="Python",
            application_date="2026-09-22"
        )


def test_technologies_cannot_be_empty():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies=[],
            application_date="2026-09-22"
        )


def test_technologies_must_contain_strings():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies=[
                "Python",
                123
            ],
            application_date="2026-09-22"
        )


def test_technologies_cannot_contain_empty_values():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies=[
                "Python",
                ""
            ],
            application_date="2026-09-22"
        )

    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies=[
                "Python",
                "   "
            ],
            application_date="2026-09-22"
        )


def test_technologies_are_stripped():
    job = Job(
        company="Google",
        position="Developer",
        status="Applied",
        technologies=[
            " Python ",
            " Django "
        ],
        application_date="2026-09-22"
    )

    assert job.technologies == [
        "Python",
        "Django"
    ]


def test_application_date_cannot_be_empty():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies=["Python"],
            application_date=""
        )


def test_application_date_must_use_correct_format():
    with pytest.raises(ValueError):
        create_job(
            application_date="22-09-2026"
        )


def test_application_date_must_be_real_date():
    with pytest.raises(ValueError):
        create_job(
            application_date="2026-02-30"
        )


def test_application_date_accepts_valid_date():
    job = create_job(
        application_date="2026-10-08"
    )

    assert job.application_date == "2026-10-08"


def test_invalid_status():
    with pytest.raises(ValueError):
        create_job(
            status="Invalid Status"
        )


def test_change_status():
    job = create_job()

    job.change_status(
        "Technical Interview"
    )

    assert job.status == (
        "Technical Interview"
    )


def test_change_status_invalid():
    job = create_job()

    with pytest.raises(ValueError):
        job.change_status(
            "Invalid Status"
        )


def test_status_must_be_string():
    with pytest.raises(ValueError):
        create_job(
            status=123
        )


def test_notes_default_value():
    job = Job(
        company="Google",
        position="Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22"
    )

    assert job.notes == ""


def test_notes_must_be_string():
    with pytest.raises(ValueError):
        Job(
            company="Google",
            position="Developer",
            status="Applied",
            technologies=["Python"],
            application_date="2026-09-22",
            notes=123
        )


def test_notes_are_stripped():
    job = Job(
        company="Google",
        position="Developer",
        status="Applied",
        technologies=["Python"],
        application_date="2026-09-22",
        notes="  Remote position  "
    )

    assert job.notes == "Remote position"


def test_to_dict():
    job = create_job()

    data = job.to_dict()

    assert data == {
        "company": "Google",
        "position": "Python Developer",
        "status": "Applied",
        "technologies": [
            "Python",
            "Django"
        ],
        "application_date": "2026-09-22",
        "notes": "Backend position"
    }


def test_from_dict():
    data = {
        "company": "Google",
        "position": "Python Developer",
        "status": "Applied",
        "technologies": [
            "Python",
            "Django"
        ],
        "application_date": "2026-09-22",
        "notes": "Backend position"
    }

    job = Job.from_dict(data)

    assert job.company == "Google"
    assert job.position == "Python Developer"
    assert job.status == "Applied"


def test_is_active_when_applied():
    job = create_job(
        status="Applied"
    )

    assert job.is_active is True


def test_is_active_during_technical_assessment():
    job = create_job(
        status="Technical Assessment"
    )

    assert job.is_active is True


def test_is_active_during_hr_interview():
    job = create_job(
        status="HR Interview"
    )

    assert job.is_active is True


def test_is_active_during_technical_interview():
    job = create_job(
        status="Technical Interview"
    )

    assert job.is_active is True


def test_is_active_when_offer():
    job = create_job(
        status="Offer"
    )

    assert job.is_active is True


def test_is_not_active_when_hired():
    job = create_job(
        status="Hired"
    )

    assert job.is_active is False


def test_is_not_active_when_rejected():
    job = create_job(
        status="Rejected"
    )

    assert job.is_active is False