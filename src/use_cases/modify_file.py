from dataclasses import dataclass
from src.entities.file import File, now
from src.use_cases.interfaces.file_repository import FileRepository

@dataclass
class EditFileInput:
    name :str
    content:str

@dataclass
class EditFileOutput:
    file: File
    message:str ="file has been modified successfully"

class EditFileUseCase:
    def __init__(self,repository:FileRepository) -> None:
        self.repository = repository

    def execute(self,input_data:EditFileInput)-> EditFileOutput:
        file = self.repository.find_by_name(input_data.name)

        if file is None:
            raise ValueError(f"file '{input_data.name}' not found")
        
        file.content = input_data.content
        file.modify_at = now()

        modified_file = self.repository.update_file(file)

        return EditFileOutput(file = modified_file)
