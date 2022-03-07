class MessageDataExtractor:

    @staticmethod
    def message_time(line: str) -> str:
        return line[0:7]

    @staticmethod
    def message_author(line: str) -> str:
        cursor_end_location = line.index(': ')
        return line[8:cursor_end_location]

    @staticmethod
    def message_text(line: str) -> str:
        cursor_start_location = line.index(': ')
        return line[cursor_start_location+1:]
