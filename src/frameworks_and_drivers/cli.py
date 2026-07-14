
import argparse

from src.interface_adapters.controller.file_controller import FileController
from src.interface_adapters.repository.in_memory_file_repository import  (JsonFileRepository)


class _C: 
    RESET = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[32m"
    CYAN   = "\033[36m"
    RED    = "\033[31m"

def _ok(msg:str)->None:
    print(f"{_C.GREEN} ✓ {msg}{_C.RESET}")

def _err(msg:str)-> None:
    print(f"{_C.RED}  ✗   {msg}{_C.RESET}")
        
def build_parser()-> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog= "file_manager",
    description="File Manager CLI With Clean ARchitecture")
    subparsers = parser.add_subparsers(dest="command", required = True)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~create a file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    parser_create_file =subparsers.add_parser("create-file",help = "create a new file")
    parser_create_file.add_argument("--name", required= True, help = "add file name")
    parser_create_file.add_argument("--content",default="", help="file content")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~read a file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    parser_read_file = subparsers.add_parser("read-file",help = "read a file")
    parser_read_file.add_argument("--name",required= True, help="add the name of the file you want to read")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~delete a file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    parser_delete_file=subparsers.add_parser("delete-file",help="delete a file")
    parser_delete_file.add_argument("--name",required=True,help="add the name of the file you want to delete")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~list files~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    subparsers.add_parser("list-files", help="list all the files")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~modify a file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    parser_modify_file = subparsers.add_parser("modify-file",help="modify a file")
    parser_modify_file.add_argument("--name",required=True,help="enter the name of the file")
    parser_modify_file.add_argument("--content",required=True, help= "enter a new content")

    return parser
    
def run_cli()->None:
    file_repo = JsonFileRepository()
    file_controller= FileController(file_repo)

    parser =  build_parser()
    args = parser.parse_args()


    try:
        if args.command == "create-file":
            result = file_controller.create_file({
                "name":args.name,
                "content": args.content})

            if result["success"]:
             _ok(result.get("message"))
            else:
                _err(result.get("error"))
    

        elif args.command == "read-file":
            result = file_controller.read_file(args.name)

            if result["success"]:
                print(result.get("content"))
            else:
                _err(result.get("error"))


        elif args.command == "delete-file":
            result = file_controller.delete_file(args.name)

            if result["success"]:
                _ok(result.get("message")) 
            else:
                _err(result.get("error"))


        elif args.command == "list-files":
             result = file_controller.list_files()

             if result["success"]:
                files =result.get("files",[])
                if not files:
                    print("no files found")
                else:
                    for file in files:
                        print(f"-{file['name']}")       
             else:
                _err(result.get("error"))


        elif args.command == "modify-file":
            result = file_controller.modify_file({"name":args.name,
                                              "content":args.content})
            if result["success"]:
                _ok(result.get("message")) 
            else:
                _err(result.get("data"))

    except ValueError as e:
        _err(str(e))