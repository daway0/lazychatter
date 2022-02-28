import os


class DirectoryManager:

    @staticmethod
    def make_directories(directories_name_list: list) -> None:
        os.system('cls')
        for name in directories_name_list:
            try:
                os.mkdir(f'./{name}')

            except:
                pass

        os.system('cls')

    @staticmethod
    def import_chat_files() -> list:
        files = os.listdir()
        chat_files = []

        for file in files:
            if not '[public-chat]' in file:
                continue
            chat_files.append(file)

        return chat_files
