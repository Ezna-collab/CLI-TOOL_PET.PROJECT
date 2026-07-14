from datetime import datetime
from typing import List, Dict,Any
from src.entities.file import File



class FilePresenter:

    @ staticmethod
    def to_dict(file : File)->Dict[str,Any]:
        return{"name":file.name,
               "content": file.content,
               "type_file":file.type_file,
               "created_at":file.created_at.isoformat(),
               "modify_at":file.modify_at.isoformat()
               }
    @staticmethod
    def to_list(files:List[File])-> List[dict[str,Any]]:
        return [FilePresenter.to_dict(f) for f in files]

    