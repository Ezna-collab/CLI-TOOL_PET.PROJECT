
from dataclasses import dataclass,field
from datetime import datetime, timezone
from typing import Optional
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
    content:str
    type_file:Optional[FileExtension] = None
    created_at:datetime = field(default_factory=now)
    modify_at:datetime =field(default_factory= now)

    def __post_init__(self) -> None: 
        self.validate_name()
        self.validate_type_file()

    def validate_name(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("file name can't be empty")
        self.name = self.name.strip()
    
    def validate_type_file(self) -> None:
        if "." not in self.name:
            raise ValueError("extension is required")
        extension = self.name.split(".")[-1].lower()
         
        try:
            self.type_file = FileExtension(extension)
        except:
            raise ValueError ("unsupported file extension")

