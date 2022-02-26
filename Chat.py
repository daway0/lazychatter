class Chat:
    def __init__(self, file: str) -> None:
        self.__file_name = file
        self.chat_lines = []
        self.extract_chat()

    def extract_chat(self):
        with open(self.__file_name, 'r', encoding='utf-8') as chatfile:
            for line in chatfile:
                self.chat_lines.append(line)

    def class_date(self) -> str:
        cursor_end_location = len(self.__file_name) - \
            1 - self.__file_name[::-1].index('_')
        cursor_start_location = self.__file_name.index('_')+1
        return self.__file_name[cursor_start_location: cursor_end_location]

    def class_name(self) -> str:
        curosr_stop_location = self.__file_name.index('[')
        return self.__file_name[:curosr_stop_location]

    def file_name(self) -> str:
        return self.__file_name
