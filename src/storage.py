import json
from pathlib import Path


class Storage:

    def save_data(self, file_path: str, data: list[dict]) -> None:
        path = Path(file_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with path.open(
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_data(self, file_path: str) -> list[dict]:
        path = Path(file_path)

        try:
            with path.open(
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

        if not isinstance(data, list):
            return []

        return data