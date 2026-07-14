
from dataclasses import dataclass
from src.use_cases.interfaces.file_repository import FileRepository
from src.entities.file import File


@dataclass
class ReadFileInput:
    name: str


@dataclass
class ReadFileOutput:
    found: bool
    content: str = ""
    message: str = ""

class ReadFileUseCase:
    def __init__(self, repository: FileRepository) -> None:
        self.repository = repository

    def execute(self, input_data:ReadFileInput)->ReadFileOutput:
        content = self.repository.read_file(name= input_data.name)

        if content is None:
            return ReadFileOutput(
                found=False,
                message = f"file '{input_data.name}' is not found"
            )
        return ReadFileOutput(
            found = True,
            content = content
        )