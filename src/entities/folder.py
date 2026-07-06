
from dataclasses import dataclass,field
from datetime import datetime, timezone

def now()-> datetime:
    return datetime.now(timezone.utc)

@dataclass
class Folder:
    name:str
    path:str
    created_at: datetime = field(default_factory=now)
    modified_at: datetime = field(default_factory=now)
    default_folder: list = ["PDF","DOCX","PPT","TXT","PY","JS"]

    def __post_init__(self) -> None:
        self.validate_path()
        self.validate_name()

    def validate_name(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("folder name can't be empty")
        self.name = self.name.strip()
        
    def validate_path(self) -> None:    
        if not self.path or not self.path.strip():
            raise ValueError("folder path can't be empty")
        self.path = self.path.strip()

    def rename(self, new_name: str) -> None:
        if not self.new_name or not self.new_name.strip():
            raise ValueError("you need to enter a name")
        self.name=new_name

    def change_path(self,new_path :str):
        if not self.new_path or not self.new_path.strip():
            raise ValueError("path cannot be empty")
        self.path = new_path
    