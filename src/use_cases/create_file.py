
from dataclasses import dataclass
from src.entities.file import File
from src.use_cases.interfaces.file_repository import FileRepository

folder ="file"

@dataclass
class CreateFileInput :
    name:str
    content:str

@dataclass
class CreateFileOutput:
   file:File
   message:str ="file has been created successfully"



class CreateFileUseCase:
    def __init__(self, repository : FileRepository) -> None:
        self.repository = repository
    
    def execute(self, input_data: CreateFileInput) -> CreateFileOutput:

        file = File(name=input_data.name, content=input_data.content)

        save_file = self.repository.save_file(file)

        return CreateFileOutput(file = save_file)

