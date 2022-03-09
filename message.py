class Message:
    def __init__(self, line: str) -> None:
        self.__time: str = None
        self.__author: str = None
        self.__msg: str = None

        try:
            if line[0] == '[' and line[6] == ']':
                self.__time = line[1:6]
        except:
            pass
        try:
            cursor_end_location = line.index(': ')
            self.__author = line[8:cursor_end_location]
        except:
            pass

        try:
            cursor_start_location = line.index(': ')
            self.__msg = line[cursor_start_location+2:]
        except:
            pass

    def __str__(self) -> str:
        return f'{self.__time} {self.__author}: {self.__msg}'

    def time(self):
        return self.__time

    def author(self):
        return self.__author

    def message(self):
        return self.__msg
