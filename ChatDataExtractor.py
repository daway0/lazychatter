
from Chat import Chat


class ChatDataExtractor():

    @staticmethod
    def __message_time(line: str) -> str:
        return line[1:6]

    @staticmethod
    def __message_text(line: str) -> str:
        try:
            cursor_start_location = line.index(': ')
            return line[cursor_start_location+1:]
        except:
            pass

    @staticmethod
    def message_author(line: str) -> str:
        try:
            cursor_end_location = line.index(': ')
            return line[8:cursor_end_location]
        except:
            pass

    @staticmethod
    def chatters(chat: Chat) -> set:
        chatters = set()
        for line in chat.chat_lines:
            chatters.add(ChatDataExtractor.message_author(line))
        return chatters

    @staticmethod
    def text_with_time(line: str) -> str:
        time = ChatDataExtractor.__message_time(line)
        message = ChatDataExtractor.__message_text(line)
        return f'[{time}] {message}'
