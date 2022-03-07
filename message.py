class Message:
    def __init__(self, line: str) -> None:
        self.__time: str = None
        self.__author: str = None
        self.__msg: str = None

        self.__time = line[0:7]

        cursor_end_location = line.index(': ')
        self.__author = line[8:cursor_end_location]

        cursor_start_location = line.index(': ')
        self.__msg = line[cursor_start_location+2:]

    def __str__(self) -> str:
        return f'{self.__time} {self.__author}: {self.__msg}'

    def time(self):
        return self.__time

    def author(self):
        return self.__author

    def message(self):
        return self.__msg
