from chat import Chat
from chat_info_extractor import ChatInfoExtractor
from message_data_extractor import MessageDataExtractor
from professor import Professor
from student import Student


class ChatMesseageCategorizer:

    def __init__(self, chat: Chat, professor: Professor) -> None:
        self.__chat = chat
        self.__chat_professor = professor

    def categorize(self) -> None:
        for line in self.__chat.lines:

            student_name = MessageDataExtractor.message_author(line)

            if not student_name in self.__chat_professor.student_name_list():
                student = Student(student_name)
                self.__chat_professor.add_student(student)

            time = MessageDataExtractor.message_time(line)
            text = MessageDataExtractor.message_text(line)
            message = f'{time} {text}'
            student = self.__chat_professor.get_student(student_name)
            class_date = ChatInfoExtractor.class_date(self.__chat)

            student.add_message(message, class_date)
