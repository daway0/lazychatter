
from Chat import Chat
import sys
sys.stdout = open('[ChatDataExtractor]output.txt', 'w', encoding='utf-8')


class ChatDataExtractor():

    @staticmethod
    def extract_message_time(line: str) -> str:
        return line[1:6]
        # [16:52] اكبر توحيد لو: سلام

    @staticmethod
    def extract_message_text(line: str) -> str:
        try:
            cursor_start_location = line.index(': ')
            return line[cursor_start_location+1:]
        except:
            pass

    @staticmethod
    def extract_message_author(line: str) -> str:
        try:
            cursor_end_location = line.index(': ')
            return line[8:cursor_end_location]
        except:
            pass
        

    @staticmethod
    def extarct_chatters(chat: Chat):
        chatters = set()
        with open(chat.get_file_name(), 'r', encoding='utf-8') as file:
            for line in file:
                chatters.add(ChatDataExtractor.extract_message_author(line))
        return chatters

    @staticmethod
    def extract_time_text(line: str):
        time = ChatDataExtractor.extract_message_time(line)
        message = ChatDataExtractor.extract_message_text(line)
        return f'[{time}] {message}'

# with open ('bbb-تاریخ امامت[public-chat]_2022-2-23_17-52.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print (ChatDataExtractor.extract_time_text(line), end='')