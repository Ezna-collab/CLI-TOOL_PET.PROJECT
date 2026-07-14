from dataclasses import dataclass
from src.entities.file import File
from src.use_cases.interfaces.file_repository import FileRepository 

@dataclass
class DeleteFileInput:
    name : str

@dataclass
class DeleteFileOutput:
    success: bool
    message: str = "file has been deleted successfully"

class DeleteFileUseCase:
    def __init__(self,repository:FileRepository) -> None:
        self.repository = repository
        
    def execute(self,input_data:DeleteFileInput)-> DeleteFileOutput:
        file = self.repository.find_by_name(input_data.name)

        if file is None:
            raise ValueError(f"file '{input_data.name}' not found")
        self.repository.delete_file(input_data.name)
    
        return DeleteFileOutput(success = True)