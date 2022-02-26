import os
from time import sleep
from turtle import delay


class DirectoryManager:

    @staticmethod
    def make_directories(directories_name_list: list) -> None:
        os.system('cls')
        for name in directories_name_list:
            try:
                os.mkdir(f'./{name}')
                print(f'{name} Created!')
                sleep(0.5)
            except:
                print(f'{name} is already created! ')
                sleep(0.5)
        sleep(1)
        os.system('cls')

    @staticmethod
    def import_chat_files():

        files = os.listdir()
        chat_files_number = 0
        chat_files = []

        for file in files:
            if not '[public-chat]' in file:
                continue

            chat_files_number += 1
            chat_files.append(file)
            print(file)
            sleep(0.01)

        if chat_files_number == 0:
            print('file not found !')
            sleep(1)
            os.system('cls')
            return False

        print('\n')
        ans = input(
            f'{chat_files_number} chat files collected, do you confirm it? (YES/NO)')

        if ans.lower() == 'yes':
            os.system('cls')
            delay(0.5)
            print('waiting...')
            return chat_files
        return False
