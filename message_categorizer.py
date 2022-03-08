from chat import Chat
from chat_info_extractor import ChatInfoExtractor
from professor import Professor
from student import Student


class ChatMesseageCategorizer:

    def __init__(self, chat: Chat, professor: Professor) -> None:
        self.__chat = chat
        self.__chat_professor = professor

    def categorize(self) -> None:
        for msg in self.__chat.messages:

            student_name = msg.author()

            if not student_name in self.__chat_professor.student_name_list():
                student = Student(student_name)
                self.__chat_professor.add_student(student)

            time = msg.time()
            text = msg.message()
            message = f'{time} {text}'
            student = self.__chat_professor.get_student(student_name)
            class_date = ChatInfoExtractor.class_date(self.__chat)

            student.add_message(message, class_date)
            student.msgpp_in_time(time)
