import json

from src.storage import Storage


def test_save_and_load_data(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    data = [
        {
            "company": "Google",
            "position": "Python Developer"
        }
    ]

    storage.save_data(
        str(file_path),
        data
    )

    result = storage.load_data(
        str(file_path)
    )

    assert result == data


def test_load_missing_file(tmp_path):
    storage = Storage()

    file_path = tmp_path / "missing.json"

    result = storage.load_data(
        str(file_path)
    )

    assert result == []


def test_load_invalid_json(tmp_path):
    storage = Storage()

    file_path = tmp_path / "invalid.json"

    file_path.write_text(
        "{ invalid json",
        encoding="utf-8"
    )

    result = storage.load_data(
        str(file_path)
    )

    assert result == []


def test_load_json_that_is_not_list(tmp_path):
    storage = Storage()

    file_path = tmp_path / "object.json"

    file_path.write_text(
        json.dumps(
            {
                "company": "Google"
            }
        ),
        encoding="utf-8"
    )

    result = storage.load_data(
        str(file_path)
    )

    assert result == []


def test_save_empty_list(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    storage.save_data(
        str(file_path),
        []
    )

    result = storage.load_data(
        str(file_path)
    )

    assert result == []


def test_save_multiple_jobs(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    data = [
        {
            "company": "Google",
            "position": "Python Developer"
        },
        {
            "company": "Microsoft",
            "position": "Backend Developer"
        }
    ]

    storage.save_data(
        str(file_path),
        data
    )

    result = storage.load_data(
        str(file_path)
    )

    assert len(result) == 2
    assert result[0]["company"] == "Google"
    assert result[1]["company"] == "Microsoft"