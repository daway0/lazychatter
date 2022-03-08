from chat import Chat
from message import Message


class ChatInfoExtractor:
    @staticmethod
    def class_date(chat: Chat) -> str:
        file_name = chat.file_name
        cursor_start_location = file_name.index(']')+2
        cursor_end_location = file_name[cursor_start_location::].index(
            '_')+cursor_start_location
        return file_name[cursor_start_location: cursor_end_location]

    @staticmethod
    def class_name(chat: Chat) -> str:
        file_name = chat.file_name
        cursor_start_location = file_name.index('-')+1
        curosr_stop_location = file_name.index('[')
        return file_name[cursor_start_location:curosr_stop_location]

    @staticmethod
    def start_end(chat: Chat) -> tuple:
        with open(chat.file_name, 'r', encoding='utf-8') as f:
            first_msg = Message(f.readline())
            for last_line in f:
                pass
            last_msg = Message(last_line)
            return (first_msg.time(), last_msg.time())
