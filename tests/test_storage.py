import json

import pytest

from src.storage import Storage


def test_load_data_file_not_found(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    result = storage.load_data(str(file_path))

    assert result == []


def test_load_valid_json(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    data = [
        {
            "company": "Google",
            "position": "Python Developer"
        }
    ]

    file_path.write_text(
        json.dumps(data),
        encoding="utf-8"
    )

    result = storage.load_data(str(file_path))

    assert result == data


def test_load_invalid_json(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    file_path.write_text(
        "{ invalid json",
        encoding="utf-8"
    )

    result = storage.load_data(str(file_path))

    assert result == []


def test_load_json_that_is_not_a_list(tmp_path):
    storage = Storage()

    file_path = tmp_path / "jobs.json"

    data = {
        "company": "Google"
    }

    file_path.write_text(
        json.dumps(data),
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        storage.load_data(str(file_path))