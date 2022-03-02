from Chat import Chat
from ChatDataExtractor import ChatDataExtractor
from Professor import Professor
from Student import Student


class ChatMesseageCategorizer:

    def __init__(self, chat: Chat, professor: Professor) -> None:
        self.__chat = chat
        self.__chat_professor = professor

    def categorize(self) -> None:
        for line in self.__chat.chat_lines:
            
            if ChatDataExtractor.is_chatline_valid(line):
                student_name = ChatDataExtractor.message_author(line)
                if not student_name in self.__chat_professor.student_name_list():
                    student = Student(student_name)
                    self.__chat_professor.add_student(student)

                text = ChatDataExtractor.text_with_time(line)
                self.__chat_professor.get_student(student_name).add_message(
                    text, self.__chat.class_date())

                previous_chat_author = student_name
                previous_message_time = ChatDataExtractor.message_time(line)
                
            else:
                unstructured_text_message = f'[{previous_message_time}]  {line}'
                self.__chat_professor.get_student(previous_chat_author).add_message(
                    unstructured_text_message, self.__chat.class_date())
