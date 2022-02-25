from cgitb import text
from Chat import Chat
from ChatDataExtractor import ChatDataExtractor
from Student import Student


class MesseageCategorizer:

    def __init__(self, chat: Chat) -> None:
        self.__chat_file_name = chat.get_file_name()
        self.__students = {}
        self.__create_time = chat.date()

    def update_student_name_set(self):
        pass

    def categorize(self):
        with open(self.__chat_file_name, 'r', encoding='utf-8') as chatfile:
            for line in chatfile:

                student_name = ChatDataExtractor.extract_message_author(line)

                if not (student_name in self.__students.keys()):
                    self.__students[student_name] = Student(student_name)

                
                text = ChatDataExtractor.extract_time_text(line)
                
                self.__students[student_name].add_message(text, self.__create_time)
    def students(self):
        return self.__students


chat1  = Chat('bbb-سیستم های عامل[public-chat]_2022-2-24_10-49.txt')
mo1= MesseageCategorizer(chat1)
mo1.categorize()

for student in mo1.students().values():
    student.export_chats()