
from typing import Any,Dict 

#from src.entities.file import File

from src.use_cases.interfaces.file_repository import FileRepository
from src.use_cases.create_file import CreateFileInput, CreateFileUseCase
from src.use_cases.delete_file import DeleteFileInput, DeleteFileUseCase
from src.use_cases.list_files import ListFileUseCase
from src.use_cases.modify_file import EditFileInput,EditFileUseCase
from src.use_cases.read_file import ReadFileInput, ReadFileUseCase
from src.interface_adapters.presenter.file_presenter import FilePresenter


class FileController:

    def __init__ (self,repository:FileRepository)->None:
        self.create_file_use_case = CreateFileUseCase(repository)
        self.delete_file_use_case = DeleteFileUseCase(repository)
        self.list_files_use_case = ListFileUseCase(repository)
        self.modify_file_use_case = EditFileUseCase(repository)
        self.read_file_use_case = ReadFileUseCase(repository)


    def create_file (self, data : Dict[str,Any]) -> Dict[str,Any]:
        name = data.get("name","" ).strip()
        if not name :
            return{"success": False,
                   "message" : "name is required"}
        output = self.create_file_use_case.execute(CreateFileInput
                                          (name = name,
                                           content = data.get("content","")
                                           ))
        return {
            "success" : True,
                "file": FilePresenter.to_dict(output.file),
                "message":output.message
                }
    
    def delete_file(self, name :str)-> Dict[str,Any]:
        output = self.delete_file_use_case.execute(DeleteFileInput(name))
        return {
            "success": output.success,
                "message": output.message
                }
    
    
    def list_files(self)-> list[dict[str,Any]]:
        output = self.list_files_use_case.execute()
        return {
            "success":True,
                "files":[FilePresenter.to_dict(f) for f in output.files]
                }
    
    
    def modify_file(self,data :Dict[str,Any])->Dict[str,Any]:
        name = data.get("name","").strip()

        output = self.modify_file_use_case.execute(
            EditFileInput(name=name, content=data.get("content", "") )
            )
        return{
            "success": True,
               "message":output.message,
               "file":FilePresenter.to_dict(output.file)
               }
    

    def read_file(self,name : str)->Dict[str,Any]:
        if not name:
            return {"success":False,
                    "message" :"name is required"}
        output =self.read_file_use_case.execute(ReadFileInput(name = name))
        return {
            "success": True,
                "content": output.content
                }



