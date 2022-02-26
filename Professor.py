from Student import Student


class Professor:
    def __init__(self) -> None:
        self.__students = {}

    def add_student(self, student: Student) -> None:
        self.__students[student.name()] = student

    def get_student(self, student_name) -> Student:
        return self.__students[student_name]

    def student_name_list(self):
        return self.__students.keys()
