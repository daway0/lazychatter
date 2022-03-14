from student import Student
from bidi.algorithm import get_display
import arabic_reshaper


class Professor:
    def __init__(self) -> None:
        self.__students = {}

    def add_student(self, student: Student) -> None:
        self.__students[student.name()] = student

    def get_student(self, student_name: str) -> Student:
        return self.__students[student_name]

    def student_name_list(self):
        return self.__students.keys()

    def sorted_name_list(self):
        name_list = self.student_name_list()
        reshaped_names_list = []

        for name in name_list:
            reshaped_text = arabic_reshaper.reshape(name)
            artext = get_display(reshaped_text)
            reshaped_names_list.append(
                ((f'{artext} [{self.get_student(name).number_all_chats()} in {self.get_student(name).number_all_classes()}]'), self.get_student(name)))

        number_chats_list = []
        all_chats = 0
        for name in self.student_name_list():
            number_student_chats = self.get_student(
                name).number_all_chats()
            all_chats += number_student_chats
            number_chats_list.append(number_student_chats)

        # sorting data by number of chat messages
        #
        desorted_list_tuple = []
        for i in range(len(number_chats_list)):
            desorted_list_tuple.append(
                (reshaped_names_list[i], number_chats_list[i]))
        sorted_list_tuple = self.__sort_tuple(desorted_list_tuple)

        return sorted_list_tuple

    def __sort_tuple(self, tup):
        tup.sort(key=lambda x: x[1])
        return tup
