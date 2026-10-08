import json

from src.storage import Storage


def test_save_data(tmp_path):
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

    assert file_path.exists()

    with file_path.open(
        "r",
        encoding="utf-8"
    ) as file:
        result = json.load(file)

    assert result == data


def test_save_data_creates_parent_directory(
    tmp_path
):
    storage = Storage()

    file_path = (
        tmp_path
        / "data"
        / "jobs.json"
    )

    data = [
        {
            "company": "Google"
        }
    ]

    storage.save_data(
        str(file_path),
        data
    )

    assert file_path.exists()


def test_load_data(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    data = [
        {
            "company": "Google",
            "position": "Developer"
        }
    ]

    with file_path.open(
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(data, file)

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


def test_load_json_that_is_not_a_list(
    tmp_path
):
    storage = Storage()

    file_path = tmp_path / "object.json"

    file_path.write_text(
        '{"company": "Google"}',
        encoding="utf-8"
    )

    result = storage.load_data(
        str(file_path)
    )

    assert result == []