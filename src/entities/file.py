
from dataclasses import dataclass,field
from datetime import datetime, timezone
from enum import Enum


def now()-> datetime:
    return datetime.now(timezone.utc)

class FileExtension(Enum):
    DOCX = "docx"
    PPT ="ppt"
    PDF = "pdf"
    TXT = "txt"
    PY = "py"
    JS ="js"

@dataclass
class File:
    name:str
    path:str
    type_file:FileExtension
    created_at:datetime = field(default_factory=now)
    modify_at:datetime =field(default_factory= now)

    def __post_init__(self) -> None: 
        self.validate_name()
        self.validate_path()

    def validate_name(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("file name can't be empty")
        self.name = self.name.strip()

    def validate_path(self) -> None:
        if not self.path or not self.path.strip():
            raise ValueError("file path can't be empty")
        self.path = self.path.strip()

    def rename(self, new_name: str) -> None:
        if not self.new_name or not self.new_name.strip:
            raise ValueError("you need to enter a name")
        self.name = new_name.strip()


    def change_extension(self,new_extension: str)-> None:
        if not self.new_extension :
            raise ValueError("extension cannot be empty")
        self.type_file= FileExtension(new_extension)
        
    def change_path(self,new_path :str):
        if not self.new_path or not self.new_path.strip():
            raise ValueError("path cannot be empty")
        self.path = new_path.strip()

