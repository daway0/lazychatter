from chat import Chat
from message_data_extractor import MessageDataExtractor


class ChatRepairman:
    def __init__(self, chat: Chat):
        self.__chat = chat
        self.__repaired_chat = Chat(chat.file_name)

    def repair(self):
        self.__repaired_chat.lines = []

        for line in self.__chat.lines:
            line = ChatRepairman.__remove_break(line)
            line = ChatRepairman.__remove_listenonly(line)

            if ChatRepairman.__is_empty_message(line):
                continue
            if ChatRepairman.__is_valid_chatline(line):
                self.__repaired_chat.lines.append(line)
                current_author = MessageDataExtractor.message_author(line)
                current_time = MessageDataExtractor.message_time(line)
                continue

            structured_message = f'{current_time} {current_author}: {line}'
            self.__repaired_chat.lines.append(structured_message)

        return self.__repaired_chat

    @classmethod
    def __is_valid_chatline(cls, line: str):
        if line[0] == '[' and line[3] == ':' and line[6] == ']':
            return True
        return False
    # valid chatline starts with:[00:00] bla bla bla

    @classmethod
    def __is_empty_message(cls, line: str):
        if line.replace(f'{MessageDataExtractor.message_time(line)} ', '') == '':
            return True
        return False
    # empty msg:[00:00] [empty]

    @classmethod
    def __remove_break(cls, line: str):
        return line.replace('\n', '')

    @classmethod
    def __remove_listenonly(cls, line: str):
        if 'LISTENONLY-' in line:
            return line.replace('LISTENONLY-', '')
        return line