import os
import shutil


class DirectoryManager:

    @staticmethod
    def __remove_directory(directory: str):
        try:
            shutil.rmtree(directory)
        except:
            pass

    @staticmethod
    def make_directories(directories_name_list: list) -> None:
        
        for name in directories_name_list:
            DirectoryManager.__remove_directory(name)
            os.mkdir(f'./{name}')

        

    @staticmethod
    def import_chat_files() -> list:
        files = os.listdir()
        chat_files = []

        for file in files:
            if not '[public-chat]' in file:
                continue
            chat_files.append(file)

        return chat_files
