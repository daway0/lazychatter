
from datetime import date
from tkinter.tix import COLUMN
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

    @staticmethod
    def class_dates(files: str) -> list:
        dates = []

        for file in files:
            chatinfo = Chat(file)
            dates.append(chatinfo.class_date())

        dates.sort()
        column_number_date_dict = {}

        col = 1
        for date in dates:
            column_number_date_dict[col] = date
            col += 1
            #{1:'2022-6-6'}
        return column_number_date_dict
