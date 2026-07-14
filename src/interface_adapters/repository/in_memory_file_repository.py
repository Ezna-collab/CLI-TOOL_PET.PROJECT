
import json
from pathlib import Path

from src.entities.file import File, FileExtension
from src.use_cases.interfaces.file_repository import FileRepository


class JsonFileRepository(FileRepository):

    def __init__(self) -> None:
        self.file_path = Path("data/files.json")

        self.file_path.parent.mkdir(exist_ok=True)

        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def _load(self) -> list:
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save(self, data: list[dict]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def save_file(self, file: File) -> File:
        files = self._load()

        for item in files:
            if item["name"] == file.name:
                raise ValueError(
                    f"file '{file.name}' already exists"
                )

        files.append({
            "name": file.name,
            "content": file.content,
            "type_file": file.type_file.value
        })

        self._save(files)

        return file

    def find_by_name(self, name: str) -> File | None:
        files = self._load()

        for item in files:
            if item["name"] == name:
                return File(
                    name=item["name"],
                    content=item["content"],
                    type_file=FileExtension(
                        item["type_file"]
                    )
                )

        return None

    def read_file(self, name: str) -> str | None:
        file = self.find_by_name(name)

        if file:
            return file.content

        return None

    def delete_file(self, name: str) -> bool:
        files = self._load()

        new_files = [
            file
            for file in files
            if file["name"] != name
        ]

        if len(new_files) == len(files):
            raise ValueError(
                f"file '{name}' not found"
            )

        self._save(new_files)

        return True

    def get_all_files(self) -> list:
        files = self._load()

        return [
            File(
                name=item["name"],
                content=item["content"],
                type_file=FileExtension(
                    item["type_file"]
                )
            )
            for item in files
        ]

    def update_file(self, file: File) -> File:
        files = self._load()

        for item in files:
            if item["name"] == file.name:
                item["content"] = file.content
                item["type_file"] = file.type_file.value

                self._save(files)
                return file

        raise ValueError(
            f"file '{file.name}' not found"
        )
    

