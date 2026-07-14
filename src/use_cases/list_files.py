from dataclasses import dataclass
from typing import List
from src.entities.file import File
from src.use_cases.interfaces.file_repository import FileRepository

@dataclass
class ListFileOutput:
    files: List[File]
    message:str = "here is the list of all files in the folder"

class ListFileUseCase:
    def __init__(self,repository:FileRepository):
        self.repository = repository
    
    def execute (self)->ListFileOutput:
        files = self.repository.get_all_files()

        if not files:
            return ListFileOutput(
                files=[],
                message="no files found in the folder"
                )
        
        return ListFileOutput(files = files)
