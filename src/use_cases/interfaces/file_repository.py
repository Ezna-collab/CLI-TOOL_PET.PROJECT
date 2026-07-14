from abc import ABC, abstractmethod
from src.entities.file import File

class FileRepository(ABC):
    
    @abstractmethod
    def save_file(self, file: File) -> File:
        ...

    @abstractmethod
    def read_file (self,name:str )-> str|None:
        ...

    @abstractmethod
    def find_by_name(self,name:str)-> File|None:
        ...

    @abstractmethod
    def delete_file(self,name:str)-> bool:
        ...
    
    @abstractmethod
    def get_all_files(self)-> list[File]:
        ...

    @abstractmethod
    def update_file(self, file :File)->File:
        ...

