import time
import os

import sys
sys.stdout = open('[chat]output.txt', 'w', encoding='utf-8')


class Chat:
    def __init__(self, file: str) -> None:
        self.__file_name = file

    def date(self) -> str:
        return time.ctime(os.path.getctime(self.__file_name))

    def class_name(self) -> str:
        curosr_stop_location = self.__file_name.index('[')
        return self.__file_name[:curosr_stop_location]

    def get_file_name(self):
        return self.__file_name


def main():
    chat1 = Chat('bbb-تاریخ امامت[public-chat]_2022-2-23_17-52.txt')
    print(chat1.class_name())
    print(chat1.date())


if __name__ == '__main__':
    main()
